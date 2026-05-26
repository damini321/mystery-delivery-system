# Mystery Delivery System

## Overview

This project simulates a logistics delivery system for a fictional company called FastBox.

The system:
- Reads delivery data from JSON files
- Assigns packages to the nearest delivery agent
- Calculates delivery distances using Euclidean distance
- Generates a delivery report
- Saves the final report to `report.json`

---

# Project Structure

```plaintext
PYTHONASSIGNMENT
│
├── main.py
├── README.md
├── base_case.json
├── report.json
│
└── Python Assignment(Delivery System Test Cases)
      ├── test_case_1.json
      ├── test_case_2.json
      ├── test_case_3.json
      └── ...
```

---

# Requirements

- Python 3.x

No external libraries are required.

---

# How to Run

## Step 1

Open terminal in the project folder.

## Step 2

Run the following command:

```bash
python main.py
```

---

# Input

Enter JSON filename when prompted.

Examples:

```plaintext
base_case.json
```

OR

```plaintext
test_case_1.json
```

---

# Features

- JSON file parsing
- Euclidean distance calculation
- Nearest agent assignment
- Delivery simulation
- Efficiency calculation
- Best agent selection
- Automatic report generation

---

# Working Logic

1. Read JSON data
2. Find nearest agent to warehouse
3. Calculate:
   - Agent → Warehouse distance
   - Warehouse → Destination distance
4. Update total distance traveled
5. Update agent location after delivery
6. Generate final report
7. Save report to `report.json`

---

# Output Example

```json
{
    "A1": {
        "packages_delivered": 2,
        "total_distance": 85.32,
        "efficiency": 42.66
    },
    "A2": {
        "packages_delivered": 2,
        "total_distance": 120.12,
        "efficiency": 60.06
    },
    "A3": {
        "packages_delivered": 1,
        "total_distance": 50.00,
        "efficiency": 50.00
    },
    "best_agent": "A1"
}
```

---

# Notes

- The code supports multiple JSON formats
- Supports both dictionary and list-based structures
- Automatically creates `report.json`

---

# Assumptions

- The nearest available agent is selected based on Euclidean distance from the warehouse.
- After completing a delivery, the agent’s current location is updated to the package destination.
- Lower efficiency value is considered better because it represents less distance traveled per package.
- If multiple agents are at the same distance, the first encountered agent is selected.
- The system supports both dictionary-based and list-based JSON structures for warehouses and agents.
- The system supports both `warehouse` and `warehouse_id` keys in package data.

# Author

Damini Khule