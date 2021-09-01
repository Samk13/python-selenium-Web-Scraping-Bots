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

    def close_cookie_banner(self):
        close_button = self.find_element_by_id(
            'onetrust-accept-btn-handler')
        print("should be clicked now!")
        close_button.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_result = self.find_element_by_css_selector('li[data-i="0"]')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]')
        check_out_element.hover()
