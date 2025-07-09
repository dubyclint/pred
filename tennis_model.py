# tennis_model.py

import numpy as np
from h2h_collector import search_tennis_player, get_last_six_tennis_matches
from pattern_detector import detect_tennis_pattern

WEIGHTS = {
    "serve_power": 0.25,
    "return_game": 0.2,
    "fitness": 0.15,
    "motivation": 0.1,
    "h2h_win_percent": 0.1,
    "unforced_errors_rate": -0.05,
    "break_point_conversion": 0.08,
    "experience": 0.07,
    "injury_status": -0.05,
    "coach_strategy": 0.05,
    "pattern_confidence": 0.15
}

def calculate_strength_score(stats):
    return sum(w * stats.get(k, 0) for k, w in WEIGHTS.items())

def predict_tennis_match(player_a, player_b, match_date):
    api_home = search_tennis_player(player_a)
    api_away = search_tennis_player(player_b)

    if not api_home or not api_away:
        return {"error": f"Player not found: {player_a} vs {player_b}"}

    h2h_matches = get_last_six_tennis_matches(api_home, api_away)
    if not h2h_matches:
        return default_tennis_prediction(api_home, api_away, match_date)

    patterns = detect_tennis_pattern(h2h_matches)
    
    player_a_stats = get_team_stats(api_home) # Re-using get_team_stats for player stats
    player_b_stats = get_team_stats(api_away)

    strength_a = calculate_strength_score(player_a_stats)
    strength_b = calculate_strength_score(player_b_stats)

    delta = strength_a - strength_b
    win_a = 1 / (1 + np.exp(-0.8 * delta))
    win_b = 1 - win_a

    # Tennis score ranges are set-based, so this is a simplified representation
    home_sets_min = int(max(0, strength_a / 5))
    home_sets_max = int(min(3, strength_a / 3)) # Max 3 sets for best of 3, 5 for best of 5
    away_sets_min = int(max(0, strength_b / 5))
    away_sets_max = int(min(3, strength_b / 3))

    return {
        "match": f"{api_home} vs {api_away}",
        "date": match_date,
        "sport": "Tennis",
        "winner": api_home if win_a > win_b else api_away,
        "win_percent": win_a if win_a > win_b else win_b,
        "score_range": { # Simplified set prediction
            "home_min": home_sets_min, "home_max": home_sets_max,
            "away_min": away_sets_min, "away_max": away_sets_max,
            "total_min": max(home_sets_min, away_sets_min), # Total sets played
            "total_max": max(home_sets_max, away_sets_max)
        },
        "pattern_summary": patterns["summary"],
        "probabilities": {
            "Win A": win_a,
            "Draw": 0.0, # No draws in tennis
            "Win B": win_b
        }
    }

def get_team_stats(player_name):
    """Placeholder for fetching actual tennis player statistics.
    Replace with real data retrieval logic."""
    # This is a mock-up. You'd integrate with a data source here.
    return {
        "serve_power": 8.0,
        "return_game": 7.5,
        "fitness": 8.5,
        "motivation": 4.0,
        "h2h_win_percent": 0.6,
        "unforced_errors_rate": 0.07,
        "break_point_conversion": 0.45,
        "experience": 9.0,
        "injury_status": 0.02,
        "coach_strategy": 7.0,
    }

def default_tennis_prediction(player_a_name, player_b_name, match_date):
    """
    Provides a default tennis prediction when head-to-head data is not available.
    """
    import random
    winner = random.choice([player_a_name, player_b_name])
    return {
        "match": f"{player_a_name} vs {player_b_name}",
        "date": match_date,
        "sport": "Tennis",
        "winner": winner,
        "win_percent": 0.51,
        "score_range": {
            "home_min": 0, "home_max": 2, # Sets won
            "away_min": 0, "away_max": 2,
            "total_min": 2, "total_max": 3 # Total sets played
        },
        "pattern_summary": "No head-to-head data for pattern detection. Default prediction.",
        "probabilities": {
            "Win A": 0.51 if winner == player_a_name else 0.49,
            "Draw": 0.0,
            "Win B": 0.51 if winner == player_b_name else 0.49
        }
    }
