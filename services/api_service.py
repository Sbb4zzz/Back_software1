import requests, os
from config import Config

class FootballAPIService:

    BASE_URL = "https://api.football-data.org/v4"
    HEADERS = {
        "X-Auth-Token": Config.FOOTBALL_API_KEY
    }

    @staticmethod
    def get_world_cup_matches():
        url = f"{FootballAPIService.BASE_URL}/competitions/WC/matches"
        response = requests.get(url, headers=FootballAPIService.HEADERS)

        if response.status_code != 200:
            raise Exception(f"API error: {response.text}")

        return response.json()

    @staticmethod
    def get_world_cup_standings():
        url = f"{FootballAPIService.BASE_URL}/competitions/WC/standings"
        response = requests.get(url, headers=FootballAPIService.HEADERS)

        if response.status_code != 200:
            raise Exception(response.text)

        return response.json()