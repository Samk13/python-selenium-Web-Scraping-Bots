import os
import booking.constants as const
from selenium import webdriver


class Booking(webdriver.Chrome):
    """docstring for Booking."""

    def __init__(self, driver_path=const.DRIVERS_PATH, tear_down=False):
        self.driver_path = driver_path
        self.tear_down = tear_down
        os.environ["PATH"] += os.pathsep + self.driver_path
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, *args):
        if self.tear_down:
            self.quit()
