from context.config import settings
from appium import webdriver
from appium.common.exceptions import *
from abc import abstractmethod


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.package_name = settings.app_package

    @abstractmethod
    def _validate_page(self):
        return

