# Publish and submit the documentation

This package can be hosted in a new public GitHub repository and submitted to Context7. It contains only English documentation, interface schemas and publication helpers. PR-CY API credentials and account data are not needed for publication and must not be uploaded.

## Publish on GitHub

Choose the GitHub account or organization authorized to host the documentation. The suggested repository name is `pr-cy-mcp-docs`; the package does not assume a particular GitHub owner.

Use your existing GitHub authentication or provide a GitHub token through the `GITHUB_TOKEN` process environment. A token needs permission to create the selected repository and publish its files. Organization restrictions can require an organization owner's involvement.

If Git Credential Manager is installed and has no saved GitHub login, start the normal device sign-in and complete it yourself:

```bash
git credential-manager github login --device --no-ui
```

After selecting the correct owner, run the publication helper from the package folder:

```bash
python scripts/publish_github.py --owner YOUR_GITHUB_ACCOUNT --repository pr-cy-mcp-docs
```

The helper creates a **new public repository**, commits the documentation and verifies the published file tree. It refuses to replace an existing repository. If it creates a repository but a later step fails, inspect that repository instead of blindly rerunning creation.

For an existing repository, add the package through your normal Git workflow in an appropriate branch and review the changes before merging.

## Submit to Context7

Open [Context7 Add Library](https://context7.com/add-library), select GitHub and paste the published repository URL. The root `context7.json` selects `docs/` for parsing; root-level Markdown is also included according to Context7's current parsing rules.

For API submission, obtain your Context7 API key from the dashboard and provide it through the `CONTEXT7_API_KEY` process environment. Run:

```bash
python scripts/submit_context7.py --repository-url https://github.com/YOUR_GITHUB_ACCOUNT/pr-cy-mcp-docs
```

The helper uses the documented endpoint and request shape:

```http
POST https://context7.com/api/v2/add/repo/github
Authorization: Bearer YOUR_CONTEXT7_API_KEY
Content-Type: application/json
```

```json
{
  "docsRepoUrl": "https://github.com/YOUR_GITHUB_ACCOUNT/pr-cy-mcp-docs"
}
```

The API key is for **Context7**, not PR-CY. This submits a public repository; no GitHub access token is sent to Context7 by the helper. The helper records the returned submission data in `submission-result.json`, which is excluded from version control.

## Verify availability

A submitted repository can still be queued or parsing. Wait for the Context7 library to be ready and use the actual returned library ID. Check retrieval with these questions:

```text
How do I authenticate the PR-CY MCP server in Codex?
Does get_wordstat accept an engine input?
How does get_project_events.date_to differ from get_project_notes.date_to?
Which device_type values does get_page_screenshot support?
How do I edit an HTML artifact using the current revision_id?
```

Successful submission is not proof of successful indexing. Confirm that answers retrieve the relevant pages and current examples before reporting completion.

## Optional ownership and updates

Once the library exists, follow [Claim Your Library](https://context7.com/docs/howto/claiming-libraries) using the maintainer's own account. Add only the claim details generated for that account. Ownership is not required merely to submit a public repository.

After future documentation changes, push the updated files and refresh the existing Context7 library. See [Keeping Libraries Fresh](https://context7.com/docs/library-updates).
