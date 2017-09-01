# dot-restrict-scopes

Django OAuth Toolkit extension to restrict the scopes available for an application.

## Installation

Just install directly from Github using using `pip`:

```bash
pip install -e git+https://github.com/cedadev/dot-restrict-scopes.git@tag_branch_or_commit_hash#egg=dot_restrict_scopes
```

## Usage

The restricted application must be enabled in your `settings.py`:

```python
# Add dot_restrict_scopes to INSTALLED_APPS
INSTALLED_APPS = [
    # ...
    'dot_restrict_scopes',
]

# Tell Django OAuth Toolkit to use the RestrictedApplication model
OAUTH2_PROVIDER_APPLICATION_MODEL = 'dot_restrict_scopes.RestrictedApplication'

# Tell Django OAuth Toolkit to use the scopes backend
OAUTH2_PROVIDER = {
    'SCOPES_BACKEND_CLASS': 'dot_restrict_scopes.scopes.RestrictApplicationScopes',
    # ...
}

# Tell dot-restrict-scopes which scopes backend it is wrapping
# NOTE: oauth2_provider.scopes.SettingsScopes is the default, so this is not
#       strictly necessary if you want to use scopes from settings
DOT_RESTRICT_SCOPES = {
    'WRAPPED_SCOPES_BACKEND_CLASS': 'oauth2_provider.scopes.SettingsScopes',
}
```
