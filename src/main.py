"""
Main Module - Deliverable 2 & Deliverable 3

This script demonstrates:
1. Phase 2: Proof-of-Concept (Deliverable 2)
2. Phase 3: Optimization, Scaling, and Performance Evaluation (Deliverable 3)

Modules:
- D2:
    user_store.py
    graph.py
    heap_recommender.py
- D3:
    optimized_user_store.py
    optimized_graph.py
    heap_recommender.py
"""

import time
import random
import os
import matplotlib.pyplot as plt

# Ensure results folder exists
os.makedirs("results", exist_ok=True)

# -----------------------------
# PHASE 2 - DELIVERABLE 2
# -----------------------------
print("=== PHASE 2: Proof-of-Concept (Deliverable 2) ===")
from src.user_store import UserStore          # Deliverable 2 user storage
from src.graph import Graph                    # Deliverable 2 graph
from src.heap_recommender import get_top_n_recommendations  # Shared heap module

# Initialize data structures (D2)
users_d2 = UserStore()
graph_d2 = Graph()

# Measure D2 execution time
start_time_d2 = time.time()

# Step 1: Add user interactions
users_d2.add_rating("U1", "P1", 5)
users_d2.add_rating("U1", "P2", 3)

# Step 2: Build graph edges
graph_d2.add_edge("U1", "P1", 5)
graph_d2.add_edge("U1", "P2", 3)

# Step 3: Simulate recommendation scores
scores_d2 = {"P3": 4.5, "P4": 4.7, "P5": 4.2}

# Step 4: Get Top-N recommendations
recommendations_d2 = get_top_n_recommendations(scores_d2, 2)

end_time_d2 = time.time()

print("Top Recommendations (D2 PoC):", recommendations_d2)
print(f"D2 Execution Time: {end_time_d2 - start_time_d2:.6f}s")

# -----------------------------
# Deliverable 2 Graph
# -----------------------------
plt.figure(figsize=(6,4))
plt.bar(["Add+Graph+TopN"], [end_time_d2 - start_time_d2], color='skyblue')
plt.title("Deliverable 2: PoC Execution Time")
plt.ylabel("Time (seconds)")
plt.grid(axis='y')

# Save graph
plt.savefig("results/d2_execution_time.png")
plt.close()  # Close figure to avoid overlap with D3 plots

# -----------------------------
# PHASE 3 - DELIVERABLE 3
# -----------------------------
print("\n=== PHASE 3: Optimization & Performance Evaluation (Deliverable 3) ===")
from src.optimized_user_store import OptimizedUserStore  # D3 optimized user store
from src.optimized_graph import OptimizedGraph            # D3 optimized graph

# Function: Generate synthetic dataset for testing
def generate_data(num_users=1000, num_products=500):
    """
    Generates random user-product interactions.
    Returns a list of tuples: (user_id, product_id, rating)
    """
    data = []
    for u in range(1, num_users + 1):
        user_id = f"U{u}"
        num_ratings = random.randint(5, 20)  # Each user rates 5-20 products
        for _ in range(num_ratings):
            product_id = f"P{random.randint(1, num_products)}"
            rating = round(random.uniform(1, 5), 1)
            data.append((user_id, product_id, rating))
    return data

# Function: Benchmark optimized structures
def benchmark(data, top_n=5):
    """
    Inserts data into optimized structures and measures:
    - Insertion time
    - Top-N recommendation generation time
    """
    users = OptimizedUserStore()
    graph = OptimizedGraph()

    # Measure insertion time
    start_insert = time.time()
    for user_id, product_id, rating in data:
        users.add_rating(user_id, product_id, rating)
        graph.add_edge(user_id, product_id, rating)
    insert_time = time.time() - start_insert

    # Simulate recommendation scores per user
    scores = {f"P{i}": random.uniform(1, 5) for i in range(1, 101)}

    # Measure Top-N recommendation time
    start_topn = time.time()
    top_products = get_top_n_recommendations(scores, top_n)
    topn_time = time.time() - start_topn

    return insert_time, topn_time

# Dataset sizes for testing scalability
dataset_sizes = [1000, 5000, 10000, 50000]
insert_times = []
topn_times = []

for size in dataset_sizes:
    print(f"\nDataset size: {size}")
    data = generate_data(num_users=size//5, num_products=1000)
    insert_time, topn_time = benchmark(data)
    print(f"Insertion Time: {insert_time:.4f}s, Top-N Time: {topn_time:.4f}s")
    insert_times.append(insert_time)
    topn_times.append(topn_time)

# Plot performance graph
plt.figure(figsize=(8,5))
plt.plot(dataset_sizes, insert_times, marker='o', label="Insertion Time")
plt.plot(dataset_sizes, topn_times, marker='s', label="Top-N Recommendation Time")
plt.title("Deliverable 3: Optimized Recommendation System Performance")
plt.xlabel("Dataset Size (Number of Users)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)

# Save graph
plt.savefig("results/performance_graph.png")
plt.show()