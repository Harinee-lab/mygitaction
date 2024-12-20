


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

  deploy:
    runs-on: windows-latest
    needs: test  # Runs only if tests are successful

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.13.0'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Deploy locally
        shell: pwsh
        run: |
          $destination = 'C:\Users\Sowmyasree\Documents\deployment'
          
          # Ensure the destination directory exists
          if (!(Test-Path -Path $destination)) {
            New-Item -ItemType Directory -Path $destination
          }
          
          # Clear the destination directory
          Remove-Item -Path "$destination\*" -Recurse -Force

          # Copy files to the destination
          Copy-Item -Path .\* -Destination $destination -Recurse -Force

      - name: Verify deployment contents
        shell: pwsh
        run: |
          $destination = 'C:\Users\Sowmyasree\Documents\deployment'
          Get-ChildItem -Path $destination -Recurse

      - name: Deploy locally
        shell: pwsh
        run: |
          $destination = 'C:\Users\Sowmyasree\Documents\deployment'
    
          # Ensure the destination directory exists
          if (!(Test-Path -Path $destination)) {
          New-Item -ItemType Directory -Path $destination
          }
    
          # Clear the destination directory
          Remove-Item -Path "$destination\*" -Recurse -Force

          # Log files to be copied
          Write-Host "Files to be copied:"
          Get-ChildItem -Path .\* -Recurse

          # Copy files to the destination
          Copy-Item -Path .\* -Destination $destination -Recurse -Force
    
          # Verify copied contents
          Write-Host "Contents of the destination directory:"
          Get-ChildItem -Path $destination -Recurse





app.py



import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if _name_ == "_main_":
    unittest.main()
















