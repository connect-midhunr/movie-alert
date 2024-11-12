import requests
from bs4 import BeautifulSoup
import time
from helpers import write_string_to_txt_file, play_music

selected_date = "2024-11-14"
film = "Kanguva"
sleep_time = 60

def check_movie(selected_date, film, sleep_time, headers):
    url = f"https://paytm.com/movies/trivandrum/ariesplex-sl-cinemas-cinionic-dolby-atmos-vanchiyoor-thiruvananthapuram-c/1018571?fromdate={selected_date}"
    response = requests.get(url, headers=headers)
    write_string_to_txt_file(response.text)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        movies = [element.get_text() for element in soup.find_all("div", class_="MovieSessionsListingDesktop_movieDetailsDivHeading__INXv0")]

        if not movies:
            print("No movie details found with the specified class.")
        elif film not in movies:
            print(f"Booking for {film} is yet to start.")
        else:
            print(f"Booking for {film} has started at Ariesplex SL Cinemas.")
            return True
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

    return False

if __name__ == '__main__':
    try:
        # Set headers to mimic a real browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }

        started = False
        while not started:
            started = check_movie(date, film, sleep_time, headers)
            if started:
                play_music("Friends.mp3")
            else:
                time.sleep(sleep_time)
        
    except Exception as e:
        print(f"Error occurred: {e}")
