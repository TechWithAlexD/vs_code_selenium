# python
Tutorials and sample web automation tests project using VS Code, Selenium and Python

## Installation
1. Make sure you have [Python 3.13](https://www.python.org/downloads/) or newer installed on your machine. Check installation
    ```PS
    python -V
    ```
2. Clone this repository to your local machine.
3. Open folder (`vs_code_automation\python\selenium`) in VS Code. 
4. Optional: Create a virtual environment for the project
    ```
    python -m venv .venv
    ```
5. Optional: Activate the new virtual environment .venv
    ```
    .\.venv\Scripts\activate
    ```
6. Using terminal navigate to the project folder (e.g. selenium) and install the dependencies 
    ```
    pip install -r requirements.txt
    ```
7. Optional:  Select interpreter: open Command Palette and type in: "python select interpreter". Select the new virtual environment .venv
    ```
    .venv
    ```

## Usage
1. Make sure you have the appropriate browser installed (`https://www.selenium.dev/documentation/webdriver/browsers/`)
2. Open the project directory in VS Code or your preferred IDE. 
3. Run the tests using your preferred test runner or IDE or from terminal, e.g. use any of the following:
    ```PS
    pytest .\tests\test_selenium.py
    pytest -m selenium
    ```
4. Optional: Deactivate virtual environment, in terminal type in:
    ```
    deactivate
    ```

## Tech
- python 3.13
- selenium 4
- pytest 8

## YT channel
Please check my YouTube channel for step by step implementation or detailed tutorials on automation and more: https://www.youtube.com/@TechWithAlexDuta

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.