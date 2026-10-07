from playwright.sync_api import sync_playwright, Playwright
import sys

def run(playwright: Playwright, package): 
    dependency = []
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
    repository = page.locator('//a[@aria-labelledby="repository repository-link"]').get_attribute("href")
    homepage = page.locator('//a[@aria-labelledby="homePage homePage-link"]').get_attribute("href")
    page.locator('//a[@id="package-tab-dependencies"]').click()
    for row in page.locator('//ul[@aria-label="Dependencies"]').get_by_role("listitem").all():
        dependency.append(row.text_content())
    dependency = ", ".join(dependency)

    print("Name: ",name, "| Version: ",version, "| License: ",license, "| Weekely Downloads: ",downloads, "| Repository: ", repository, "| Homepage: ", homepage, "| Dependencies: ", dependency)
    page.wait_for_timeout(3000)
    browser.close()

def main():
    if len(sys.argv) < 2:
        print("Please enter the package you want to search! ")
    elif len(sys.argv) > 2:
        print("Pleae enter one package at a time!")
    else:
        pkg = sys.argv[1]
        with sync_playwright() as playwright:
            run(playwright, pkg)

if __name__ == "__main__":
    main()