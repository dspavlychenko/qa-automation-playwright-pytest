# QA Automation: Playwright + Pytest + requests

[![Tests](https://github.com/dspavlychenko/qa-automation-playwright-pytest/actions/workflows/tests.yml/badge.svg)](https://github.com/dspavlychenko/qa-automation-playwright-pytest/actions)

Portfolio test automation framework covering **UI**, **REST API** and **GraphQL** testing.

| Layer | Target | Tools |
|---|---|---|
| UI | [saucedemo.com](https://www.saucedemo.com) | Playwright, Page Object Model |
| REST API | [Restful-Booker](https://restful-booker.herokuapp.com/apidoc) | requests |
| GraphQL | [Countries API](https://countries.trevorblades.com) | requests |

## Features
- **Page Object Model** – locators and actions live in `pages/`, tests stay readable
- **No hard sleeps** – Playwright auto-waiting and `expect` assertions
- **Test data via API** – fixtures create and clean up data through the API
- **Parametrized tests**, pytest markers (`ui`, `api`, `smoke`)
- **Parallel run** with `pytest-xdist`
- **CI** on GitHub Actions, **Allure** results

## Project structure
```
api/        API clients (REST, GraphQL)
config/     settings from env variables
pages/      Page Objects
tests/ui    UI tests
tests/api   API tests
```

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium

pytest                  # all tests
pytest -m smoke         # smoke only
pytest -m api           # API only
pytest -n 4             # in parallel
pytest --headed         # see the browser
allure serve allure-results   # report (requires Allure CLI)
```
