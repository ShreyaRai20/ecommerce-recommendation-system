"""
Sparse Matrix Module

This module simulates a sparse matrix using a dictionary.
Only non-zero values (user-product interactions) are stored.

Why Sparse?
- Efficient memory usage
- Avoids storing large empty matrices

Time Complexity:
- Insert: O(1)
- Retrieve: O(1)
"""

class SparseMatrix:
    def __init__(self):
        # Dictionary to store only non-zero entries
        # Format: { (user, product): rating }
        self.matrix = {}

    def add_value(self, user, product, rating):
        """
        Adds a value to the sparse matrix.

        Args:
            user (str): User identifier
            product (str): Product identifier
            rating (float/int): Interaction value
        """
        self.matrix[(user, product)] = rating

    def get_value(self, user, product):
        """
        Retrieves a value from the sparse matrix.

        Args:
            user (str): User identifier
            product (str): Product identifier

        Returns:
            rating if exists, else 0
        """
        return self.matrix.get((user, product), 0)