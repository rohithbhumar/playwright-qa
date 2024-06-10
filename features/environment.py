from playwright.sync_api import sync_playwright
from pages.uiplaygroundhome import UIPlayGroundHome

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.ui_home = UIPlayGroundHome(page=context.page, url="http://www.uitestingplayground.com")

def after_all(context):
    context.page.close()
    context.browser.close()
    context.playwright.stop()
