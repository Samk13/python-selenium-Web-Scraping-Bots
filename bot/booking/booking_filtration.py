# This file will encapuslate the logic for filtering the booking data
# to only include the relevant data for the bot

# import static types from drivers so we can use autocomplete
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_start_rating(self, *star_values):
        star_filtration_box = self.driver.find_element_by_id('filter_class')
        star_child_elements = star_filtration_box.find_elements_by_css_selector(
            '*')
        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML').strip() == f'{star_value} stars'):
                    star_element.click()
