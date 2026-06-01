
##  Overview

This project demonstrates **core file handling concepts in Python** using only built-in features.
It progresses from basic file writing to building a **mini report system with error handling and user input**.

---

## ⚙️ Restrictions Followed

* ❌ No external libraries (`pandas`, `csv`, etc.)
* ✅ Only built-in file handling (`open()`)
* ✅ Simple logic and condition checks
* ✅ `os.path.exists()` used for safe file handling (Task 6)

---

#  Task 1: Write Sales Records to a File

###  Objective

Store a list of sales values into a file.

###  Key Points

* Use `"w"` mode (write mode)
* Each value stored on a new line

###  Concept

* Overwrites existing file
* Used for fresh data storage

---

#  Task 2: Read File in Different Ways

###  Objective

Understand different file reading methods

###  Methods

* `read()` → entire file
* `readline()` → single line
* `readlines()` → list of lines

###  Concept

* `.strip()` removes newline characters
* Convert strings → integers for processing

---

#  Task 3: Append New Sales

###  Objective

Add new data without deleting old data

###  Key Points

* Use `"a"` mode (append mode)
* Data is added at the end

###  Concept

* Useful for logs, transactions, history

---

#  Task 4: Generate Summary Report

###  Objective

Analyze file data

###  Operations

* Total Sales → `sum()`
* Highest Sale → `max()`
* Lowest Sale → `min()`
* Average → `total / count`

###  Concept

* File data must be cleaned (`strip()`)
* Convert to integers before calculations

---

#  Task 5: Product Info File (User Input)

###  Objective

Store user-entered product data

###  Format

```
ProductName | Price
```

###  Concept

* Acts like a simple database
* Uses `input()` for dynamic data

---

#  Task 6: Read File Safely

###  Objective

Prevent program crashes if file does not exist

###  Method Used

```
os.path.exists(filename)
```

###  Concept

* Avoids runtime errors
* Displays user-friendly message

---

#  Task 7: Mini Project – Discount Report

###  Objective

Create a complete report system

###  Features

* Dictionary-based product pricing
* User input for discount
* Discount calculation
* File export (`discount_report.txt`)
* Summary generation

###  File Format

```
Product | Original Price | Discounted Price
```

###  Concept

* Combines all previous learnings
* Simulates real billing/report system

---

#  Real-World Applications

*  E-commerce order systems
*  Invoice & billing systems
*  Sales analytics without databases
*  Log and report generation

---

#  Key Learnings

* File modes: `"r"`, `"w"`, `"a"`
* Data persistence using text files
* Data cleaning (`strip()`)
* Type conversion (`int()`, `float()`)
* Error-safe file handling
* Structured data storage in plain text

---

#  Conclusion

This project builds a strong foundation in:

* File handling
* Data processing
* User interaction
* Real-world backend logic



Your Name
deepak shukla
