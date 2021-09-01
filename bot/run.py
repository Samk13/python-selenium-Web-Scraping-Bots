from booking.booking import Booking

# you pass tear_down if you want to close the browser window when done
with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='SEK')
    bot.close_cookie_banner()
    bot.select_place_to_go("Stockholm, Stockholm county, Sweden")
