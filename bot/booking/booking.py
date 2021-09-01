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
        self.implicitly_wait(const.WAITING_TIME)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, *args):
        if self.tear_down:
            self.quit()

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            const.CURRENCY_SELECTOR)
        currency_element.click()

        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()
