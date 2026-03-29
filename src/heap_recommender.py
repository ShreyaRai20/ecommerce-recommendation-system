"""
Heap Recommender Module

This module uses a min-heap (priority queue) to efficiently
retrieve the Top-N highest scoring products.

Why Heap?
- Avoids sorting entire dataset (O(n log n))
- Maintains Top-N in O(n log k)

Time Complexity:
- O(n log k), where k = number of recommendations
"""

import heapq

def get_top_n_recommendations(scores, n=5):
    """
    Returns the top-N products based on their scores.

    Args:
        scores (dict): Dictionary of product scores
                       Format: { product_id: score }
        n (int): Number of top recommendations

    Returns:
        list: Top-N product IDs sorted by score (descending)
    """

    # Initialize an empty heap (min-heap)
    heap = []

    # Iterate over all product scores
    for product, score in scores.items():

        # If heap is not full, push element
        if len(heap) < n:
            heapq.heappush(heap, (score, product))

        # If heap is full, push new element and pop smallest
        else:
            heapq.heappushpop(heap, (score, product))

    # Sort heap in descending order before returning
    return [product for score, product in sorted(heap, reverse=True)]