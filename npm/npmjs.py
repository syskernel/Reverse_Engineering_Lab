from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright): 
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"height": 800, "width": 1280})
    page = context.new_page()
    page.goto("https://www.npmjs.com/package/express")
    page.wait_for_timeout(10000)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)