# Automaticity Academy - Automated Testing Suite

## Project Overview
This repository contains automated tests for Automaticity Academy, implemented using Selenium WebDriver, pytest-bdd, and the Page Object Model (POM). The tests cover core functionalities, including login, registration, and dashboard redirection.

## Technologies Used
- Python 3.11+
- Selenium WebDriver
- pytest-bdd (Behavior-Driven Development framework)
- WebDriver Manager (for automatic driver setup)
- Page Object Model (POM) for maintainable test structure
- Logging and screenshot capture on test failure

## Project Structure
```
automaticity_tests/
│── features/              # BDD feature files
│── pages/                 # Page Object Model implementation
│── tests/                 # Test cases using pytest-bdd
│── logs/                  # Test execution logs
│── screenshots/           # Failure screenshots
│── videos/                # Test execution recordings
│── conftest.py            # Pytest configuration & WebDriver setup
│── requirements.txt       # Python dependencies
│── config.json            # Test data and environment configuration
│── README.md              # Project documentation
```

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/jovankns/automaticity_tests.git
cd automaticity_tests
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Tests
#### Run all tests:
```bash
pytest --browser=chrome
```
#### Run specific test:
```bash
pytest tests/test_login.py
```
#### Run tests with verbose output:
```bash
pytest -v
```
#### Run tests and capture screenshots on failure:
```bash
pytest --browser=chrome --capture=tee-sys
```

## Test Execution Details
- **WebDriver Setup:** WebDriver is managed via `webdriver-manager`, eliminating the need to manually install drivers.
- **Headless Mode:** To run tests in headless mode, set `HEADLESS_FLAG=True`.
- **Logging & Reports:** Execution logs are stored in `logs/`, while failure screenshots are saved in `screenshots/`.
- **Video Recording:** Test sessions are recorded and saved in `videos/`.

## Pytest-BDD Commands and Documentation
For detailed pytest-bdd commands and usage, refer to:
- Official documentation: https://pytest-bdd.readthedocs.io/en/latest/
- Running scenarios: `pytest --feature=features/login.feature`
- Running all tests in parallel: `pytest -n auto`

## Contributing
To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-new-test`)
3. Commit changes (`git commit -m "Added new test for XYZ"`)
4. Push the branch (`git push origin feature-new-test`)
5. Create a pull request

## License
This project is licensed under the JK License.

