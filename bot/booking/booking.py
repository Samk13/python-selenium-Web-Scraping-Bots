import os
import booking.constants as const
from selenium import webdriver
from booking.booking_filtration import BookingFiltration


class Booking(webdriver.Chrome):
    """docstring for Booking."""

    def __init__(self, driver_path=const.DRIVERS_PATH, tear_down=False):
        self.driver_path = driver_path
        self.tear_down = tear_down
        os.environ["PATH"] += os.pathsep + self.driver_path
        # ignore the driver warnings on the console
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            'excludeSwitches', ['enable-automation', 'enable-logging'])

        super(Booking, self).__init__(options=options)
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
        try:
            close_button = self.find_element_by_id(
                'onetrust-accept-btn-handler')
            print("should be clicked now!")
            close_button.click()
        except:
            print('not be able to find the cookie banner')
            pass

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
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]')
            decrease_adults_element.click()
            adults_value_element = self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute(
                "value")  # get the value of adults count
            if int(adults_value) == 1:
                break
        # if value of adults reach one we get out of the loop
        incrase_adults_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]')
        for i in range(count - 1):
            incrase_adults_element.click()

    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]')
        search_button.click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.sort_price_lower_first()
