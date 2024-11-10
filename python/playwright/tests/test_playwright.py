from playwright.sync_api import Page, expect
import pytest

@pytest.mark.regression
def test_check_page_title(page: Page):
    page.goto("file:///C:/workspace/test-apps/web/v1/web-form.html")
    expect(page).to_have_title("Web Form")