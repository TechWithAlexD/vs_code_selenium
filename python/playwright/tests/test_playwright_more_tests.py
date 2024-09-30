from playwright.sync_api import Page, expect

def test_check_page_title(page: Page):
    page.goto("file:///C:/workspace/test-apps/web/v1/web-form.html")
    #page.wait_for_timeout(1000)
    expect(page).to_have_title("Web Form")