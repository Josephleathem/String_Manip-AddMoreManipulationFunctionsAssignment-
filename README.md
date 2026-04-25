# Week 5 - Hands On Exercise 10
School - Course: California Institute of Applied Technology - Course ASD264-21: Coding with AI

## Course Objectives
CO8 - Use Copilot to create and run unit tests for Python and JavaScript, applying TDD principles and the red-green-refactor workflow to improve code quality and reliability.

**Estimated time to Complete:** 1 hour

## Description
Students will use test-driven development to add more string manipulation functions to the `string_manip.py` file in the `ch07/pytest/string_manip` folder.

## Required Resources
- VS Code
- `string_manip.py` file in the `ch07/pytest/string_manip` folder: Files > Student Files > Course Files > ch07 > pytest > string_manip

## Deliverable
### Assignment Submission
For each program, attach the two required files to your submission.

- Copy/paste your code and output screenshots into an MS Word file.
- Your source code `.py` file.

Notes for the difference between the two files:

- "Your source code" refers to the actual code files, such as `.py` files, not just screenshots.
- The source code allows instructors to evaluate their logic, structure, and syntax and test it themselves.
- A screenshot only shows a static result that the student tested, but instructors can't run, verify, or review the full code/script if it's long.

## What I Did

Following the TDD red-green-refactor workflow, I added 4 new string manipulation functions to `string_manip.py` along with 23 new tests in `test_string_manip.py`.

### Red Phase
I wrote 23 new failing tests in `test_string_manip.py` for four functions that did not yet exist:

- `reverse_string` — returns a string reversed
- `count_vowels` — counts vowels (a, e, i, o, u) case-insensitively
- `is_palindrome` — checks if a string reads the same forwards and backwards, ignoring case and spaces
- `truncate` — clips a string to a maximum length and appends `...` if it was shortened

Each function had tests covering normal behavior, edge cases (empty strings, exact length), and invalid input (`TypeError` and `ValueError`). Running pytest at this stage showed all 23 new tests failing.

### Green Phase
I implemented all four functions in `string_manip.py` with proper input validation. Running pytest again showed all 30 tests passing (the original 7 plus the 23 new ones).

### Results
```
30 passed in 0.14s
```
Open and access VS Code.

## Lab Steps
### Instructions
Use test-driven development to add more string manipulation functions to the `string_manip.py` file in the `ch07/pytest/string_manip` folder (Files > Student Files > Course Files > ch07 > pytest > string_manip).

Then, for each program, attach the two required files to your submission:

- Copy/paste your code and output screenshots into an MS Word file.
- Your source code `.py` file.

Notes for the difference between the two files:

- "Your source code" refers to the actual code files, such as `.py` files, not just screenshots.
- The source code allows instructors to evaluate their logic, structure, and syntax and test it themselves.
- A screenshot only shows a static result that the student tested, but instructors can't run, verify, or review the full code/script if it's long.
