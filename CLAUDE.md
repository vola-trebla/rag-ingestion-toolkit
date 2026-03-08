# Project Rules

## Git
- Conventional commits: `feat:`, `fix:`, `chore:`, `refactor:`, `docs:`, `test:`
- Never commit directly to main. Always create a feature branch (`feat/...`, `fix/...`, `chore/...`)
- Create a PR and merge through GitHub
- After committing, automatically push and create a PR without asking
- After PR is merged: when user confirms merge, switch to main, pull latest, and delete the merged feature branch

## Python
- Formatter/linter: ruff
- Run `ruff check --fix` and `ruff format` before committing
