# csharp
Tutorials and sample web automation tests project using VS Code, Selenium and C#

## Installation
1. Make sure you have [.NET 8 SDK](https://dotnet.microsoft.com/en-us/download) or newer installed on your machine (projects were developed using .NET 8). Check installation
    ```PS
    dotnet --version
    ```
2. Clone this repository to your local machine.
3. Open folder (`csharp`) in VS Code. 
4. Using terminal navigate to a project and run `dotnet build` (implicit restore)
    ```PS
    dotnet build
    ```

## Usage
1. Make sure you have the appropriate browser installed (`https://www.selenium.dev/documentation/webdriver/browsers/`)
2. Open the solution directory in VS Code or your preferred IDE. 
3. Using terminal navigate to a project (cd command) and run `dotnet build` (implicit restore).
4. Run the tests using your preferred test runner or IDE or from terminal, e.g. use any of the below:
    ```PS
    dotnet test .\bin\Debug\net8.0\selenium_tests.dll
    dotnet test .\bin\Debug\net8.0\selenium_tests.dll --filter TestCategory="Selenium"
    ```

## Tech
- .NET 8.0
- C#
- Selenium WebDriver 4
- NUnit 4
- NUnit3TestAdapter
- .NET.Test.SDK

## YT channel
Please check my YouTube channel for step by step implementation or detailed tutorials on automation and more: https://www.youtube.com/@TechWithAlexDuta

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.