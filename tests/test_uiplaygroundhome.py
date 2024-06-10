import time

from pages.uiplaygroundhome import UIPlayGroundHome
from playwright.sync_api import Page, expect
import pytest


@pytest.fixture(autouse=True)
def visit_ui_play_page(page: Page):
    ui_home = UIPlayGroundHome(page=page, url="http://www.uitestingplayground.com")
    ui_home.navigate_to_url()
    yield ui_home
    page.close()


def test_home_page(visit_ui_play_page: UIPlayGroundHome):
    page = visit_ui_play_page.page
    assert page.title() == "UI Test Automation Playground"
    actual_list = visit_ui_play_page.all_h3_link_texts()
    expected_list = ['Dynamic ID', 'Class Attribute', 'Hidden Layers', 'Load Delay', 'AJAX Data', 'Client Side Delay',
                     'Click', 'Text Input', 'Scrollbars', 'Dynamic Table', 'Verify Text', 'Progress Bar', 'Visibility',
                     'Sample App', 'Mouse Over', 'Non-Breaking Space', 'Overlapped Element', 'Shadow DOM']
    assert actual_list == expected_list


def test_click_dynamic_link(visit_ui_play_page: UIPlayGroundHome):
    ui_home = visit_ui_play_page
    expect(ui_home.link_dynamic_id()).to_be_visible() and expect(ui_home.link_dynamic_id()).to_have_count("Dynamic ID")
    ui_home.link_dynamic_id().click()

    expect(ui_home.btn_dynamic_id()).to_have_text("Button with Dynamic ID")
    expect(ui_home.btn_dynamic_id()).to_be_visible()
    ui_home.btn_dynamic_id().click()








