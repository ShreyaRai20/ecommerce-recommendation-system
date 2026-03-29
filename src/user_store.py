"""
UserStore Module

This module manages user-related data using a hash table (Python dictionary).
It stores user IDs and their corresponding product ratings.

Time Complexity:
- Add user: O(1)
- Add rating: O(1)
- Get ratings: O(1)
"""

class UserStore:
    def __init__(self):
        # Dictionary to store user data
        # Format: { user_id: { product_id: rating } }
        self.users = {}

    def add_user(self, user_id):
        """
        Adds a new user to the system.

        Args:
            user_id (str): Unique identifier for the user
        """
        self.users[user_id] = {}

    def add_rating(self, user_id, product_id, rating):
        """
        Adds or updates a rating for a product by a user.

        Args:
            user_id (str): User identifier
            product_id (str): Product identifier
            rating (float/int): Rating given by the user
        """
        # If user does not exist, create a new entry
        if user_id not in self.users:
            self.add_user(user_id)

        # Store or update the rating
        self.users[user_id][product_id] = rating

    def get_user_ratings(self, user_id):
        """
        Retrieves all ratings for a given user.

        Args:
            user_id (str): User identifier

        Returns:
            dict: Product-rating mapping or empty dict if user not found
        """
        return self.users.get(user_id, {})