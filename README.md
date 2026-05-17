# 🐍 Python Tutorial

> **Hands-on collection of Python examples** covering core language features, OOP, design patterns, API testing, data validation, multithreading, and common interview questions.

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![jsonschema](https://img.shields.io/badge/jsonschema-4.x-green)](https://python-jsonschema.readthedocs.io/)
[![pydantic](https://img.shields.io/badge/pydantic-v2-red)](https://docs.pydantic.dev/)
[![pytest](https://img.shields.io/badge/pytest-9.x-orange?logo=pytest)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running an Example](#running-an-example)
- [Module Documentation](#module-documentation)
  - [api\_testing](#api_testing)
  - [design\_pattern](#design_pattern)
  - [interview\_questions](#interview_questions)
  - [lambda\_function](#lambda_function)
  - [oops](#oops)
  - [pydantic](#pydantic)
  - [schema\_validation](#schema_validation)
  - [solid\_principles](#solid_principles)
  - [tenacity](#tenacity)
  - [threads](#threads)
- [Contributing](#contributing)

---

## Overview

This repository is a structured Python learning resource. Every module is self-contained and runnable. It covers:

| Capability | Description |
|---|---|
| 🌐 **API Testing** | All major HTTP methods using `requests` against a live REST API |
| 🏗️ **Design Patterns** | Singleton and other classic patterns |
| 💼 **Interview Questions** | 25+ common Python coding problems with clean solutions |
| ⚡ **Lambda Functions** | Anonymous one-liner functions with practical examples |
| 🧱 **OOP** | Encapsulation, inheritance, overloading, overriding, abstraction |
| ✅ **Pydantic** | Data validation & serialization with Pydantic v2 |
| 📐 **Schema Validation** | JSON schema validation using `jsonschema` |
| 🏛️ **SOLID Principles** | Open/Closed and other SOLID principle implementations |
| 🔄 **Tenacity** | Automatic retry logic with `stop_after_attempt` & `wait_fixed` |
| 🧵 **Threads** | Multithreading via functions and subclassing `Thread` |

---

## Tech Stack

| Library | Version | Purpose |
|---|---|---|
| Python | 3.13 | Programming language |
| requests | 2.x | HTTP client for API testing |
| jsonschema | 4.x | JSON schema validation |
| pydantic | v2 | Data validation & serialization |
| tenacity | latest | Retry logic |
| pytest | 9.x | Testing framework |
| Faker | latest | Fake data generation |
| PyYAML | latest | YAML parsing |
| selenium | latest | Browser automation |

---

## Project Structure

```
PythonTutorial/
│
├── api_testing/                    # REST API testing with requests
│   ├── get_call.py                 # GET request with assertions
│   ├── post_call.py                # POST request — create a resource
│   ├── put_call.py                 # PUT request — full update
│   ├── patch_call.py               # PATCH request — partial update
│   ├── delete_call.py              # DELETE request
│   └── schema_validation.py        # Validate API response schema
│
├── design_pattern/
│   └── single_pattern/
│       └── single_pattern.py       # Singleton pattern implementation
│
├── interview_questions/            # 25+ Python coding problem solutions
│
├── lambda_function/
│   └── lambda_function.py          # Lambda syntax & practical examples
│
├── oops/                           # Object-Oriented Programming concepts
│   ├── abstraction.py
│   ├── encapsulation.py
│   ├── inheritance.py
│   ├── overloading.py
│   └── overriding.py
│
├── pydantic/                       # Data validation with Pydantic v2
│   ├── user.py
│   ├── product.py
│   ├── studnet.py
│   └── api_validation.py
│
├── schema_validation/
│   └── schema_vlaidation.py        # JSON schema validation with jsonschema
│
├── solid_principles/
│   └── open_closed_principle/      # Open/Closed principle via Shape ABC
│
├── tenacity/
│   └── demo.py                     # Retry logic demo
│
├── threads/                        # Multithreading examples
│   ├── mainthread.py
│   ├── using_function.py
│   └── usingsubclass.py
│
├── requirements.txt
└── README.md
```

---

## Prerequisites

Ensure the following are installed before proceeding:

- ✅ [Python 3.10+](https://www.python.org/downloads/) (3.13 recommended)
- ✅ [pip](https://pip.pypa.io/en/stable/)
- ✅ [Git](https://git-scm.com/)
- ✅ [PyCharm](https://www.jetbrains.com/pycharm/) or any Python IDE (optional, recommended)

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/PythonTutorial.git
cd PythonTutorial
```

### 2. Create & Activate Virtual Environment

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running an Example

Each file is self-contained and can be executed directly:

```bash
python api_testing/get_call.py
python interview_questions/palindrome.py
python lambda_function/lambda_function.py
```

---

## Module Documentation

### `api_testing`

Demonstrates all major HTTP methods using the [`requests`](https://docs.python-requests.org/) library against the [ReqRes](https://reqres.in/) API.

| File | Description |
|---|---|
| `get_call.py` | GET request with status code & body assertions |
| `post_call.py` | POST request — create a new resource |
| `put_call.py` | PUT request — full update of a resource |
| `patch_call.py` | PATCH request — partial update |
| `delete_call.py` | DELETE request |
| `schema_validation.py` | Validate API response against a JSON schema |

---

### `design_pattern`

| Pattern | File | Description |
|---|---|---|
| Singleton | `single_pattern/single_pattern.py` | Ensures only one instance of a class exists |

---

### `interview_questions`

Solutions to frequently asked Python coding problems, each with clear examples.

| File | Topic |
|---|---|
| `palindrome.py` | Palindrome check (slicing & two-pointer) |
| `reverse_string.py` | Reverse a string |
| `reversing_individual_words.py` | Reverse each word in a sentence |
| `second_largest.py` | Find the second largest element |
| `largest_element_in_list.py` | Find the largest element in a list |
| `two_numbers_sum_up_to_target.py` | Two-sum problem |
| `remove_duplicates.py` | Remove duplicates from a list |
| `common_elements.py` | Find common elements between lists |
| `frequency_of_each_element.py` | Count element frequency |
| `move_all_zeroes_to_end.py` | Move all zeroes to end of list |
| `closest_number.py` | Find the closest number to a target |
| `sort_a_list_using_inbuilt_function.py` | Sort using built-in functions |
| `sort_a_list_without_inbuilt_function.py` | Sort without built-in functions |
| `sort_shortname_to_longname.py` | Sort strings by length |
| `swap_numbers.py` | Swap two numbers |
| `decorator.py` | Decorators & execution-time logging |
| `list_comprehension.py` | List comprehension examples |
| `exceptions.py` | Exception handling |
| `namespace.py` | Python namespaces & scope |
| `nested_dictionary.py` | Working with nested dictionaries |
| `straight_staircase.py` | Print a straight staircase pattern |
| `reverse_staircase.py` | Print a reverse staircase pattern |
| `centered_staircase.py` | Print a centered staircase pattern |
| `reverse_keeping_count_of_char.py` | Reverse while tracking character count |
| `guess_output.py` | Tricky "guess the output" snippets |
| `list_output.py` | List behavior & output questions |

---

### `lambda_function`

Anonymous one-liner functions using Python's `lambda` keyword.

**Syntax:**
```python
lambda arguments: expression
```

| File | Description |
|---|---|
| `lambda_function.py` | Add, multiply, uppercase, and conditional examples |

---

### `oops`

| File | Concept |
|---|---|
| `encapsulation.py` | Public, protected & private access (BankAccount demo) |
| `inheritance.py` | Parent/Child classes, `super()`, method overriding |
| `overloading.py` | Method overloading via `*args` |
| `overriding.py` | Method overriding in subclasses |
| `abstraction.py` | Abstract base classes using `ABC` and `@abstractmethod` |

---

### `pydantic`

Data validation and serialization using [Pydantic v2](https://docs.pydantic.dev/).

| File | Description |
|---|---|
| `user.py` | Basic model with type validation |
| `product.py` | Optional fields, `model_dump()`, JSON schema |
| `studnet.py` | Field constraints, `EmailStr`, `AnyUrl` validation |
| `api_validation.py` | Nested models for API request validation |

---

### `schema_validation`

| File | Description |
|---|---|
| `schema_vlaidation.py` | Validate JSON data against a schema using `jsonschema` |

**Key concepts:**

| Keyword | Purpose |
|---|---|
| `type` | Expected data type (`object`, `string`, `integer`, `array`) |
| `properties` | Expected fields and their types inside an object |
| `required` | Fields that MUST be present in the data |

> If validation passes → no exception is raised. If it fails → a `ValidationError` is raised with details.

---

### `solid_principles`

| Principle | Folder | Description |
|---|---|---|
| Open/Closed | `open_closed_principle/` | Extend behavior via `Shape` ABC without modifying existing code |

---

### `tenacity`

| File | Description |
|---|---|
| `demo.py` | Automatic retries with `stop_after_attempt` & `wait_fixed` |

---

### `threads`

| File | Description |
|---|---|
| `mainthread.py` | Identify the main thread |
| `using_function.py` | Create a thread from a plain function |
| `usingsubclass.py` | Create a thread by subclassing `Thread` |

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "feat: add your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

### Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Usage |
|---|---|
| `feat:` | New feature or script |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `refactor:` | Code refactor without behaviour change |
| `test:` | Adding or updating tests |
| `chore:` | Maintenance tasks (deps, config) |

---

## 📄 License

This project is open source and available for educational purposes under the [MIT License](LICENSE).

---

> **Maintained by:** Python Learners  
> **Last Updated:** May 2026
