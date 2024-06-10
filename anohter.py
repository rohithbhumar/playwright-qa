from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page(no_viewport=True)

    page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")
    link_2015 = page.locator('//*[@id="2015"]')
    print("clicking on 2015")
    # page.pause()
    link_2015.click()

    start = perf_counter()

    tds = page.locator('//*[@id="table-body"]//tr//td[1]')
    print(tds.first.inner_text())
    time_taken = perf_counter() - start
    print(f"..movies loaded in {round(time_taken, 2)}")
    print(tds.count())

    print(type(tds.all()))  # list

    for td in tds.all():  # .all() converts the locator elements into an iterable (List in this case)
        print(td.inner_text())
        # print(type(td.inner_text()))  # str
        # break

    