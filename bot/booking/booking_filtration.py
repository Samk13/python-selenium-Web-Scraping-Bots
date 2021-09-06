# This file will encapuslate the logic for filtering the booking data
# to only include the relevant data for the bot

# import static types from drivers so we can use autocomplete
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def sort_price_lower_first(self):
        element = self.driver.find_element_by_css_selector(
            'li[data-id="review_score_and_price"]')
        element.click()
