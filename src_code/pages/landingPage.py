from pages.basePage import BasePage
from context.config import settings


class LandingPage(BasePage):
    instance = None
    _SEARCH_BUTTON_XPATH = "(//android.widget.ImageView[@content-desc='Search Wikipedia'])[1]"
    _SEARCH_INPUT_ID = f"{settings.app_package}:id/search_src_text"
    _RESULT_LIST_ID = f"{settings.app_package}:id/page_list_item_container"

    def __init__(self, driver):
        super().__init__(driver)

    def _validate_page(self):
        pass

    def search_article(self, search_term):
        self.driver.get_driver().find_element_by_xpath(self._SEARCH_BUTTON_XPATH).click()
        self.driver.get_driver().find_element_by_id(self._SEARCH_INPUT_ID).send_keys(search_term)

    def select_first_result(self):
        self.driver.get_driver().find_elements_by_id(self._RESULT_LIST_ID)[0].click()

