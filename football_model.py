# football_model.py

import numpy as np
from h2h_collector import search_football_team, get_last_six_football_matches
from pattern_detector import detect_football_pattern

WEIGHTS = {
    "key_players": 0.3,
    "bench_depth": 0.1,
    "defensive_rating": 0.15,
    "motivation": 0.1,
    "h2h_win_percent": 0.08,
    "turnover_rate": -0.05,
    "possession_edge": 0.07,
    "goal_scoring": 0.07,
    "injury_status": -0.05,
    "coach_strategy": 0.05,
    "pattern_confidence": 0.17
}

def calculate_strength_score(stats):
    return sum(w * stats.get(k, 0) for k, w in WEIGHTS.items())

def predict_football_match(team_a, team_b, match_date):
    api_home = search_football_team(team_a)
    api_away = search_football_team(team_b)

    if not api_home or not api_away:
        return {"error": f"Team not found: {team_a} vs {team_b}"}

    h2h_matches = get_last_six_football_matches(api_home, api_away)
    if not h2h_matches:
        return default_football_prediction(api_home, api_away, match_date)

    patterns = detect_football_pattern(h2h_matches)
    
    team_a_stats = get_team_stats(api_home)
    team_b_stats = get_team_stats(api_away)

    strength_a = calculate_strength_score(team_a_stats)
    strength_b = calculate_strength_score(team_b_stats)

    delta = strength_a - strength_b
    win_a = 1 / (1 + np.exp(-0.8 * delta))
    win_b = 1 - win_a

    home_min = max(0, int((strength_a - 0.5) * 10))
    home_max = int((strength_a + 0.5) * 10)
    away_min = max(0, int((strength_b - 0.5) * 10))
    away_max = int((strength_b + 0.5) * 10)
    total_min = max(0, int((strength_a + strength_b - 1.0) * 10))
    total_max = int((strength_a + strength_b + 1.0) * 10)

    return {
        "match": f"{api_home} vs {api_away}",
        "date": match_date,
        "sport": "Football",
        "winner": api_home if win_a > win_b else api_away,
        "win_percent": win_a if win_a > win_b else win_b,
        "score_range": {
            "home_min": home_min,
            "home_max": home_max,
            "away_min": away_min,
            "away_max": away_max,
            "total_min": total_min,
            "total_max": total_max
        },
        "pattern_summary": patterns["summary"],
        "probabilities": {
            "Win A": win_a,
            "Draw": 0.0,
            "Win B": win_b
        }
    }

def get_team_stats(team_name):
    """Placeholder for fetching actual football team statistics.
    Replace with real data retrieval logic."""
    # This is a mock-up. You'd integrate with a data source here.
    return {
        "key_players": 7.5,
        "bench_depth": 6.5,
        "defensive_rating": 8.0,
        "motivation": 4.5,
        "h2h_win_percent": 0.6,
        "turnover_rate": 0.1,
        "possession_edge": 0.05,
        "goal_scoring": 7.0,
        "injury_status": 0.05,
        "coach_strategy": 7.0,
    }

def default_football_prediction(team_a_name, team_b_name, match_date):
    """
    Provides a default football prediction when head-to-head data is not available.
    """
    import random
    winner = random.choice([team_a_name, team_b_name])
    return {
        "match": f"{team_a_name} vs {team_b_name}",
        "date": match_date,
        "sport": "Football",
        "winner": winner,
        "win_percent": 0.51,
        "score_range": {
            "home_min": 0, "home_max": 3,
            "away_min": 0, "away_max": 3,
            "total_min": 0, "total_max": 6
        },
        "pattern_summary": "No head-to-head data for pattern detection. Default prediction.",
        "probabilities": {
            "Win A": 0.51 if winner == team_a_name else 0.49,
            "Draw": 0.0,
            "Win B": 0.51 if winner == team_b_name else 0.49
        }
    }
