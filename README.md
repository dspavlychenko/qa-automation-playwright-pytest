# QA Automation: Playwright + Pytest + requests

[![Tests](https://github.com/dspavlychenko/qa-automation-playwright-pytest/actions/workflows/tests.yml/badge.svg)](https://github.com/dspavlychenko/qa-automation-playwright-pytest/actions)

<<<<<<< HEAD
Portfolio test automation framework covering **UI** and **REST API** testing.
=======
Portfolio test automation framework covering **UI**, **REST API** and **GraphQL** testing.
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7

| Layer | Target | Tools |
|---|---|---|
| UI | [saucedemo.com](https://www.saucedemo.com) | Playwright, Page Object Model |
| REST API | [Restful-Booker](https://restful-booker.herokuapp.com/apidoc) | requests |
<<<<<<< HEAD

## Features
- **Page Object Model** – locators and actions live in `pages/` (with a `BasePage`), tests stay readable
- **No hard sleeps** – Playwright auto-waiting and `expect` assertions; fixtures wait until the page is ready
- **REST API coverage** – auth, full CRUD (GET/POST/PUT/PATCH/DELETE), filtering, negative cases
- **Test data via API** – fixtures create data through the API and always clean it up (`yield` teardown)
- **Parametrized tests** – invalid-login matrix (wrong/empty/case-sensitive/SQL-like input), cart and sorting scenarios
- **Request timeouts** – every API call goes through one `_request` wrapper with a timeout
- **Known bugs tracked with `xfail(strict=True)`** – the run turns red once the bug is fixed
- **Parallel run** with `pytest-xdist`, **markers** (`ui`, `api`, `smoke`)
- **Allure** reports with feature/story grouping
- **CI** on GitHub Actions: lint → API job + UI matrix (chromium, firefox) → Allure report

## Project structure
```
api/        REST API client
config/     settings from env variables
pages/      Page Objects
tests/ui    UI tests: login, products, cart, checkout
tests/api   API tests: auth, booking CRUD, negative cases
.github/    CI workflow
=======
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
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
```

## Run locally
```bash
<<<<<<< HEAD
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

pytest                          # all tests (chromium by default)
pytest -m smoke                 # smoke only
pytest -m api                   # API only (no browser needed)
pytest -m ui --browser firefox  # UI in another browser
pytest -n 4                     # in parallel
pytest --headed                 # see the browser
ruff check .                    # lint
allure serve allure-results     # report (requires Allure CLI)
```

Settings can be overridden through environment variables or a `.env` file (see `.env.example`).

## CI
Workflow: [`.github/workflows/tests.yml`](.github/workflows/tests.yml)

| Job | What it does |
|---|---|
| `lint` | `ruff check .` |
| `api` | `pytest -m api` in parallel |
| `ui` | `pytest -m ui` on chromium and firefox (matrix); Playwright browsers are cached |
| `report` | merges Allure results and publishes the report to GitHub Pages (`main` only) |

On a failed UI run the **trace, screenshot and video** are uploaded as the `playwright-artifacts-<browser>` artifact.
Open a trace with `playwright show-trace trace.zip`.

To get the published Allure report: *Settings → Pages → Source: Deploy from a branch → `gh-pages` / `(root)`*
(the `gh-pages` branch is created by the first run on `main`).
=======
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
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
