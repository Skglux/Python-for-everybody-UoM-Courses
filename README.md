# Python for Everybody - University of Michigan

![Status: In Progress](https://img.shields.io/badge/Status-In_Progress-yellow)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This repository contains my coursework, exercises, and projects for the **Python for Everybody** Specialization offered by the University of Michigan on Coursera.

## 📖 About the Course
The specialization covers the fundamentals of programming using Python, including data structures, networked application program interfaces, and databases. 

* **Instructor:** Charles Severance (Dr. Chuck)
* **Platform:** Coursera

--- 

## 📚 Course Topics 

* **Why we program**: [`c1_basicsyntax.py`](./c1_basicsyntax.py) — A simple script that uses the `print()` function to display text.
* **Variables and Expressions**: [`c2_variables.py`](./c2_variables.py) — Calculates total pay by taking user input for hours and rate, then converting them to floats.
* **Conditional Code**: [`c3_conditions.py`](./c3_conditions.py) — A grading tool that uses conditional logic (`if/elif/else`) to assign a letter grade based on a numeric score.
* **Functions**: [`c4_functions.py`](./c4_functions.py) — Uses a custom function and `try/except` blocks to calculate pay, including overtime rates.
* **Loops and Iteration**: [`c5_loops.py`](./c5_loops.py) — A loop-based program that continuously asks for numbers to identify the largest and smallest values until the user types "done".
* **Strings**: [`c6_strings.py`](./c6_strings.py) — A string parsing program designed to extract and convert a specific numerical value from a string of text.
* **Files**: [`c7.1_files.py`](./c7.1_files.py) — A read file program that transforms its entire content to uppercase.  
  [`  c7.2_files.py`](./c7.2_files.py) — A file program that searches through mail logs to extract, convert, and average spam confidence scores.
* **Lists**: [`c8.4_lists.py`](./c8.4_lists.py) — A program that reads a file and converts its lines in to lists then it takes each word of each list and creates a new list without duplicate words and sorts the list.
[`c8.5_lists.py`](./c8.5_lists.py) — A read file program that searches for lines that start with a specific word then creates a list out of them and prints the second word and total count of lines found.
* **Dictionaries**: [`c9.4_dict.py`](./c9.4_dict.py) — A read file program that searches for sender's email address, creates a dictionary of the senders email and their count and finds the most prolific committer. [`c9.5_dict.py`](./c9.5_dict.py) — A read file program that records that finds the senders email and captures and counts in a dictionary the domain name and finaly prints the domain with most messages send.
* **Tuples**: [`c10.2_tuples.py`](./c10.2_tuples.py) — A script that parses a file with email logs to calculate the distribution of messages by hour.[`c10_wordfrequencyanalyzer.py`](./c10_wordfrequencyanalyzer.py) — A script that parses an ebook file and returns the Top 10 most frequent words, but with these constraints:
Excludes "Stop Words": Ignore common words like the, a, an, in, or, is.
Normalizes: "Python," "python!", and "PYTHON" must count as the same word.
---

## 💡 Key Takeaways
* **Error Handling**: Using `try` and `except` to prevent crashes from invalid user input.
* **Control Flow**: Implementing `while`,`for` loops and `if/elif/else` logic to create interactive programs.
* **Functions**: Designing reusable blocks of code with the `def` keyword to simplify calculations.
* **Data Extraction**: Using string methods like `.find()` and slicing to isolate and convert specific numerical data from complex text lines.
* **File Iteration**: Implementing loops to read through large files line-by-line and filter content using conditional checks like `.startswith()`.
* **Collection Logic**: Utilizing Python lists to store, sort, and manage unique data sets while preventing duplicates with membership operators.
* **Dictionaries manipulation**: Implementing Decorate-Sort-Undecorate pattern to sort dictionairy items.

---

## 🛠️ Technologies & Tools
* **Language:** Python 3 🐍
* **Editor:** VS Code 💻
* **Version Control:** Git & GitHub 🐙

## 🚀 How to Run
To run any of the scripts locally, ensure you have Python installed and execute the following command in your terminal:

```bash
python3 filename.py

