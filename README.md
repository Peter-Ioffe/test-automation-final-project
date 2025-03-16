# Test Automation Project

Watch a short demonstration of the test automation in action:

[Click Here to Watch](https://drive.google.com/file/d/1YmE0BgZo6B0KAzLQtwiOnZrG2vYv87gx/view?usp=sharing)

This repository was created to demonstrate a smart automation infrastructure. It contains a suite of automated test scripts developed in **Python** using **Selenium** and **Pytest**. The most significant advantages of the test infrastructure demonstrated here are that it can be ***easily maintained and expanded***. The tests target several types of applications and interfaces:

- **Web Testing** (an online banking website)
- **Mobile App Testing** (a to-do list application)
- **API Testing** (a JSON server)
- **Desktop App Testing** (Windows Calculator)
- **Electron App Testing** (another to-do list application)

## Table of Contents

- [Overview](#overview)
- [What Is Tested](#what-is-tested)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Screenshots](#screenshots)
- [Notes](#notes)
- [Contact](#contact)

---

## Overview

This project showcases diverse testing strategies within a single Python-based repository. It serves as a comprehensive demonstration of test automation practices by centralizing tests for **web**, **mobile**, **desktop**, **Electron**, and **API** environments.

Key features include:
- **Cross-Platform Testing**: Ensuring consistent functionality across multiple platforms and device types.
- **Continuous Integration**: Seamless integration into CI pipelines (**Jenkins**).
- **Maintainable Code Structure**: Illustrating best practices for organizing tests and page objects within Pytest.  
- **Scalable Testing**: Enabling easy extension to new devices or environments with minimal refactoring.
- **Page Object Model (POM) Design Pattern**: Implementation of POM to enhance maintainability and reusability.
- **Project Layers**: Clear separation of test cases, workflows, and extensions for maintaining the modular design.
- **Reporting System**: Automated test reports, including screenshots for failed tests.
- **Database Support**: Utilizing database-stored test data to validate test scenarios dynamically.
- **Common Functionality**: Reusable utility functions to avoid redundancy in test scripts.
- **External Files Support**: Utilizing external files (CSV, XML) for test data and configurations.
---

## What Is Tested

1. **Website Testing**  
   - Covers typical web scenarios (e.g., registering, logging into the website, UI element interactions, validations).

2. **Mobile App Testing**  
   - Tests a to-do list application on a mobile device (e.g., adding tasks, marking them as completed, and deleting them from the list).

3. **API Testing**  
   - Uses **requests** library to test a JSON Server REST API.

4. **Desktop App Testing**  
   - Automates basic and advanced functionality of the Windows Calculator application.

5. **Electron App Testing**  
   - Validates a to-do list functionality in an Electron-based application.

---

## Technologies Used

- **Programming Language**: Python (3.x)  
- **Testing Framework**: [Pytest](https://docs.pytest.org/en/stable/)  
- **Web Automation**: [Selenium WebDriver](https://www.selenium.dev/)  
- **Mobile Automation**: [Appium Studio](https://digital.ai/products/continuous-testing/appium-studio/free-trial/)
- **Desktop Automation**: [WinAppDriver](https://github.com/microsoft/WinAppDriver)
- **API**: [requests](https://pypi.org/project/requests/) library
- **JSON Server** (for mock API endpoints)
- **DB Browser for SQLite** (for database creation)
- **Continuous Integration**: [Jenkins](https://www.jenkins.io/)
- **Reporting**: [Allure Report](https://allurereport.org/)

---

## Project Structure

```
test-automation-final-project/
├── .idea/
├── allure-report/
├── allure-results/
│   └── history/
├── allure-screenshots/
├── configuration/
├── ddt/
├── extensions/
├── page_objects/
├── test_cases/
├── utilities/
├── workflows/
├── requirements.txt
└── README.md
```

- **.idea/**: Contains project-specific settings and configurations for IntelliJ's IDE.
- **allure-report/**: Houses the generated Allure test reports, providing a visual representation of test results.
- **allure-results/**: Stores raw data and history used by Allure to generate comprehensive test reports.
  - **history/**: Maintains historical data of test executions to track trends over time.
- **allure-screenshots/**: Contains screenshots captured during test executions, especially useful for debugging failed tests.
- **configuration/**: Contains a configuration file that includes settings essential for the test framework's operation.
- **ddt/**: Stands for Data-Driven Testing; this directory holds data files used to drive parameterized tests.
- **extensions/**: Contains custom extensions or actions that enhance or extend the functionality of the test framework.
- **page_objects/**: Implements the Page Object Model (POM) design pattern, with classes representing web pages or components to encapsulate page-specific behaviors and elements.
- **test_cases/**: Houses the test scripts organized by application type (web, mobile, API, etc.), each validating specific functionalities.
- **utilities/**: Contains utility modules and helper functions that support the main test scripts, promoting code reuse and modularity.
- **workflows/**: Defines test workflows that can be used across multiple test cases or modules.
- **requirements.txt**: Lists all Python dependencies required to set up and run the tests.
- **README.md**: Provides an overview of the project, including its structure, technologies used, and other pertinent information.

---

## Setup

To run the tests for mobile, Electron, and desktop applications, Selenium 3 is recommended (e.g., version 3.141.0).

In test_cases/conftest.py file, the get_chrome() method's definition should be as follows:
~~~bash
def get_chrome():
    chrome_driver = selenium.webdriver.Chrome(ChromeDriverManager().install())
    return chrome_driver
~~~

(The examples given here are for the Chrome browser; if another browser is used, then the correspondent method's definition should be adjusted accordingly.)

For web and API tests, Selenium 4 (latest version) should be installed in the IDE. Then, the get_chrome() method's definition should be as follows:
~~~bash
def get_chrome():
    srv = Service(ChromeDriverManager().install())
    chrome_driver = selenium.webdriver.Chrome(service=srv)
    return chrome_driver
~~~

Additionally, the project is configured to run via Jenkins. To run it from an IDE (e.g., PyCharm), the configuration/data.xml file must be changed.

Replace:
~~~bash
<CsvLocation>ddt/loans.csv</CsvLocation>
~~~
With:
~~~bash
<CsvLocation>../ddt/loans.csv</CsvLocation>
~~~

Also, replace:
~~~bash
<ScreenshotPath>./allure-screenshots/</ScreenshotPath>
~~~
With:
~~~bash
<ScreenshotPath>./../allure-screenshots/</ScreenshotPath>
~~~
---
## Screenshots
![Jenkins](https://imgur.com/tohC42S.png)

![Allure 1](https://imgur.com/5hq4xwp.png)

![Allure 2](https://imgur.com/FWt9B89.png)
---
## Notes
It is essential to point out that this project is for demonstration purposes only. In an actual testing environment, it should be divided into several projects.

---
## Contact

- **Author**: [Peter Ioffe](https://www.linkedin.com/in/peter-ioffe-594432155/) (LinkedIn)

If you have any questions, suggestions, or issues, please reach out via LinkedIn or directly via GitHub.
