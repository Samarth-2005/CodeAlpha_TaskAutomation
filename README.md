# CodeAlpha_TaskAutomation

A **Task Automation with Python Scripts** project built for the **CodeAlpha Python Programming Internship (Task 3)**.

## Project Overview

This script automates three real-life repetitive tasks from an interactive console menu:
1. **Move `.jpg` Files**: Moves all `.jpg` images from a source folder into a destination folder using `os` and `shutil`.
2. **Extract Email Addresses**: Scans any `.txt` file using regular expressions (`re`) and saves all unique email addresses to `extracted_emails.txt`.
3. **Scrape Webpage Title**: Fetches a live webpage, extracts its HTML `<title>` tag, and saves the result to `webpage_title.txt`.

## Key Concepts Used

- `os` and `shutil` modules (directory creation, file listing, moving files)
- `re` module (regex pattern matching for email addresses and HTML `<title>` tags)
- HTTP requests (`urllib.request`)
- File handling (`open()`, reading and writing `.txt` files)

## How to Run

1. Open a terminal in the project folder (`CodeAlpha_TaskAutomation`).
2. Run the script:
   ```bash
   python task_automation.py
   ```
