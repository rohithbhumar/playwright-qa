from playwright.sync_api import Page


class UIPlayGroundHome:

    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url

    def navigate_to_url(self):
        self.page.goto(url=self.url)

    def link_dynamic_id(self):
        dynamic_id_link = self.page.get_by_role("link", name="Dynamic ID")
        return dynamic_id_link

    def all_h3_link_texts(self):
        all_h3_links = self.page.locator("//h3/a")
        all_h3_texts = [h3_link_text.inner_text() for h3_link_text in all_h3_links.all()]
        return all_h3_texts

    def btn_dynamic_id(self):
        dynamic_id_link = self.page.get_by_role("button", name="Button with Dynamic ID")
        return dynamic_id_link
