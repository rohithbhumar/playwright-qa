import re
import time

from playwright.sync_api import sync_playwright

# sync_playwright().start()
with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=200, args=['--start-maximized'])
    print(browser)

    # create a new page
    page = browser.new_page(no_viewport=True)

    # visit the playwright website
    page.goto("https://playwright.dev/python")
    get_started_btn = page.get_by_role("link", name="Get started")
    get_started_btn.highlight()
    get_started_btn.click()
    page.get_by_role('link', name='Docs').click()
    print(page.url)

    page.locator("xpath=//a[@class='breadcrumbs__link']").click()  # xpath= is optional

    page.goto("https://bootswatch.com/default/")
    primary_button = page.get_by_role("button", name="Primary")
    primary_button.locator("nth=0").highlight()

    # parent element locator using '..'
    page.locator("//h2[text() = 'Example body text']").locator("..").highlight()
    print(page.get_by_text("Heading 1").inner_text())

    # Mouse Clicks
    block_button = page.get_by_role("button", name="Block button").first
    block_button.hover()
    block_button.click(button="right")
    time.sleep(1)
    block_button.click()
    block_button.click(modifiers=["Shift"], delay=2000)
    time.sleep(2)

    #  Input (send_keys) is = fill()
    email_filed = page.locator("//input[@id='exampleInputEmail1']")
    email_filed.fill("joe@example.com")
    email_filed.clear()
    # human typed send_keys/ type()
    email_filed.type("joe@example.com", delay=200)
    print(email_filed.input_value())
    time.sleep(1)
    print(email_filed.get_attribute("value"))

    # radio button and checkbox - .check(). Can use click() also






