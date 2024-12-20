name: Python CI/CD Pipeline

on:
  push:
    branches:
      - main  # Trigger on pushes to the main branch
  pull_request:
    branches:
      - main  # Trigger on pull requests targeting the main branch

jobs:
  test:
    runs-on: windows-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3  # Checks out your code

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.13.0'  # Specify your Python version

      - name: Install dependencies
        run: |
          pip install -r requirements.txt  # Install necessary packages

      - name: Run tests
        run: |
          python -m unittest discover -s tests  # Adjust the path as needed

 
          
          







