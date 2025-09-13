import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def launch_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(launch_browser):
    page = launch_browser.new_page()
    yield page
    page.close()
