import streamlit as st
import requests
from paytm import check_movie
from datetime import date
import time
from helpers import play_music

url = 'https://hckinfo.kerala.gov.in/digicourt/Casedetailssearch'

from urllib.request import Request, urlopen
sleep_time = 60

def check_website_exists(url):
    try:
        response = requests.head(url)
        return response.status_code
    except requests.ConnectionError:
        return False

if __name__ == '__main__':

    # Title
    st.title("Streamlit App with Textbox, Date, and Button")

    # Textbox
    movie = st.text_input("Enter the text:")

    # Date picker
    selected_date = st.date_input("Pick a date:", date.today()).strftime("%Y-%m-%d")

    # Button
    if st.button("Submit"):
        try:
            # Set headers to mimic a real browser request
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",
            }

            started = False
            while not started:
                started = check_movie(selected_date, movie, sleep_time, headers)
                if started:
                    st.write("Started!")
                    play_music("Friends.mp3")
                else:
                    time.sleep(sleep_time)
            
        except Exception as e:
            print(f"Error occurred: {e}")
