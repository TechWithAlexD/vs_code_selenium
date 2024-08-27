# python
Tutorials and sample web automation tests project using VS Code, Fantoccini and Rust

## Installation
1. Make sure you have installed [Rust](https://www.rust-lang.org/tools/install). Installation steps can be found [here](https://www.youtube.com/watch?v=yUnh6l9cK18). 
Check installation:
    ```PS
    rustc --version
    ```
2. Clone this repository to your local machine.
3. Open folder (`rust`) in VS Code. 
4. Using terminal navigate to Cargo.toml file location and run (Cargo will fetch the dependencies and all of their dependencies)
    ```PS
    cargo build
    ```

## Usage
1. Make sure you have Chrome browser installed
2. Make sure you have the corresponding chrome driver version (based on browser version) started (e.g. locally)
3. Open the project directory (e.g. fantoccini_tests) in VS Code or your preferred IDE. 
4. Run the tests using your preferred test runner or IDE or from terminal, e.g. use any of the below:
    ```PS
    cargo test
    ```

## Tech
- rust 1.78+
- fantoccini 0.21+
- tokio 1.39.2+
- serde_json 1.0.124+

## YT channel
Please check my YouTube channel for step by step implementation or detailed tutorials on automation and more: https://www.youtube.com/@TechWithAlexDuta

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.