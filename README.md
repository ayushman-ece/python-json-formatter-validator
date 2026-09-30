# 🧾 Python JSON Formatter & Validator

A simple Python command-line tool that formats, validates, and reads JSON data using Python's built-in `json` module.

---

## 🎯 Project Goal

The goal of this project is to learn how to:

- Work with JSON data
- Convert JSON strings into Python objects
- Validate JSON
- Format JSON
- Read JSON files
- Handle JSON errors
- Work with Python's built-in `json` module

---

## ✨ Features

- 🧾 Format JSON
- ✅ Validate JSON
- 📂 Load JSON files
- ❌ Detect invalid JSON
- 🛡️ Handle file errors
- ⚡ No external libraries required

---

## 🛠️ Technologies Used

- Python
- JSON
- `json` module
- Exception Handling
- File Handling
- Object-Oriented Programming

---

## 📁 Project Structure

```text
python-json-formatter-validator/
│
├── main.py
├── json_tool.py
├── sample.json
├── README.md
└── .gitignore
```

---

# 🧠 Concepts Learned

## 1. JSON Module

Python provides a built-in JSON module:

```python
import json
```

---

## 2. Loading JSON

```python
json.loads(text)
```

This converts a JSON string into a Python object.

---

## 3. Reading JSON Files

```python
json.load(file)
```

This reads JSON directly from a file.

---

## 4. Formatting JSON

```python
json.dumps(data, indent=4)
```

The `indent=4` makes JSON easier to read.

---

## 5. JSON Validation

```python
try:
    json.loads(text)
except json.JSONDecodeError:
    print("Invalid JSON")
```

If the JSON syntax is incorrect, Python raises `JSONDecodeError`.

---

## 6. File Handling

The project uses:

```python
with open(filename, "r", encoding="utf-8") as file:
```

This safely opens and reads a JSON file.

---

# 🚀 How to Run

Run:

```bash
python main.py
```

No additional packages are required.

---

# 🖥️ Program Menu

```text
🧾 JSON FORMATTER & VALIDATOR

1. Format JSON
2. Validate JSON
3. Load JSON File
4. Exit
```

---

# 📚 What I Learned

- JSON data
- Python `json` module
- `json.loads()`
- `json.dumps()`
- `json.load()`
- JSON validation
- JSON error handling
- File handling
- Exception handling
- Classes and objects

---

# 🔮 Future Improvements

- Save formatted JSON to a new file
- Minify JSON
- Validate multiple JSON files
- Compare two JSON files
- Add JSON key search
- Add JSON statistics
- Create a graphical interface

---

# 🎓 Project Status

✅ Completed

This project was built as part of my Python learning journey.

---

# 👨‍💻 Author

**Ayushman Tiwari**

GitHub:

https://github.com/ayushman-ece