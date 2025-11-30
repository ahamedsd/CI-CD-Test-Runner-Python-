Overview

TestPilot CI Runner is a simple Python-based tool that automatically discovers and executes unit tests inside a project. It is designed to make testing feel effortless, especially when the project begins to grow and you no longer want to run individual test files manually. The tool gathers all tests, runs them at once, and produces a clear HTML report showing which parts of the code are working and which need attention.

This project is intended for learners and intermediate Python developers who want a gentle introduction to automation testing and basic DevOps-style workflows.

How It Works

The tool goes through four main steps:

Test Discovery
The runner scans the tests folder and finds every test file whose name starts with “test_”. This helps the system automatically pick up new test files without any changes to the code.

Test Execution
After discovery, the built-in unittest framework takes over. It executes all the test cases and stores the results, including passes, failures, errors, and timestamps.

HTML Report Creation
A separate module converts the raw results into a readable HTML report. This report is saved inside the reports folder and gives a simple, clean summary of the entire test run.

Logging
Every major action is logged. This includes which tests were detected, if any test failed unexpectedly, and when the report was generated. The log file can be found in the logs folder.

Project Structure
The project is divided into small, understandable parts:

src – contains the main logic of the test runner and the HTML report generator
tests – holds your test files
reports – stores all generated HTML reports
logs – saves log messages
README.txt – documentation for the project

Who This Project Is For
This tool is helpful for anyone learning testing, continuous integration, or basic DevOps concepts. 
It is especially useful for beginners who want hands-on experience with automation but do not want to deal with heavy tools or complicated setups.

How To Run
To use the tool, simply run the test_runner.py file inside the src folder. 
The tests will run automatically, and the HTML report will be generated inside the reports folder.

Example:

python src/test_runner.py

After the run completes, open the latest report file in your browser to see the results.

What You Can Do Next
This project can grow in many directions. Here are some ideas if you want to extend it further:

• Add parallel test execution for faster results.
• Add an option to send failed-test notifications by email or messaging apps.
• Connect it to GitHub Actions or another CI pipeline so it runs automatically on every code push.
• Add a configuration file to control paths and options easily.
• Improve the HTML report design or add charts showing test history.

Summary

TestPilot CI Runner gives you a lightweight, easy-to-understand testing workflow. It helps you automate your tests, generate readable reports, and keep track of what is happening inside your project. 
It’s simple enough for beginners but flexible enough to evolve into a more serious automation tool.
