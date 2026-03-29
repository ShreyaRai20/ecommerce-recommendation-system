"""
Test Module

This file contains unit tests to validate the correctness
of the recommendation logic.

Run using:
pytest
"""

from src.heap_recommender import get_top_n_recommendations

def test_top_n():
    """
    Test case to verify Top-N recommendation functionality.
    """

    # Sample input scores
    scores = {
        "P1": 1,
        "P2": 5,
        "P3": 3
    }

    # Get top 2 products
    result = get_top_n_recommendations(scores, 2)

    # Assertions
    assert "P2" in result  # Highest score must be included
    assert len(result) == 2  # Only 2 results should be returned