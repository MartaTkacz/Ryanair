import time
import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = Chrome()

    # Wait before attempting interactions
    driver.implicitly_wait(3)
    driver.maximize_window()

    # Return the driver object at the end of setup
    yield driver

    # Quit the driver
    driver.quit()


def test_ryanair_website(browser):
    URL = 'https://www.ryanair.com'

    # Navigate to the Ryanair website
    browser.get(URL)
    # Close cookies
    browser.find_element_by_id('glyphs.close').click()
    # Find departure input textbox
    departure = browser.find_element_by_id('input-button__departure')
    # Find destination input textbox
    destination = browser.find_element_by_id('input-button__destination')

    # Type in Dublin and press enter
    departure.send_keys('Dublin' + Keys.RETURN)
    # Type in Barcelona
    destination.send_keys('Barcelona')
    # Click on Barcelona from the dropdown
    browser.find_element_by_xpath('//hp-airport-item/span/span[contains(text(),\' Barcelona \')]').click()

    # Find the month September and click on it from the dropdown
    september = browser.find_element_by_xpath('//div[contains(text(),\'Sep \')]')
    september.click()
    time.sleep(2)

    # Find the exact date in september and select it
    depart_date = browser.find_element_by_xpath('//div[contains(@data-id, \'2020-09-08\')]')
    depart_date.click()
    time.sleep(2)

    # Find the exact return date and select it
    arrival_date = browser.find_element_by_xpath('//div[contains(@data-id, \'2020-09-12\')]')
    arrival_date.click()
    time.sleep(2)

    # Add an extra adult
    add_adult = browser.find_element_by_xpath(
        '//ry-counter-button[contains(@aria-label, '
        '\'1Adults+1\')]//div//parent::div//parent::div//parent::ry-counter-button//parent::div')
    add_adult.click()

    # Find and click on the search button and wait
    search_button = browser.find_element_by_xpath('//button//ry-spinner')
    search_button.click()
    time.sleep(5)

    # Find and click on the first departure flight available
    depart_flight = browser.find_element_by_xpath(
        '//journey-container[@data-ref=\'outbound\']//flight-list//flight-card[1]')
    depart_flight.click()
    time.sleep(2)

    # Select regular type of ticket
    regular_departure_ticker = browser.find_element_by_xpath('//div[@class=\'fare-card fare-card--secondary\']')
    regular_departure_ticker.click()
    time.sleep(2)

    # Find and click on the first return flight
    arrival_flight = browser.find_element_by_xpath(
        '//journey-container[@data-ref=\'inbound\']//flight-list//flight-card[1]')
    arrival_flight.click()
    time.sleep(2)

    # Select the regular type of ticket
    arrival_departure_ticker = browser.find_element_by_xpath('//div[@class=\'fare-card fare-card--secondary\']')
    arrival_departure_ticker.click()
    time.sleep(2)

    # Confirm that the login popup appears
    login_string = browser.find_element_by_xpath('//ry-login-touchpoint-container//h3').text
    assert login_string == 'Log in to myRyanair'

    # Confirm that the passengers section is displayed
    passengers_string = browser.find_element_by_xpath('//div//h3[@class=\'app-title\']').text
    assert passengers_string == 'Passengers'

    # Confirm that the passengers section is disabled
    passenger_details_input = browser.find_element_by_xpath('//div[@class=\'form-wrapper form-wrapper--disabled\']')
    assert passenger_details_input.is_displayed()

    # Find and move to 'Login later' button in order to type in passenger details
    login_later_button = browser.find_element_by_xpath(
        '//div[@class=\'login-touchpoint\']//span[contains(text(),\'Log in later\')]//parent::div//parent::button')
    actions = ActionChains(browser)
    actions.move_to_element(login_later_button).perform()
    time.sleep(3)
    assert login_later_button.is_displayed()
    login_later_button.click()

    # Confirm that the passenger section is no longer disabled
    passenger_details_input = browser.find_elements_by_xpath('//div[@class=\'form-wrapper form-wrapper--disabled\']')
    assert not len(passenger_details_input)

    # Find and fll in Passenger 1 details
    passenger_1_title = browser.find_element_by_xpath(
        '//span[contains(text(),\' Passenger 1 \')]//parent::h4//parent::div//parent::div//pax-passenger-details'
        '-container//ry-dropdown//div[@class=\'dropdown b2\']')
    passenger_1_title.click()

    mr_tag = browser.find_element_by_xpath('//ry-dropdown-item//div[contains(text(),\'Mr\')]')
    mr_tag.click()

    passenger_1_name = browser.find_element_by_id('formState.passengers.ADT-0.name')
    passenger_1_name.send_keys("Bob")

    passenger_1_surname = browser.find_element_by_id('formState.passengers.ADT-0.surname')
    passenger_1_surname.send_keys('Bobson')

    # Find and fill out passenger 2 details
    passenger_2_title = browser.find_element_by_xpath(
        '//pax-passenger-container//span[contains(text(),\' Passenger 2 '
        '\')]//parent::h4//parent::div//parent::div//pax-passenger-details-container//ry-dropdown//div['
        '@class=\'dropdown b2\']')
    passenger_2_title.click()
    time.sleep(3)

    mrs_tag = browser.find_element_by_xpath(
        '//div[@data-ref=\'pax-details__ADT-1\']//ry-dropdown-item//div[contains(text(),\'Mrs\')]')
    mrs_tag.click()

    passenger_2_name = browser.find_element_by_id('formState.passengers.ADT-1.name')
    passenger_2_name.send_keys("Mary")

    passenger_2_surname = browser.find_element_by_id('formState.passengers.ADT-1.surname')
    passenger_2_surname.send_keys('Kelly')

    # Find and click on the 'Continue' button
    continue_button = browser.find_element_by_xpath(
        '//button[@class=\'continue-flow__button ry-button--gradient-yellow\']')
    time.sleep(3)
    continue_button.click()
    time.sleep(10)

    # Confirm that the seats selection page is displayed
    seats_selection_page_header = browser.find_element_by_xpath('//h3[contains(text(),\'Where would you like to sit?\')]')
    time.sleep(5)
    assert seats_selection_page_header.is_displayed()

    # Find first free seat in the included section of the plane
    select_standard_seat = browser.find_element_by_xpath(
        '//span[contains(text(), \'Included\')]//parent::div//parent::div//parent::div//parent::priceband//parent'
        '::div//div//button[@class=\'ng-star-inserted seatmap__seat seatmap__seat--standard\']')
    select_standard_seat.click()
    time.sleep(5)

    # Find and select the next free seat in the included section of the plane
    select_standard_seat2 = browser.find_element_by_xpath(
        '//span[contains(text(), \'Included\')]//parent::div//parent::div//parent::div//parent::priceband//parent'
        '::div//div//button[@class=\'ng-star-inserted seatmap__seat seatmap__seat--standard\']')
    select_standard_seat2.click()
    time.sleep(5)

    # Click on ;Next flight' button
    next_button = browser.find_element_by_xpath('//span//button[contains(text(), \' Next flight \')]')
    next_button.click()
    time.sleep(10)

    # Select the standard seats again
    select_standard_seat = browser.find_element_by_xpath(
        '//span[contains(text(), \'Included\')]//parent::div//parent::div//parent::div//parent::priceband//parent'
        '::div//div//button[@class=\'ng-star-inserted seatmap__seat seatmap__seat--standard\']')
    select_standard_seat.click()
    time.sleep(5)

    # Select the standard seats again
    select_standard_seat2 = browser.find_element_by_xpath(
        '//span[contains(text(), \'Included\')]//parent::div//parent::div//parent::div//parent::priceband//parent'
        '::div//div//button[@class=\'ng-star-inserted seatmap__seat seatmap__seat--standard\']')
    select_standard_seat2.click()
    time.sleep(5)

    # Click on 'Continue' button
    continue_button = browser.find_element_by_xpath('//span//button[contains(text(), \' Continue \')]')
    continue_button.click()
    time.sleep(10)

    # Confirm that the next page about baggage is displayed
    bags_header = browser.find_element_by_xpath('//span[contains(text(), \' What bags are you taking on board? \')]')
    assert bags_header.is_displayed()
