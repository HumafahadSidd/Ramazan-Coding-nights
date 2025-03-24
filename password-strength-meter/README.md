# Password Strength Meter

A modern web-based application that checks password strength in real-time, built with Streamlit.

## Features

- Modern, responsive web interface
- Real-time password strength evaluation
- Visual strength indicator with progress bar
- Color-coded strength levels
- Interactive requirements checklist
- Helpful tips for weak passwords
- Secure password input (hidden characters)

## Requirements

- Python 3.x
- Streamlit

## Installation

1. Clone this repository or download the files
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## How to Run

1. Make sure you have Python and the requirements installed
2. Run the application using:
   ```
   streamlit run app.py
   ```
3. The application will open in your default web browser

## Password Requirements

The password strength is evaluated based on three simple criteria:
- Minimum length of 6 characters
- Contains at least one number
- Contains at least one letter

## Usage

1. Launch the application
2. Type or paste your password in the input field
3. The strength meter will update in real-time
4. Check the requirements checklist to see what's missing
5. Follow the tips if your password is weak

## Security Note

This application runs locally on your machine and does not store or transmit any passwords. 