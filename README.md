# QA Automation: Playwright + Pytest + requests

[![Tests](https://github.com/dspavlychenko/qa-automation-playwright-pytest/actions/workflows/tests.yml/badge.svg)](https://github.com/dspavlychenko/qa-automation-playwright-pytest/actions)

Portfolio test automation framework covering **UI** and **REST API** testing.

| Layer | Target | Tools |
|---|---|---|
| UI | [saucedemo.com](https://www.saucedemo.com) | Playwright, Page Object Model |
| REST API | [Restful-Booker](https://restful-booker.herokuapp.com/apidoc) | requests |

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
- **CI** on GitHub Actions: flake8 → all tests (chromium)

## Project structure
```
api/        REST API client
config/     settings from env variables
pages/      Page Objects
tests/ui    UI tests: login, products, cart, checkout
tests/api   API tests: auth, booking CRUD, negative cases
.github/    CI workflow
```

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

pytest                          # all tests (chromium by default)
pytest -m smoke                 # smoke only
pytest -m api                   # API only (no browser needed)
pytest -m ui --browser firefox  # UI in another browser
pytest -n 4                     # in parallel
pytest --headed                 # see the browser
flake8 --max-line-length=120 .   # lint (pip install flake8)
allure serve allure-results     # report (requires Allure CLI)
```

Settings can be overridden through environment variables or a `.env` file (see `.env.example`).

## CI
Workflow: [`.github/workflows/tests.yml`](.github/workflows/tests.yml) – one job on every push to `main` and every pull request:

1. `flake8` lint
2. install Playwright chromium
3. `pytest` (all UI + API tests)

If a test fails, the Playwright traces are uploaded as the `test-results` artifact.
Open a trace with `playwright show-trace trace.zip`.
