from pages.landingPage import LandingPage
from context import driver

def before_feature(context, feature):
    pass

def before_scenario(context, scenario):
    context.driver = driver.Driver()

    # Instantiate pages into context for use within the test
    context.landing_page = LandingPage(context.driver)

    #launch the app
    context.driver.start_app()

def after_scenario(context, scenario):
    context.driver.stop_driver()
