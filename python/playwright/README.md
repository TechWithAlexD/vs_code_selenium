# python
Tutorials and sample web automation tests project using VS Code, Playwright and Python

## Installation
1. Make sure you have [.Python 3](https://www.python.org/downloads/) or newer installed on your machine (project was developed using python 3.12). Check installation
    ```PS
    python -V
    ```
2. Install playwright and the browsers as described here: https://youtu.be/NSF8Dn-oP38?feature=shared
3. Clone this repository to your local machine.
4. Open folder (`vs_code_automation\python\playwright`) in VS Code. 

## Usage
1. Open the project directory in VS Code or your preferred IDE. 
3. Run the tests using your preferred test runner or IDE or from terminal, e.g. use any of the below:
    ```PS
    pytest test_playwright.py
    pytest test_playwright.py --headed
    pytest test_playwright.py --headed --browser firefox
    pytest test_playwright.py --headed --browser firefox --browser webkit --browser chromium
    pytest test_playwright.py --headed --browser-channel msedge --headed
    pytest test_playwright.py --headed --browser-channel chrome --headed
    pytest --headed --browser firefox --browser webkit --browser chromium --numprocesses 3
    ```

## Tech
- python 3.12
- pytest-playwright 1.46
- pytest 8
- pytest-xdist 3.6

## YT channel
Please check my YouTube channel for step by step implementation or detailed tutorials on automation and more: https://www.youtube.com/@TechWithAlexDuta

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.