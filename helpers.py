import json
import pygame

dict_city = {
    "KOCHI": "koch"
}

# function to write a string to a TXT file
def write_string_to_txt_file(string_content):
    try:
        file_path = 'temp.txt'
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(string_content)
        print(f"Content has been written to '{file_path}' successfully.")
    except IOError as e:
        print(f"Error writing to file: {e}")

# function to load JSON data from a file
def load_json_file(filename: str):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# function to format movie title
def format_movie_title(title: str):
    formatted_title = title.lower().replace(' ', '-')
    print("Movie title:", formatted_title)
    return formatted_title

# function to format movie code
def format_movie_code(code: str):
    formatted_code = code.upper()
    print("Movie code:", formatted_code)
    return formatted_code

# function to format cinema
def format_cinema(cinema: str):
    formatted_cinema = cinema.title()
    print("Cinema:", formatted_cinema)
    return formatted_cinema

# function to format city
def format_city(city: str):
    formatted_city = city.lower()
    print("City:", formatted_city)
    return formatted_city

# function to return city code
def get_city_code(city: str):
    city_code = dict_city[city.upper()]
    print("City code:", city_code)
    return city_code

# function to format date
def format_date(date: str):
    formatted_city = ''.join(date.split('-')[::-1])
    print("Date:", formatted_city)
    return formatted_city

# function to generate movie page url
def generate_movie_page_url(movie_title, movie_code, city):
    url = f"https://in.bookmyshow.com/{city}/movies/{movie_title}/{movie_code}"
    print("Movie ticket booking page URL:", url)
    return url

# function to generate movie ticket booking page url
def generate_movie_ticket_booking_page_url(movie_title, movie_code, city, date):
    url = f"https://in.bookmyshow.com/buytickets/{movie_title}-{city}/movie-{get_city_code(city)}-{movie_code}-MT/{date}"
    print("Movie page URL:", url)
    return url

def play_music(file_path):
    # Initialize pygame
    pygame.init()

    try:
        # Load the MP3 file
        pygame.mixer.music.load(file_path)

        # Play the loaded music file
        pygame.mixer.music.play()

        # Keep the program running until music playback is finished
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Adjust tick speed for smoother playback

    except pygame.error as e:
        print(f"Error occurred while playing the music: {e}")

    finally:
        # Stop and quit pygame
        pygame.mixer.music.stop()
        pygame.quit()