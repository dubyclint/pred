# pattern_detector.py

import numpy as np

def detect_repeating_pattern(h2h_matches, sport="basketball"):
    if not h2h_matches: # Handle empty list
        return {"summary": "No head-to-head data for pattern detection."}

    if sport == "basketball":
        return detect_basketball_pattern(h2h_matches)
    elif sport == "football":
        return detect_football_pattern(h2h_matches)
    elif sport == "tennis":
        return detect_tennis_pattern(h2h_matches)
    elif sport == "hockey":
        return detect_hockey_pattern(h2h_matches)
    elif sport == "volleyball":
        return detect_volleyball_pattern(h2h_matches)
    elif sport == "cricket":
        return detect_cricket_pattern(h2h_matches)
    else:
        return {"summary": "No specific pattern detection implemented for this sport."}

def detect_basketball_pattern(h2h_matches):
    q3_scores_a = [m["scores"]["home"]["third"] for m in h2h_matches]
    q3_scores_b = [m["scores"]["away"]["third"] for m in h2h_matches]

    count_a_high_q3 = sum(1 for s in q3_scores_a if s >= 20)
    count_b_high_q3 = sum(1 for s in q3_scores_b if s >= 20)

    std_a_q3 = np.std(q3_scores_a) if q3_scores_a else 0
    std_b_q3 = np.std(q3_scores_b) if q3_scores_b else 0

    summary = []
    if count_a_high_q3 >= 5:
        summary.append("Strong Q3 play (Home)")
    if count_b_high_q3 >= 5:
        summary.append("Strong Q3 play (Away)")
    if std_a_q3 <= 2 and q3_scores_a:
        summary.append("Consistent Q3 scoring (Home)")
    if std_b_q3 <= 2 and q3_scores_b:
        summary.append("Consistent Q3 scoring (Away)")

    # Ensure max_point_diff is calculated safely if h2h_matches is not empty
    max_point_diff = max(abs(m["scores"]["home"]["total"] - m["scores"]["away"]["total"]) for m in h2h_matches) if h2h_matches else 0

    return {
        "q3_trend": "High Q3 output" if count_a_high_q3 >= 5 else ("Consistent Q3" if std_a_q3 < 2 else "Balanced Q3 play"),
        "max_point_diff": max_point_diff,
        "summary": " | ".join(summary) if summary else "No strong pattern detected for Basketball."
    }

def detect_football_pattern(h2h_matches):
    first_half_a = [m["home"]["first_half"] for m in h2h_matches]
    second_half_a = [m["home"]["second_half"] for m in h2h_matches]
    first_half_b = [m["away"]["first_half"] for m in h2h_matches]
    second_half_b = [m["away"]["second_half"] for m in h2h_matches]

    count_home_strong_start = sum(1 for g in first_half_a if g >= 1)
    count_away_strong_start = sum(1 for g in first_half_b if g >= 1)

    count_home_strong_finish = sum(1 for g in second_half_a if g >= 1)
    count_away_strong_finish = sum(1 for g in second_half_b if g >= 1)

    summary = []

    if count_home_strong_start >= 4:
        summary.append("Strong starters (Home)")
    if count_away_strong_start >= 4:
        summary.append("Strong starters (Away)")

    if count_home_strong_finish >= 4:
        summary.append("Late-game finishers (Home)")
    if count_away_strong_finish >= 4:
        summary.append("Late-game finishers (Away)")

    max_goal_diff = max(abs(m["home"]["total"] - m["away"]["total"]) for m in h2h_matches) if h2h_matches else 0

    return {
        "start_trend": "Strong start" if count_home_strong_start >= 4 else ("Balanced" if count_home_strong_start == count_away_strong_start else "Weak start"),
        "finish_trend": "Strong finish" if count_home_strong_finish > count_away_strong_finish else "Even finish",
        "max_goal_diff": max_goal_diff,
        "summary": " | ".join(summary) if summary else "No strong pattern detected for Football."
    }

def detect_tennis_pattern(h2h_matches):
    """Placeholder for tennis pattern detection."""
    # Example: Analyze set wins, tie-break frequency, serve break patterns.
    # For now, a generic placeholder.
    return {"summary": "No specific pattern detection implemented for Tennis."}

def detect_hockey_pattern(h2h_matches):
    """Placeholder for hockey pattern detection."""
    # Example: Analyze goal scoring periods, power play conversion rates, penalty trends.
    return {"summary": "No specific pattern detection implemented for Hockey."}

def detect_volleyball_pattern(h2h_matches):
    """Placeholder for volleyball pattern detection."""
    # Example: Analyze set score patterns, blocking trends, ace serves.
    return {"summary": "No specific pattern detection implemented for Volleyball."}

def detect_cricket_pattern(h2h_matches):
    """Placeholder for cricket pattern detection."""
    # Example: Analyze run rates in powerplay, wicket falls, common run scoring partnerships.
    return {"summary": "No specific pattern detection implemented for Cricket."}
