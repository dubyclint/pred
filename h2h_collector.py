# h2h_collector.py

import os
import requests

RAPID_API_KEY = os.getenv("API_SPORTS_KEY")

def search_basketball_team(name):
    url = f"https://v1.basketball.api-sports.io/teams?search={name}"
    headers = {'x-rapidapi-host': "v1.basketball.api-sports.io", 'x-rapidapi-key': RAPID_API_KEY}
    try:
        response = requests.get(url, headers=headers).json()
        return response['response'][0]['team']['name'] if response['results'] > 0 else None
    except:
        return None

def search_football_team(name):
    url = f" https://v1.football.api-sports.io/teams?search={name}"
    headers = {'x-rapidapi-host': "v1.football.api-sports.io", 'x-rapidapi-key': RAPID_API_KEY}
    try:
        response = requests.get(url, headers=headers).json()
        return response['response'][0]['team']['name'] if response['results'] > 0 else None
    except:
        return None

def search_tennis_player(name):
    url = f" https://v1.tennis.api-sports.io/players?search={name}"
    headers = {'x-rapidapi-host': "v1.tennis.api-sports.io", 'x-rapidapi-key': RAPID_API_KEY}
    try:
        response = requests.get(url, headers=headers).json()
        return response['response'][0]['player']['name'] if response['results'] > 0 else None
    except:
        return None

def search_hockey_team(name):
    url = f" https://v1.hockey.api-sports.io/teams?search={name}"
    headers = {'x-rapidapi-host': "v1.hockey.api-sports.io", 'x-rapidapi-key': RAPID_API_KEY}
    try:
        response = requests.get(url, headers=headers).json()
        return response['response'][0]['team']['name'] if response['results'] > 0 else None
    except:
        return None

def search_volleyball_team(name):
    url = f" https://v1.volleyball.api-sports.io/teams?search={name}"
    headers = {'x-rapidapi-host': "v1.volleyball.api-sports.io", 'x-rapidapi-key': RAPID_API_KEY}
    try:
        response = requests.get(url, headers=headers).json()
        return response['response'][0]['team']['name'] if response['results'] > 0 else None
    except:
        return None

def search_cricket_team(name):
    url = f" https://v1.cricket.api-sports.io/teams?search={name}"
    headers = {'x-rapidapi-host': "v1.cricket.api-sports.io", 'x-rapidapi-key': RAPID_API_KEY}
    try:
        response = requests.get(url, headers=headers).json()
        return response['response'][0]['team']['name'] if response['results'] > 0 else None
    except:
        return None

# --- Placeholder functions for fetching last six matches ---
# In a real scenario, these would interact with your sports API (RapidAPI)
# to fetch actual head-to-head match data.
def get_last_six_basketball_matches(team_a_api_name, team_b_api_name):
    """Placeholder: Returns dummy H2H basketball matches."""
    # Implement actual API call here
    return [
        {"scores": {"home": {"third": 25, "total": 100}, "away": {"third": 22, "total": 95}}},
        {"scores": {"home": {"third": 20, "total": 90}, "away": {"third": 23, "total": 98}}},
        {"scores": {"home": {"third": 28, "total": 110}, "away": {"third": 18, "total": 85}}},
        {"scores": {"home": {"third": 21, "total": 92}, "away": {"third": 20, "total": 88}}},
        {"scores": {"home": {"third": 24, "total": 105}, "away": {"third": 26, "total": 108}}},
        {"scores": {"home": {"third": 19, "total": 80}, "away": {"third": 25, "total": 90}}},
    ]

def get_last_six_football_matches(team_a_api_name, team_b_api_name):
    """Placeholder: Returns dummy H2H football matches."""
    # Implement actual API call here
    return [
        {"home": {"first_half": 1, "second_half": 1, "total": 2}, "away": {"first_half": 0, "second_half": 1, "total": 1}},
        {"home": {"first_half": 0, "second_half": 1, "total": 1}, "away": {"first_half": 1, "second_half": 1, "total": 2}},
        {"home": {"first_half": 2, "second_half": 0, "total": 2}, "away": {"first_half": 0, "second_half": 0, "total": 0}},
        {"home": {"first_half": 1, "second_half": 0, "total": 1}, "away": {"first_half": 0, "second_half": 0, "total": 0}},
        {"home": {"first_half": 0, "second_half": 2, "total": 2}, "away": {"first_half": 1, "second_half": 0, "total": 1}},
        {"home": {"first_half": 0, "second_half": 0, "total": 0}, "away": {"first_half": 0, "second_half": 1, "total": 1}},
    ]

def get_last_six_tennis_matches(player_a_api_name, player_b_api_name):
    """Placeholder: Returns dummy H2H tennis matches."""
    # Implement actual API call here
    return [
        {"winner": player_a_api_name, "scores": "6-4 6-2"},
        {"winner": player_b_api_name, "scores": "7-5 6-7 6-4"},
        {"winner": player_a_api_name, "scores": "6-1 6-0"},
        {"winner": player_b_api_name, "scores": "6-3 6-3"},
        {"winner": player_a_api_name, "scores": "7-6 6-4"},
        {"winner": player_a_api_name, "scores": "6-2 6-3"},
    ]

def get_last_six_hockey_matches(team_a_api_name, team_b_api_name):
    """Placeholder: Returns dummy H2H hockey matches."""
    # Implement actual API call here
    return [
        {"scores": {"home": 3, "away": 2}},
        {"scores": {"home": 1, "away": 4}},
        {"scores": {"home": 5, "away": 1}},
        {"scores": {"home": 2, "away": 3}},
        {"scores": {"home": 4, "away": 0}},
        {"scores": {"home": 2, "away": 2}}, # Example of a draw/tie game
    ]

def get_last_six_volleyball_matches(team_a_api_name, team_b_api_name):
    """Placeholder: Returns dummy H2H volleyball matches."""
    # Implement actual API call here
    return [
        {"sets": {"home": 3, "away": 1}},
        {"sets": {"home": 2, "away": 3}},
        {"sets": {"home": 3, "away": 0}},
        {"sets": {"home": 1, "away": 3}},
        {"sets": {"home": 3, "away": 2}},
        {"sets": {"home": 0, "away": 3}},
    ]

def get_last_six_cricket_matches(team_a_api_name, team_b_api_name):
    """Placeholder: Returns dummy H2H cricket matches."""
    # Implement actual API call here
    return [
        {"winner": team_a_api_name, "runs_a": 250, "runs_b": 230},
        {"winner": team_b_api_name, "runs_a": 180, "runs_b": 185},
        {"winner": team_a_api_name, "runs_a": 300, "runs_b": 280},
        {"winner": team_b_api_name, "runs_a": 210, "runs_b": 220},
        {"winner": team_a_api_name, "runs_a": 150, "runs_b": 140},
        {"winner": team_a_api_name, "runs_a": 270, "runs_b": 265},
    ]
