"""Publish this documentation package as a new public GitHub repository.

Authenticate using GITHUB_TOKEN / GH_TOKEN or an existing Git Credential
Manager login. No token is written to a file, command argument or log.
"""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent.parent

def github_token():
    token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GH_TOKEN')
    if token:
        return token
    env = os.environ.copy()
    env.update(GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
    result = subprocess.run(['git', 'credential', 'fill'], input='protocol=https\nhost=github.com\n\n', text=True, capture_output=True, timeout=20, env=env)
    fields = dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)
    token = fields.get('password')
    if not token:
        raise SystemExit('GitHub authentication is missing. Sign in with Git Credential Manager or provide GITHUB_TOKEN securely in the environment.')
    return token

def api(token, path, method='GET', body=None):
    data = None if body is None else json.dumps(body).encode('utf-8')
    headers = {'Authorization': 'Bearer ' + token, 'Accept': 'application/vnd.github+json', 'Content-Type': 'application/json', 'User-Agent': 'pr-cy-mcp-docs-publisher', 'X-GitHub-Api-Version': '2022-11-28'}
    with urllib.request.urlopen(urllib.request.Request('https://api.github.com' + path, data=data, headers=headers, method=method), timeout=30) as response:
        return json.load(response)

def publish(owner, repository):
    token = github_token()
    user = api(token, '/user')
    repo_path = f'/repos/{owner}/{repository}'
    try:
        api(token, repo_path)
    except urllib.error.HTTPError as error:
        if error.code != 404:
            raise
    else:
        raise SystemExit('That repository already exists. This publisher creates a new repository and will not replace existing content.')
    files = []
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if any(part.startswith('.') for part in relative.parts) and relative.name != '.gitignore':
            continue
        if '__pycache__' in relative.parts or path.suffix in ('.pyc', '.zip'):
            continue
        if path.name in ('submission-result.json', 'publication-result.json'):
            continue
        text = path.read_text(encoding='utf-8')
        files.append({'path': relative.as_posix(), 'mode': '100644', 'type': 'blob', 'content': text})
    if not any(item['path'] == 'context7.json' for item in files):
        raise SystemExit('context7.json is missing from the package.')
    create_path = '/user/repos' if owner.lower() == user['login'].lower() else f'/orgs/{owner}/repos'
    created = api(token, create_path, 'POST', {'name': repository, 'description': 'English documentation for the PR-CY MCP server: SEO, rankings, audits, analytics and content tools.', 'private': False, 'auto_init': True})
    print('Created public repository: ' + created['html_url'], flush=True)
    initial_branch = created['default_branch']
    head = api(token, repo_path + '/git/ref/heads/' + initial_branch)
    parent = api(token, repo_path + '/git/commits/' + head['object']['sha'])
    tree = api(token, repo_path + '/git/trees', 'POST', {'base_tree': parent['tree']['sha'], 'tree': files})
    commit = api(token, repo_path + '/git/commits', 'POST', {'message': 'Add English PR-CY MCP documentation for Context7', 'tree': tree['sha'], 'parents': [parent['sha']]})
    if initial_branch == 'main':
        api(token, repo_path + '/git/refs/heads/main', 'PATCH', {'sha': commit['sha'], 'force': False})
    else:
        api(token, repo_path + '/git/refs', 'POST', {'ref': 'refs/heads/main', 'sha': commit['sha']})
    api(token, repo_path, 'PATCH', {'default_branch': 'main'})
    check = api(token, repo_path + '/git/trees/' + tree['sha'] + '?recursive=1')
    published_files = {item['path'] for item in check['tree'] if item['type'] == 'blob'}
    expected = {item['path'] for item in files}
    if not expected.issubset(published_files):
        raise SystemExit('The repository was created but the published tree is incomplete; inspect it before retrying.')
    print(json.dumps({'repository_url': created['html_url'], 'commit': commit['sha'], 'files_verified': len(expected), 'context7_status': 'not_submitted'}))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a NEW PUBLIC GitHub repository containing this documentation package.')
    parser.add_argument('--owner', required=True, help='GitHub account or organization authorized to host this documentation.')
    parser.add_argument('--repository', default='pr-cy-mcp-docs')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]{0,38}', args.owner):
        parser.error('Invalid GitHub owner.')
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,99}', args.repository):
        parser.error('Invalid repository name.')
    try:
        publish(args.owner, args.repository)
    except urllib.error.HTTPError as error:
        raise SystemExit(f'GitHub returned HTTP {error.code}; check authentication, permissions and the repository state. No automatic retry was attempted.')
