from playwright.sync_api import Page, expect
import pytest

@pytest.mark.regression
def test_check_page_title(page: Page):
    page.goto("file:///C:/workspace/test-apps/web/v1/web-form.html")
    expect(page).to_have_title("Web Form")

@pytest.mark.only_browser('firefox')
def test_check_page_title_run_only_on_firefox(page: Page):
    page.goto("file:///C:/workspace/test-apps/web/v1/web-form.html")
    expect(page).to_have_title("Web Form")

@pytest.mark.skip_browser('firefox')
def test_check_page_title_skip_firefox(page: Page):
    page.goto("file:///C:/workspace/test-apps/web/v1/web-form.html")
    expect(page).to_have_title("Web Form")