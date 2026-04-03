"""
OptimizedUserStore Module

This module manages user data efficiently using a hash table (Python dictionary)
with added caching for Top-N recommendations.

Purpose:
- Fast insertion and retrieval of user-product ratings
- Quick computation of Top-N recommendations using cache
- Scalable for large datasets

Time Complexity:
- Add user/rating: O(1)
- Get user ratings: O(1)
- Get Top-N: O(m log m) for first computation, O(1) if cached
"""

from collections import defaultdict

class OptimizedUserStore:
    def __init__(self):
        """
        Initialize the user store and cache.
        users: stores user ratings { user_id: { product_id: rating } }
        cache_top_n: caches Top-N results per user to speed up repeated queries
        """
        self.users = {}
        self.cache_top_n = {}  # Cache for Top-N recommendations per user

    def add_user(self, user_id):
        """
        Adds a new user to the system if not already present.
        
        Args:
            user_id (str): Unique user identifier
        """
        self.users[user_id] = {}

    def add_rating(self, user_id, product_id, rating):
        """
        Adds or updates a rating for a product by a user.
        Invalidates cached Top-N recommendations for the user.

        Args:
            user_id (str): User identifier
            product_id (str): Product identifier
            rating (float): Rating given by the user
        """
        # If user does not exist, create a new entry
        if user_id not in self.users:
            self.add_user(user_id)

        # Update the rating in the user dictionary
        self.users[user_id][product_id] = rating

        # Invalidate cached Top-N recommendations for this user
        self.cache_top_n.pop(user_id, None)

    def get_user_ratings(self, user_id):
        """
        Retrieves all ratings for a specific user.

        Args:
            user_id (str): User identifier

        Returns:
            dict: Product-rating mapping, empty dict if user not found
        """
        return self.users.get(user_id, {})

    def get_top_n(self, user_id, n=5):
        """
        Returns the Top-N products for a user using cached values if available.
        First computation sorts ratings to find Top-N.

        Args:
            user_id (str): User identifier
            n (int): Number of top recommendations

        Returns:
            list: List of product_ids in descending order of rating
        """
        # Check if Top-N for this user is already cached
        if user_id in self.cache_top_n:
            return self.cache_top_n[user_id]

        # Retrieve user ratings
        ratings = self.get_user_ratings(user_id)

        # Sort ratings in descending order and pick top N
        top_n = sorted(ratings.items(), key=lambda x: x[1], reverse=True)[:n]

        # Cache result for future use
        self.cache_top_n[user_id] = [p for p, _ in top_n]

        return self.cache_top_n[user_id]