# Project Rules

## Git
- Conventional commits: `feat:`, `fix:`, `chore:`, `refactor:`, `docs:`, `test:`
- Never commit directly to main. Always create a feature branch (`feat/...`, `fix/...`, `chore/...`)
- Create a PR and merge through GitHub
- Push only when explicitly asked
- After PR is merged: when user says "PR смержен" (or similar), switch to main, pull latest, and delete the merged feature branch

## Python
- Formatter/linter: ruff
- Run `ruff check --fix` and `ruff format` before committing
