from booking.booking import Booking

# you pass tear_down if you want to close the browser window when done

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.close_cookie_banner()
        bot.change_currency(currency='SEK')
        bot.select_place_to_go("Stockholm")
        bot.select_dates(check_in_date='2021-09-15',
                         check_out_date='2021-09-28')
        bot.select_adults(10)
        bot.click_search()
        bot.apply_filtration()
except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You need to install chromedriver and add it to PATH.\n'
            'You can find it here: https://sites.google.com/a/chromium.org/chromedriver/downloads'
        )
    else:
        raise e
