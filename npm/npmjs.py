from playwright.sync_api import sync_playwright, Playwright

package = "ex"                     # express / ex
def run(playwright: Playwright): 
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"height": 800, "width": 1280})
    page = context.new_page()
    page.goto(f"https://www.npmjs.com/package/{package}")
    name = page.locator('//span[@class="_50685029 truncate"]').inner_text()
    version_l = page.get_by_role("heading").filter(has_text="Version")
    version = version_l.locator("xpath=following-sibling::*[1]").inner_text()
    license_l = page.locator('//h3[@class="c84e15be f5 mt2 pt2 mb0"]').filter(has_text="License")
    license = license_l.locator("xpath=following-sibling::*[1]").inner_text()
    downloads_l = page.get_by_role('heading').filter(has_text="Weekly Downloads")
    downloads = downloads_l.locator("xpath=following-sibling::*[1]").inner_text() 
    print("Name: ",name, "| Version: ",version, "| License: ",license, "| Weekely Downloads: ",downloads)
    page.wait_for_timeout(3000)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)