from context.config import settings
from appium import webdriver
from appium.common.exceptions import *
from abc import abstractmethod


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def _validate_page(self):
        return

