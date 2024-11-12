from helpers import *
from automate_browser_action import *
from datetime import datetime
import time

data = load_json_file('movie_details.json')
movie_title = format_movie_title(data['movie-title'])
movie_code = format_movie_code(data['movie-code'])
cinema = data['cinema']
city = format_city(data['city'])
date = format_date(data['date'])
format = data['format']

movie_page_url = generate_movie_page_url(movie_title, movie_code, city)
movie_ticket_booking_page_url = generate_movie_ticket_booking_page_url(movie_title, movie_code, city, date)

print()

if __name__ == "__main__":
    try:
        while True:
            start_time = datetime.now()

            switch_to_chrome()
            open_new_tab()
            # enter_url_in_address_bar(movie_page_url)
            # movie_page_source_code = copy_paste_source_code()
            # if "Book tickets" in movie_page_source_code:
            #     print(datetime.now(), ": Movie ticket booking page is opened...!")
            enter_url_in_address_bar(movie_ticket_booking_page_url)
            page_title = f"{data['movie-title']} {data['format']} Movie, Showtimes in {data['city']} & Online Ticket Booking"
            list_of_venues = retrieve_list_of_venues(page_title)
            if list_of_venues and cinema in list_of_venues:
                print(datetime.now(), f": Booking started at {cinema}...!")
                play_music('loud.mp3')
                break
            else:
                print(datetime.now(), f": Booking not started at {cinema}...!")
                close_current_tab()

            end_time = datetime.now()
            print("Time taken:", round((end_time - start_time).total_seconds(), 3), 'seconds')
            time.sleep(90)
            print()

    except Exception as e:
        print(datetime.now(), ": Exception occurred:", e)
        play_music('Friends.mp3')