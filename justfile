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
    uv run ruff format --check

types:
    uv run pyright src

lint-fix:
    uv run ruff check --fix
    uv run ruff format

test:
    uv run pytest tests

test-coverage:
    uv run coverage run -p -m pytest tests

merge-coverage:
    uv run coverage combine
    uv run coverage html --skip-covered --skip-empty

    # Report and write to summary (if on github actions).
    if [ -n "$$GITHUB_ACTIONS" ]; then \
        uv run coverage report --format=markdown >> $$GITHUB_STEP_SUMMARY; \
    fi

    # Report again and fail if under 70%.
    uv run coverage report --fail-under=70

dist:
    uv build
    ls -l dist

upload-test:
    uvx twine upload dist/* --repository testpypi

upload:
    uvx twine upload dist/*
