"""
Main Module

This script demonstrates the working of the recommendation system.
It integrates all data structures and runs a simple test scenario.
"""

from user_store import UserStore
from graph import Graph
from heap_recommender import get_top_n_recommendations

def main():
    # Initialize data structures
    users = UserStore()
    graph = Graph()

    # -----------------------------
    # Step 1: Add user interactions
    # -----------------------------
    users.add_rating("U1", "P1", 5)
    users.add_rating("U1", "P2", 3)

    # -----------------------------
    # Step 2: Build graph edges
    # -----------------------------
    graph.add_edge("U1", "P1", 5)
    graph.add_edge("U1", "P2", 3)

    # -----------------------------
    # Step 3: Simulate recommendation scores
    # (In real systems, this comes from ML models)
    # -----------------------------
    scores = {
        "P3": 4.5,
        "P4": 4.7,
        "P5": 4.2
    }

    # -----------------------------
    # Step 4: Get Top-N recommendations
    # -----------------------------
    recommendations = get_top_n_recommendations(scores, 2)

    # Output results
    print("Top Recommendations:", recommendations)

# Entry point of the program
if __name__ == "__main__":
    main()