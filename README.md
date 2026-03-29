# E-commerce Recommendation System (Proof of Concept)

## Overview

This project implements a **Proof of Concept (PoC)** for an e-commerce recommendation system using fundamental data structures in Python.

The system demonstrates how efficient data structures can be used to:

- Store user-product interactions
- Model relationships
- Generate Top-N recommendations

---

## Data Structures Used

| Data Structure             | Purpose                                  |
| -------------------------- | ---------------------------------------- |
| Hash Tables (Dictionaries) | Store user data and ratings              |
| Graphs                     | Model user-product relationships         |
| Heaps (Priority Queue)     | Generate Top-N recommendations           |
| Sparse Matrix              | Efficient storage of sparse interactions |

---

## ⚙️ Features

- Add users and product ratings
- Represent relationships using graphs
- Generate Top-N recommendations
- Memory-efficient sparse storage
- Modular and scalable design

---

## Project Structure

```
ecommerce-recommendation-system/
│
├── src/
│   ├── user_store.py
│   ├── graph.py
│   ├── heap_recommender.py
│   ├── sparse_matrix.py
│   └── main.py
│
├── tests/
│   └── test_recommender.py
│
├── README.md
└── requirements.txt
```

---

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-recommendation-system.git
cd ecommerce-recommendation-system
```

### 2. Run Application

```bash
cd src
python main.py
```

---

## Run Tests

```bash
pytest
```

---

## Example Output

```
Top Recommendations: ['P4', 'P3']
```

---

## Limitations

- Uses dummy recommendation scores (no ML yet)
- Not optimized for large-scale datasets
- Basic sparse matrix implementation

---

## Future Improvements

- Implement collaborative filtering
- Add machine learning models
- Optimize for scalability
- Use real-world datasets
- Integrate APIs for real-time recommendations

---

## 👩Author

**Shreya Rai**
**Course Number: MSCS-532-B01**

---

## References

- Aggarwal, C. C. (2016). Recommender Systems
- Koren et al. (2009). Matrix Factorization
- He et al. (2017). Neural Collaborative Filtering

---
