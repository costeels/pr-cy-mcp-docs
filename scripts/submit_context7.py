"""Submit a public documentation repository using a Context7 API key."""
import argparse
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.request

parser = argparse.ArgumentParser(description='Submit a public GitHub documentation repository to Context7 for parsing.')
parser.add_argument('--repository-url', required=True)
args = parser.parse_args()
if not re.fullmatch(r'https://github\.com/[A-Za-z0-9-]+/[A-Za-z0-9_.-]+/?', args.repository_url):
    parser.error('Provide a public https://github.com/OWNER/REPOSITORY URL.')
key = os.environ.get('CONTEXT7_API_KEY')
if not key:
    raise SystemExit('CONTEXT7_API_KEY is missing. Provide your Context7 key securely in the process environment, or submit the repository through https://context7.com/add-library.')
request = urllib.request.Request(
    'https://context7.com/api/v2/add/repo/github',
    data=json.dumps({'docsRepoUrl': args.repository_url.rstrip('/')}).encode('utf-8'),
    headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json', 'User-Agent': 'pr-cy-mcp-docs-submitter'},
    method='POST',
)
try:
    with urllib.request.urlopen(request, timeout=50) as response:
        result = json.load(response)
except urllib.error.HTTPError as error:
    raise SystemExit(f'Context7 returned HTTP {error.code}. Check the public repository URL, API key and library status before retrying.')
Path('submission-result.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
print('Submission received. Wait for parsing to complete and verify documentation retrieval before reporting the library as indexed.')
