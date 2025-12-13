#!/usr/bin/env python3
"""
Generate interactive HTML tutorials for problems 2-6 and 8
Based on the structure of problems 1 and 7
"""

import json

# Problem configurations
problems = {
    2: {
        "title": "2D Array DS - Hourglass Sum",
        "problem_url": "https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true",
        "filename": "2_2d_array_ds.html",
        "steps": 16,
        "phases": ["Understanding 2D Arrays", "The Hourglass Pattern", "The Algorithm", "The Code", "Mastery"]
    },
    3: {
        "title": "Dynamic Array",
        "problem_url": "https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=true",
        "filename": "3_dynamic_array.html",
        "steps": 17,
        "phases": ["Understanding Arrays", "XOR Operations", "The Algorithm", "The Code", "Mastery"]
    },
    4: {
        "title": "Left Rotation",
        "problem_url": "https://www.hackerrank.com/challenges/array-left-rotation/problem?isFullScreen=true",
        "filename": "4_left_rotation.html",
        "steps": 15,
        "phases": ["Understanding Rotation", "Approach 1: Slicing", "Approach 2: Iterative", "The Code", "Mastery"]
    },
    5: {
        "title": "Sparse Arrays",
        "problem_url": "https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true",
        "filename": "5_sparse_arrays.html",
        "steps": 16,
        "phases": ["Understanding Frequency", "Brute Force", "Hash Map Optimization", "The Code", "Mastery"]
    },
    6: {
        "title": "Print Elements of Linked List",
        "problem_url": "https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem?isFullScreen=true",
        "filename": "6_print_elements_of_linked_list.html",
        "steps": 14,
        "phases": ["Understanding Linked Lists", "Traversal Basics", "The Algorithm", "The Code", "Mastery"]
    },
    8: {
        "title": "Insert Node at Head",
        "problem_url": "https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem?isFullScreen=true",
        "filename": "8_insert_node_at_head.html",
        "steps": 15,
        "phases": ["Understanding Head Insertion", "The Challenge", "The Algorithm", "The Code", "Mastery"]
    }
}

print("HTML tutorial generator ready")
print(f"Will create tutorials for problems: {list(problems.keys())}")
