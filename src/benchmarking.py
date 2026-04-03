"""
Benchmarking Module

This script evaluates the performance and scalability of the
OptimizedUserStore module using synthetic large datasets.

Features:
- Measures insertion time for datasets of different sizes
- Measures Top-N retrieval time
- Generates performance graphs (time vs number of users)
- Simulates large-scale recommendation scenarios
"""

import time
import matplotlib.pyplot as plt
from optimized_user_store import OptimizedUserStore
from optimized_graph import OptimizedGraph
from heap_recommender import get_top_n_recommendations
import random

def generate_large_dataset(num_users=1000, num_products=500):
    """
    Generates a synthetic dataset for stress testing.

    Args:
        num_users (int): Number of users to generate
        num_products (int): Number of distinct products

    Returns:
        dict: { user_id: { product_id: rating, ... }, ... }
    """
    dataset = {}
    for u in range(num_users):
        user_id = f"U{u}"
        dataset[user_id] = {}
        # Each user interacts with random number of products
        for _ in range(random.randint(10, 50)):
            product_id = f"P{random.randint(0, num_products-1)}"
            rating = random.uniform(1, 5)  # Random rating between 1 and 5
            dataset[user_id][product_id] = rating
    return dataset

def benchmark_user_store(dataset, top_n=5):
    """
    Benchmarks insertion and Top-N retrieval performance.

    Args:
        dataset (dict): Synthetic user-product rating data
        top_n (int): Number of Top-N recommendations

    Returns:
        tuple: (insertion_time_seconds, top_n_retrieval_time_seconds)
    """
    store = OptimizedUserStore()

    # Measure insertion time
    start = time.time()
    for user, ratings in dataset.items():
        for product, rating in ratings.items():
            store.add_rating(user, product, rating)
    insert_time = time.time() - start

    # Measure Top-N retrieval time for all users
    start = time.time()
    for user in dataset.keys():
        store.get_top_n(user, top_n)
    retrieval_time = time.time() - start

    return insert_time, retrieval_time

def plot_results(sizes, insert_times, retrieval_times):
    """
    Plots benchmark results and saves graph to results folder.

    Args:
        sizes (list): Number of users in each test
        insert_times (list): Time taken to insert users
        retrieval_times (list): Time taken for Top-N retrievals
    """
    plt.figure(figsize=(8,5))
    plt.plot(sizes, insert_times, label="Insertion Time", marker='o')
    plt.plot(sizes, retrieval_times, label="Top-N Retrieval Time", marker='o')
    plt.xlabel("Number of Users")
    plt.ylabel("Time (seconds)")
    plt.title("Optimized UserStore Performance")
    plt.legend()
    plt.grid(True)
    plt.savefig("results/performance_graph.png")
    plt.show()

if __name__ == "__main__":
    user_sizes = [100, 500, 1000, 2000, 5000]
    insert_times = []
    retrieval_times = []

    # Run benchmarks for each dataset size
    for size in user_sizes:
        data = generate_large_dataset(num_users=size)
        ins, ret = benchmark_user_store(data)
        insert_times.append(ins)
        retrieval_times.append(ret)

    # Plot performance graph
    plot_results(user_sizes, insert_times, retrieval_times)