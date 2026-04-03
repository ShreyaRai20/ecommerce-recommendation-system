"""
OptimizedGraph Module

This module represents user-product relationships using an adjacency list
with batch insertion support for efficient scaling.

Purpose:
- Store relationships between users and products
- Enable collaborative filtering and neighbor-based recommendations
- Batch operations allow faster population for large datasets

Time Complexity:
- add_edge: O(1)
- add_edges_batch: O(E) where E is the number of edges added
- get_neighbors: O(1)
"""

from collections import defaultdict

class OptimizedGraph:
    def __init__(self):
        """
        Initialize adjacency list.
        Each user maps to a list of (product_id, rating) tuples.
        """
        self.adj = defaultdict(list)

    def add_edge(self, user, product, rating):
        """
        Adds a single edge between user and product.

        Args:
            user (str): User identifier
            product (str): Product identifier
            rating (float): Interaction score
        """
        self.adj[user].append((product, rating))

    def add_edges_batch(self, user_edges):
        """
        Adds multiple edges efficiently in batch.

        Args:
            user_edges (dict): { user_id: [(product_id, rating), ...], ... }
        """
        for user, edges in user_edges.items():
            self.adj[user].extend(edges)

    def get_neighbors(self, user):
        """
        Retrieves all products connected to a user.

        Args:
            user (str): User identifier

        Returns:
            list: List of (product_id, rating) tuples
        """
        return self.adj.get(user, [])