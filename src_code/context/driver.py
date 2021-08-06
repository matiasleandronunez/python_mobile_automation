from appium import webdriver as appium_wd
from context.config import settings


class Driver(object):
    class SeleniumDriverNotFound(Exception):
        pass

    def __init__(self):
        capabilities = {}

        if settings.execute_in_grid:
            capabilities['appPackage'] = settings.app_package
            capabilities['platformName'] = 'Android'

            self.driver = appium_wd.Remote(command_executor=f"{settings.grid_uri}/wd/hub",
                                               desired_capabilities=capabilities)
        else:
            pass

    def get_driver(self):
        return self.driver

    def stop_driver(self):
        self.driver.close_app()

