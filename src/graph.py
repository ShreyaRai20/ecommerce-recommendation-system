"""
Graph Module

This module represents user-product relationships using an adjacency list.
Each user is connected to products they have interacted with.

Used for:
- Collaborative filtering
- Traversing user-product relationships

Time Complexity:
- Add edge: O(1)
- Get neighbors: O(1)
"""

class Graph:
    def __init__(self):
        # Adjacency list representation
        # Format: { user: [(product, rating), ...] }
        self.adj = {}

    def add_edge(self, user, product, rating):
        """
        Adds a connection (edge) between a user and a product.

        Args:
            user (str): User identifier
            product (str): Product identifier
            rating (float/int): Interaction weight
        """
        # Initialize list if user does not exist
        if user not in self.adj:
            self.adj[user] = []

        # Append product interaction
        self.adj[user].append((product, rating))

    def get_neighbors(self, user):
        """
        Retrieves all products connected to a user.

        Args:
            user (str): User identifier

        Returns:
            list: List of (product, rating) tuples
        """
        return self.adj.get(user, [])