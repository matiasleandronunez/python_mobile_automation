from pages.basePage import BasePage
from context.config import settings


class ArticlePage(BasePage):
    instance = None
    _ARTICLE_HEADER_ID = f"{settings.app_package}:id/view_page_header_container"
    _ARTICLE_TITLE_ID = f"{settings.app_package}:id/view_page_title_text"
    _ARTICLE_TITLES_EPY_ID = f"{settings.app_package}:id/view_page_subtitle_text"

    def __init__(self, driver):
        super().__init__(driver)

    def _validate_page(self):
        pass

    def get_article_main_title(self):
        return self.driver.get_driver().\
            find_element_by_id(self._ARTICLE_HEADER_ID).\
            find_element_by_id(self._ARTICLE_TITLE_ID).text.strip()

    def get_article_main_title_epy(self):
        return self.driver.get_driver().\
            find_element_by_id(self._ARTICLE_HEADER_ID).\
            find_element_by_id(self._ARTICLE_TITLES_EPY_ID).text.strip()

