from booking.booking import Booking

# you pass tear_down if you want to close the browser window when done
with Booking() as bot:
    bot.land_first_page()
    print('Exitig ...')