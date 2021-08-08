import os
import json

settings = None


class Settings(object):
    """Simple singleton class for managing and accessing settings"""
    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'testsettings.json')) as f:
            settings = json.load(f)
            self.app_package = settings['app_package']
            self.main_activity = settings['main_activity']
            self.execute_in_grid = settings['execute_in_grid']
            self.grid_uri = settings['grid_uri']
            self.driver_timeout = int(settings['driver_timeout'])

settings = Settings()