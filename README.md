# FastAPI Calculator

A calculator web application. FastAPI serves a page with two number inputs
and four buttons. Each button sends the numbers as JSON to a POST endpoint
(/add, /subtract, /multiply, /divide), the server validates them with
Pydantic, runs the operation, and returns the result as JSON, which the page
displays. Invalid input or division by zero returns a 400 with an error
message instead of crashing. The server logs every calculation and error.

## Setup

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    playwright install chromium

## Run

    python main.py

Then open http://127.0.0.1:8000.

## Tests

    pytest tests/unit tests/integration
    pytest tests/e2e

- Unit tests call the four functions in app/operations directly.
- Integration tests send requests to every endpoint through FastAPI's
  TestClient, including decimals, negatives, missing or non-numeric fields,
  and the home page.
- End-to-end tests start the server and use Playwright to fill the inputs,
  click each button, and check what the page shows, including the error for
  dividing by zero and for an empty input.

GitHub Actions runs all three on every push and pull request to main.
