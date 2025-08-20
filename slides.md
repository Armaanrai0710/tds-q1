---
marp: true
title: Product Documentation Presentation
author: 24ds2000041@ds.study.iitm.ac.in
theme: default
paginate: true
---

<!-- _class: lead -->

# Product Documentation Presentation

Prepared by: **24ds2000041@ds.study.iitm.ac.in**

---

<!-- _backgroundImage: url('images/bg.jpg') -->
<!-- _backgroundSize: cover -->

# Background Image Slide

This slide uses a full background image.

---

# Algorithmic Complexity

We analyze runtime:

$$
T(n) = O(n \log n)
$$

---

# Code Example

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)
