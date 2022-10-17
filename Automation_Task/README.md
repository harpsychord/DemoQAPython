## Automation task

### Installation

1. Please ensure you have Python3 and the Firefox geckodriver installed and in your system path!

You can download the geckodriver at https://github.com/mozilla/geckodriver/releases

2. Navigate to the Automation_Task folder in the command line and run the following command:

```
pip -r requirements.txt
```

This installs all of the necessary pip modules to run this test automation.

### Execution

To run the automation, run the following command while in the Automation_Task folder:

```
pytest -v --driver Firefox testBookstore.py
```