

# 🐍 Python Mini Projects — Assignment Book (2025–2026)

A collection of 5 beginner-to-intermediate Python console applications built using only Python fundamentals (no external libraries). Each project simulates a real-world use case and covers core Python concepts.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Project 1 — Student Management System](#project-1--student-management-system)
- [Project 2 — Library Management System](#project-2--library-management-system)
- [Project 3 — Personal Expense Tracker](#project-3--personal-expense-tracker)
- [Project 4 — Quiz & Examination System](#project-4--quiz--examination-system)
- [Project 5 — Inventory Management System](#project-5--inventory-management-system)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)
- [Grade Scale](#grade-scale)

---

## Project Overview

| # | Project | Difficulty | File | Key Concepts |
|---|---------|------------|------|--------------|
| 1 | Student Management System | Easy | `student_management.py` | Dict, List, Functions |
| 2 | Library Management System | Easy–Moderate | `library_management.py` | Nested Dict, Loops |
| 3 | Personal Expense Tracker | Moderate | `expense_tracker.py` | Dict, Sets, Arithmetic |
| 4 | Quiz & Examination System | Moderate | `quiz_system.py` | Tuples, String Ops |
| 5 | Inventory Management System | Moderate–Advanced | `inventory_management.py` | File Handling, Sets |

---

## Project 1 — Student Management System

A console-based CRUD application to manage student records including name, roll number, marks, and grades.

### Features
- Add, view, search, update, and delete student records
- Auto-calculates percentage and grade from 5 subject marks
- Duplicate roll number prevention
- Input validation using `try-except`
- Clean formatted table output

### Concepts Used
`Variables` · `Lists & Dictionaries` · `Conditional Statements` · `Loops` · `Functions` · `Exception Handling`

### Sample Output
```
====== STUDENT MANAGEMENT SYSTEM ======
1. Add Student    2. View All
3. Search         4. Update
5. Delete         6. Exit

Enter choice: 1
Enter Name    : Rahul Sharma
Enter Roll No : 101
Marks (Sub 1-5): 78 85 90 72 88
=== Record Added Successfully ===
Name: Rahul Sharma | Roll: 101 | %: 82.60 | Grade: B+
```

### Functions
| Function | Description |
|----------|-------------|
| `add_student()` | Collects and validates student data |
| `view_all()` | Displays all records in formatted output |
| `search_student()` | Finds a student by roll number |
| `update_student()` | Updates specific fields of a record |
| `delete_student()` | Removes a student entry |
| `calculate_grade()` | Returns grade based on percentage |
| `show_menu()` | Displays menu and returns user choice |

---

## Project 2 — Library Management System

Tracks books, handles issue/return operations, records borrowers, and generates availability reports.

### Features
- Register books with unique ISBN
- Issue and return books with state tracking (Available / Issued)
- Multi-field search by title or author
- Due date calculation (7 days from issue)
- Borrower history tracking

### Concepts Used
`Nested Dictionaries` · `While Loops` · `String Operations` · `Exception Handling` · `State Management`

### Sample Output
```
====== LIBRARY MANAGEMENT SYSTEM ======
1. Add Book     2. Issue Book
3. Return Book  4. Search Book
5. View All     6. Exit

Enter choice: 2
Enter ISBN       : 978-3-16-148410-0
Enter Borrower ID: STU2024-07
Enter Your Name  : Priya Desai
Book Issued Successfully!
Title   : Python Programming
Due Date: 28-June-2026
```

### Functions
| Function | Description |
|----------|-------------|
| `add_book()` | Register a new book |
| `issue_book()` | Issue a book to a student |
| `return_book()` | Process book return |
| `search_book()` | Search by title or author |
| `view_catalog()` | Display full library catalog |
| `check_due_date()` | Calculate due date from issue date |

---

## Project 3 — Personal Expense Tracker

Tracks daily expenses by category, compares spending against a monthly budget, and generates reports with warnings.

### Features
- Add expenses with description, category, amount, and date
- Category-wise expense summary
- Budget report with percentage used
- Warning alerts at 80% and 100% budget usage
- Identifies top spending category

### Concepts Used
`Lists of Dictionaries` · `Arithmetic Operators` · `f-strings` · `Sets` · `For Loops` · `Functions`

### Sample Output
```
===== PERSONAL EXPENSE TRACKER =====
Monthly Budget: Rs. 5000.00
1.Add  2.View  3.Category  4.Report  5.Exit

Choice: 4
========= BUDGET REPORT =========
Total Spent  : Rs. 4200.00
Budget Limit : Rs. 5000.00
Remaining    : Rs. 800.00
Used         : 84.00%
⚠ WARNING: You have used 84% of your budget!
Top Category : Food (Rs. 1800.00)
```

### Functions
| Function | Description |
|----------|-------------|
| `add_expense()` | Collects and validates expense entry |
| `view_expenses()` | Prints all entries in table format |
| `category_summary()` | Groups and totals by category |
| `budget_report()` | Compares spending against budget |
| `get_top_category()` | Returns highest spending category |
| `validate_amount()` | Ensures positive float input |

---

## Project 4 — Quiz & Examination System

An interactive MCQ quiz that evaluates answers, tracks scores, and generates a detailed result report with wrong-answer review.

### Features
- Question bank stored as tuples (immutable, for data integrity)
- 10+ multiple-choice questions (A / B / C / D)
- Real-time correct/incorrect feedback
- Final result report with score, percentage, grade, and pass/fail verdict
- Wrong-answer review at the end

### Concepts Used
`Tuples` · `Lists` · `Dictionaries` · `String Operations` · `For Loops` · `Exception Handling`

### Sample Output
```
===== PYTHON QUIZ SYSTEM =====
Student: Anjali Patil | Roll: 204

Q1: Which data type is IMMUTABLE in Python?
  A. List        B. Dictionary
  C. Tuple       D. Set
Your Answer: C
✓ Correct!

====== RESULT REPORT ======
Name    : Anjali Patil
Score   : 8 / 10
Percent : 80.00%
Grade   : B+
Result  : PASS
```

### Functions
| Function | Description |
|----------|-------------|
| `load_questions()` | Returns the question bank (list of tuples) |
| `display_question()` | Displays a question with options |
| `get_answer()` | Accepts and validates student answer |
| `evaluate_quiz()` | Scores all answers and compiles result |
| `calculate_grade()` | Returns grade from percentage |
| `show_report()` | Prints final formatted result report |
| `show_wrong_answers()` | Displays incorrectly answered questions |

---

## Project 5 — Inventory Management System

A comprehensive stock-control application with file persistence that tracks products, handles stock transactions, triggers low-stock alerts, and generates inventory reports.

### Features
- Full product CRUD with unique Product ID (P001, P002, ...)
- Stock-in (restock) and stock-out (sales) with validation
- Low-stock alerts when quantity falls below reorder level
- Transaction log with timestamps
- Total inventory valuation report
- Category tracking using sets
- **File persistence** — loads from `inventory.txt` on startup, saves on exit

### Concepts Used
`Dictionaries` · `Lists` · `Sets` · `Tuples` · `File Handling` · `Exception Handling` · `String Formatting`

### Sample Output
```
===== INVENTORY MANAGEMENT SYSTEM =====
Products Loaded: 12 | Categories: 4
1.Add  2.Stock-In  3.Stock-Out
4.View 5.Alert     6.Report  7.Exit

Choice: 6
======= INVENTORY REPORT =======
Total Products   : 12
Total Stock Value: Rs. 1,24,500.00
Categories       : Electronics, FMCG, Apparel, Stationery
Low Stock Items  : 3 (below reorder level)
Highest Value Item: Laptop (Rs. 58,000 x 2 = Rs. 1,16,000)
```

### Functions
| Function | Description |
|----------|-------------|
| `load_inventory()` | Read data from `inventory.txt` |
| `save_inventory()` | Write data to `inventory.txt` |
| `add_product()` | Register new product |
| `stock_in()` | Add quantity to existing product |
| `stock_out()` | Deduct quantity with validation |
| `view_inventory()` | Display full formatted table |
| `low_stock_alert()` | List products below reorder level |
| `generate_report()` | Summary statistics and analytics |
| `log_transaction()` | Append entry to transaction history |
| `get_total_value()` | Returns total inventory valuation |

---

## Tech Stack

- **Language:** Python 3.x
- **Libraries:** None (pure Python only)
- **Tools:** VS Code / PyCharm / IDLE / Jupyter Notebook

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/python-mini-projects.git
   cd python-mini-projects
   ```

2. Run any project:
   ```bash
   python student_management.py
   python library_management.py
   python expense_tracker.py
   python quiz_system.py
   python inventory_management.py
   ```

> Requires Python 3.x. No additional installations needed.

---

## Grade Scale

| Grade | Percentage | Description |
|-------|------------|-------------|
| O | 90–100% | Outstanding |
| A+ | 80–89% | Excellent |
| A | 70–79% | Very Good |
| B+ | 60–69% | Good |
| B | 50–59% | Average |
| F | < 50% | Fail |

---

> **Note:** All code is original work submitted as part of the Python Programming Assignment (2025–2026). Plagiarism is strictly prohibited per academic integrity policy.