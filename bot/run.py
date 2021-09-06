from booking.booking import Booking

# you pass tear_down if you want to close the browser window when done

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.close_cookie_banner()
        bot.change_currency(currency='SEK')
        bot.select_place_to_go(input("Where you want to go?"))
        # format is 2021-09-15
        bot.select_dates(check_in_date=input("Check in date?"),
                         check_out_date=input("Check out date?"))
        bot.select_adults(int(input("How many adults?")))
        bot.click_search()
        bot.apply_filtration()
        bot.refresh()  # work around to let the bot grab the right data cause it's too fast
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You need to install chromedriver and add it to PATH.\n'
            'You can find it here: https://sites.google.com/a/chromium.org/chromedriver/downloads'
        )
    else:
        raise e
