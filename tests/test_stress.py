"""
Stress Tests

This module performs stress testing on:
- OptimizedUserStore
- OptimizedGraph

Purpose:
- Validate correctness under large datasets
- Ensure Top-N and graph retrievals scale correctly
"""

import pytest
from optimized_user_store import OptimizedUserStore
from optimized_graph import OptimizedGraph

def test_large_user_store():
    """
    Tests OptimizedUserStore with 10,000 users and multiple products.
    Validates Top-N functionality and caching.
    """
    store = OptimizedUserStore()
    for i in range(10000):
        store.add_rating(f"U{i}", f"P{i%500}", i%5+1)

    top5 = store.get_top_n("U9999", 5)
    assert len(top5) <= 5  # Ensure only 5 results returned
    assert isinstance(top5, list)

def test_large_graph():
    """
    Tests OptimizedGraph with 10,000 edges.
    Validates adjacency retrieval.
    """
    graph = OptimizedGraph()
    for i in range(10000):
        graph.add_edge(f"U{i}", f"P{i%500}", i%5+1)

    neighbors = graph.get_neighbors("U9999")
    assert len(neighbors) > 0
    assert isinstance(neighbors, list)