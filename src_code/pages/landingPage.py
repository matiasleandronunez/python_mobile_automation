from pages.basePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    instance = None
    _SEARCH_BUTTON_XPATH = "(//android.widget.ImageView[@content-desc='Search Wikipedia'])[1]"
    _SEARCH_INPUT_ID = f"{super().package_name}:id/search_src_text"
    _RESULT_LIST_ID = f"{super().package_name}:id/fragment_feed_feed"

    def __init__(self, driver):
        super().__init__(driver)

    def search_article(self, search_term):
        self.driver.get_driver().find_element_by_xpath(self._SEARCH_BUTTON_XPATH).click()
        self.driver.get_driver().find_elements_by_id(self._SEARCH_INPUT_ID).send_keys(search_term)

