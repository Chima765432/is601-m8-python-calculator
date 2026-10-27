import pytest


@pytest.mark.e2e
@pytest.mark.parametrize("button, a, b, expected", [
    ("Subtract", "9", "4", "5"),
    ("Multiply", "6", "7", "42"),
    ("Divide", "9", "2", "4.5"),
    ("Add", "-3", "1.5", "-1.5"),
])
def test_each_button_shows_the_result(page, fastapi_server, button, a, b, expected):
    page.goto("http://localhost:8000")
    page.fill("#a", a)
    page.fill("#b", b)
    page.click(f'button:text("{button}")')
    page.wait_for_selector("#result:not(:empty)")
    assert page.inner_text("#result") == f"Calculation Result: {expected}"


@pytest.mark.e2e
def test_empty_input_shows_an_error(page, fastapi_server):
    page.goto("http://localhost:8000")
    page.fill("#a", "5")
    page.click('button:text("Add")')
    page.wait_for_selector("#result:not(:empty)")
    assert page.inner_text("#result").startswith("Error:")
