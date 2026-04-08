# 🐍 Python Tutorial

A hands-on collection of Python examples covering core concepts, OOP, design patterns, API testing, data validation, multithreading, and common interview questions.

---

## 📁 Project Structure

```
PythonTutorial/
├── api_testing/             # REST API testing with requests
├── design_pattern/          # Classic design patterns
├── interview_questions/     # Common Python interview problems
├── oops/                    # Object-Oriented Programming concepts
├── pydantic/                # Data validation with Pydantic
├── schema_validation/       # JSON schema validation
├── solid_principles/        # SOLID design principles
├── tenacity/                # Retry logic with Tenacity
├── threads/                 # Multithreading examples
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/PythonTutorial.git
cd PythonTutorial

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

### Running an Example

Each file is self-contained and can be executed directly:

```bash
python api_testing/get_call.py
python interview_questions/palindrome.py
```

---

## 📦 Modules

### 🌐 API Testing (`api_testing/`)

Demonstrates all major HTTP methods using the [`requests`](https://docs.python-requests.org/) library against the [ReqRes](https://reqres.in/) API.

| File                  | Description                                |
|-----------------------|--------------------------------------------|
| `get_call.py`         | GET request with assertions                |
| `post_call.py`        | POST request — create a resource           |
| `put_call.py`         | PUT request — full update of a resource    |
| `patch_call.py`       | PATCH request — partial update             |
| `delete_call.py`      | DELETE request                             |
| `schema_validation.py`| Validate API response against a JSON schema|

### 🏗️ Design Patterns (`design_pattern/`)

| Pattern   | File                                  | Description                                |
|-----------|---------------------------------------|--------------------------------------------|
| Singleton | `single_pattern/single_pattern.py`    | Ensures only one instance of a class exists|

### 💼 Interview Questions (`interview_questions/`)

Solutions to frequently asked Python coding problems, each with clear examples.

| File                              | Topic                                       |
|-----------------------------------|---------------------------------------------|
| `palindrome.py`                   | Palindrome check (slicing & two-pointer)    |
| `reverse_string.py`              | Reverse a string                            |
| `reversing_individual_words.py`  | Reverse each word in a sentence             |
| `second_largest.py`              | Find the second largest element             |
| `largest_element_in_list.py`     | Find the largest element in a list          |
| `two_numbers_sum_up_to_target.py`| Two-sum problem                             |
| `remove_duplicates.py`           | Remove duplicates from a list               |
| `common_elements.py`            | Find common elements between lists          |
| `frequency_of_each_element.py`  | Count element frequency                     |
| `move_all_zeroes_to_end.py`     | Move all zeroes to end of list              |
| `closest_number.py`             | Find the closest number to a target         |
| `sort_a_list_using_inbuilt_function.py` | Sort using built-in functions        |
| `sort_a_list_without_inbuilt_function.py`| Sort without built-in functions     |
| `sort_shortname_to_longname.py` | Sort strings by length                      |
| `swap_numbers.py`               | Swap two numbers                            |
| `decorator.py`                   | Decorators & execution-time logging         |
| `list_comprehension.py`         | List comprehension examples                 |
| `exceptions.py`                  | Exception handling                          |
| `namespace.py`                   | Python namespaces & scope                   |
| `nested_dictionary.py`          | Working with nested dictionaries            |
| `straight_staircase.py`         | Print a straight staircase pattern          |
| `reverse_staircase.py`          | Print a reverse staircase pattern           |
| `centered_staircase.py`         | Print a centered staircase pattern          |
| `reverse_keeping_count_of_char.py`| Reverse while tracking character count    |
| `guess_output.py`               | Tricky "guess the output" snippets          |
| `list_output.py`                | List behavior & output questions            |

### 🧱 OOP Concepts (`oops/`)

| File               | Concept                                              |
|--------------------|------------------------------------------------------|
| `encapsulation.py` | Public, protected & private access (BankAccount)     |
| `inheritance.py`   | Parent/Child classes, `super()`, method overriding   |
| `overloading.py`   | Method overloading via `*args`                       |

### ✅ Pydantic (`pydantic/`)

Data validation and serialization using [Pydantic v2](https://docs.pydantic.dev/).

| File                | Description                                         |
|---------------------|-----------------------------------------------------|
| `user.py`           | Basic model with type validation                    |
| `product.py`        | Optional fields, `model_dump()`, JSON schema        |
| `studnet.py`        | Field constraints, `EmailStr`, `AnyUrl` validation  |
| `api_validation.py` | Nested models for API request validation            |

### 📐 Schema Validation (`schema_validation/`)

| File                    | Description                                    |
|-------------------------|------------------------------------------------|
| `schema_vlaidation.py`  | Validate JSON data with `jsonschema`           |

### 🏛️ SOLID Principles (`solid_principles/`)

| Principle           | Files                                     | Description                                |
|---------------------|-------------------------------------------|--------------------------------------------|
| Open/Closed         | `open_closed_principle/`                  | Extend behavior via `Shape` ABC without modifying existing code |

### 🔄 Tenacity (`tenacity/`)

| File      | Description                                          |
|-----------|------------------------------------------------------|
| `demo.py` | Automatic retries with `stop_after_attempt` & `wait_fixed` |

### 🧵 Threads (`threads/`)

| File                | Description                                |
|---------------------|--------------------------------------------|
| `mainthread.py`     | Identify the main thread                   |
| `using_function.py` | Create a thread from a function            |
| `usingsubclass.py`  | Create a thread by subclassing `Thread`    |

---

## 🛠️ Tech Stack

| Library        | Purpose                          |
|----------------|----------------------------------|
| `requests`     | HTTP client for API testing      |
| `jsonschema`   | JSON schema validation           |
| `pydantic`     | Data validation & serialization  |
| `tenacity`     | Retry logic                      |
| `pytest`       | Testing framework                |
| `Faker`        | Fake data generation             |
| `PyYAML`       | YAML parsing                     |
| `selenium`     | Browser automation               |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available for educational purposes.
