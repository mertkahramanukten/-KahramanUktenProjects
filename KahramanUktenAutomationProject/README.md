# Insider Automation Project

## Overview
This project automates the following test case on [Insider Website](https://useinsider.com/):

1. Visit https://useinsider.com/ and ensure the homepage loads correctly.
2. Navigate to Company > Careers and verify that:
   - Careers page is loaded
   - "Locations", "Teams", and "Life at Insider" sections are present

## Tech Stack
- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM) structure
- Works on both Chrome and Firefox

## How to Run
Install dependencies:
```bash
pip install -r requirements.txt
```

Run the tests with Chrome (default):
```bash
pytest tests/test_insider.py
```

Run with Firefox:
```bash
pytest tests/test_insider.py --browser firefox
```

## Notes
- A screenshot will be taken on any test failure and saved under `/screenshots/`.