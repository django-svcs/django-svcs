venv_path := justfile_directory() / ".venv"
set dotenv-load := true
os := os()
devcontainer := if env_var_or_default("USER", "nobody") == "vscode" {"true"} else {"false"}

clean: clean-build clean-test

clean-build:
    rm -rf build/
    rm -rf dist/
    rm -rf .eggs/
    find . -name '*.egg-info' -exec rm -rf {} +
    find . -name '*.egg' -exec rm -f {} +

clean-test:
    rm -f .coverage
    rm -fr htmlcov/
    rm -fr .pytest_cache

lint:
    uv run ruff check

test:
    uv run pytest

dist:
    uvx --from build pyproject-build --installer uv
    ls -l dist

upload-test:
    uvx twine upload dist/* --repository testpypi

upload:
    uvx twine upload dist/*
