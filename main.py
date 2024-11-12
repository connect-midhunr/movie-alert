import requests
import json
import time
import pygame
from datetime import datetime

def save_response(response):
    try:
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Save the response data to a JSON file
            with open('response.json', 'w') as file:
                json.dump(data, file, indent=4)
            
            print(f"Response saved to file successfully.")
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred during API request: {e}")

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


def get_movie_sessions():
    url = 'https://api3.pvrcinemas.com/api/v1/booking/content/csessions'
    headers = {'Content-Type': 'application/json', 'City': 'Kochi', 'AppVersion': '1.0', 'Platform': 'WEBSITE'}

    # Request body
    payload = {
        "city": "Kochi",
        "cid": "477",
        "lat": "9.891130756",
        "lng": "76.292316",
        "dated": "2024-09-01",
        "qr": "NO",
        "cineType": "",
        "cineTypeQR": ""
    }

    booking_started = False
    try:
        while not booking_started:

            # Making the POST request to the API
            response = requests.post(url, headers=headers, json=payload)
            save_response(response)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Convert response content to string
                response_str = response.content.decode('utf-8')
                # print(response_str)

                # Check if specific string exists in the response
                if 'THE GREATEST OF ALL TIME' in response_str:
                    print("Alert: 'THE GREATEST OF ALL TIME' found in the response!")
                    booking_started = True
                    break
                    # Add alarm triggering code here

                print("Booking not started! Time:", datetime.now())
                time.sleep(300)

            else:
                print(f"Request failed with status code: {response.content}")

        play_music('loud.mp3')

    except requests.exceptions.RequestException as e:
        print(f"Error occurred during API request: {e}")

# Calling the function to fetch movie sessions and check for the string
get_movie_sessions()