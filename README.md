# 📁 File Manager

A simple **Command-Line File Manager** built with Python.

This project is created as a learning project to practice Python and learn how to work with the filesystem using the `os` module.

## 🚀 Features

Currently, the project supports:

* 📍 Show the current directory
* 📄 List files and directories
* 📁 Create directories
* 🗑️ Delete files
* 📂 Delete empty directories
* 🔍 Check if a file or directory exists
* 🔎 Search for a file inside the current directory and its subdirectories
* 👤 Display the current username

## 🛠️ Technologies

* Python 3
* `os`
* `time`

## 📚 What I Am Learning

Through this project, I am practicing:

* Python functions
* `if / elif / else`
* `while` and `for` loops
* `break`
* `return`
* Lists
* String manipulation
* File and directory operations
* `os.path`
* `os.listdir()`
* `os.walk()`
* `os.path.join()`
* Error handling with `try / except`

## 🔍 File Search

The project uses `os.walk()` to search recursively inside directories.

Example:

```python
for root, dirs, files in os.walk(path):
    if name in files:
        print(f"* Found: {os.path.join(root, name)}")
        break
else:
    print(f"* {name} not found")
```

This allows the program to search not only in the current directory, but also inside its subdirectories.

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/hatimhansal/file-manager.git
```

Enter the project directory:

```bash
cd file-manager
```

Run the program:

```bash
python page1.py
```

## 📌 Project Status

🚧 **Work in Progress**

This project is still under development.

I am building it step by step while learning Python and improving my understanding of filesystem operations.

## 🎯 Future Improvements

Some features I may add later:

* Rename files and directories
* Copy files
* Move files
* File information
* File size formatting
* Better error handling
* Better CLI interface
* Search by file extension
* Search by filename
* Navigation between directories

---

Made with 🐍 Python
