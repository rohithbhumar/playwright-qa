# dynamic table
import pytest
from playwright.sync_api import sync_playwright, Page, expect
import logging


@pytest.fixture(autouse=True)
def visit_ui_play_page(page: Page):
    # playwright = sync_playwright().start()
    # browser = playwright.chromium.launch(headless=False)
    # page = browser.new_page()  // NO NEED TO DO THESE STEPS DUE TO page: Page
    page.goto("http://www.uitestingplayground.com")
    yield page
    page.close()


def test_btn_dynamic_id(page: Page):
    dynamic_id_link = page.get_by_role("link", name="Dynamic ID")
    expect(dynamic_id_link).to_contain_text("Dynamic ID")
    dynamic_id_link.click()

    btn_dynamic_id = page.get_by_text("Button with Dynamic ID")
    expect(btn_dynamic_id).to_be_visible()
    btn_dynamic_id.highlight()
    btn_dynamic_id.click()


def test_load_delay(page: Page):
    load_delay_link = page.get_by_role("link", name="Load Delay")
    expect(load_delay_link).to_be_visible() and expect(load_delay_link).to_contain_text("Load Delay")
    load_delay_link.click()
    logging.info("Loading......")

    btn_after_load_delay = page.get_by_role("button", name="Button Appearing After Delay")
    btn_after_load_delay.click()
    logging.info("Button clicked after delay!!")


def test_text_input(page: Page):
    text_input = page.get_by_role("link", name="Text Input")
    text_input.click()

    input_field = page.locator("input#newButtonName")
    user_text = "Good button"
    input_field.fill(user_text)
    updating_button = page.locator("css=button#updatingButton")
    updating_button.click(timeout=5000)

    expect(updating_button).to_have_text(user_text)


def test_scroll_bar(page: Page):
    scroll_bar_link = page.get_by_role("link", name="Scrollbars")
    scroll_bar_link.click()

    hidden_button = page.locator("button#hidingButton")
    hidden_button.scroll_into_view_if_needed()
    hidden_button.click()


def test_dynamic_table(page: Page):
    dyn_table = page.get_by_role("link", name="Dynamic Table")
    dyn_table.click()

    col_headers = page.get_by_role("columnheader")
    expect(col_headers).to_have_count(5)
    logging.info(f"Col. count: {col_headers.count()}")

    cpu_column = 0
    for i, column_name in enumerate(col_headers.all(), start=1):
        # print(column_name.inner_text())
        if column_name.inner_text() == "CPU":
            # print(column_name.inner_text())
            cpu_column = i
            break
    print(f"CPU is at column: {cpu_column}")

    # chrome_row = page.locator('//div[@role="row" and .//span[text()="Chrome"]]')
    chrome_row = page.get_by_role("row").filter(has_text="Chrome")  #
    print(chrome_row.inner_text())
    chrome_cpu = chrome_row.locator(f"//span[@role='cell'][{cpu_column}]")
    # chrome_cpu = chrome_row.get_by_role("row").nth(cpu_column)
    print(chrome_cpu.inner_text())

    orange_para_cpu_value = page.locator("css=p.bg-warning")
    # print(orange_para_cpu_value.inner_text())
    assert (orange_para_cpu_value.inner_text().split()[-1]) == chrome_cpu.inner_text()

def test_progress_bar(page: Page):
    progress_bar_link = page.get_by_role("link", name="Progress Bar")
    progress_bar_link.click()

    page.locator("button#startButton").click()
    progress_bar = page.get_by_role("progressbar")
    while True:
        value_now = int(progress_bar.get_attribute("aria-valuenow"))
        if value_now == 75:
            page.locator("css=button#stopButton").click()
            break
    print(value_now)
    assert value_now >= 75



