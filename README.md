# 🔐 Password Strength Meter

# Overview

The Password Strength Meter is a Python-based tool that evaluates the security of a user's password and provides actionable feedback to improve it. Built using Streamlit , this app offers a user-friendly interface to check password strength, generate strong passwords, and blacklist commonly used weak passwords.

This project is perfect for learning control flow , string manipulation , regular expressions , and GUI development with Streamlit. It also teaches security best practices for creating strong passwords.

# Features

# Core Features

Password Strength Checker :

Evaluates passwords based on length , character types , and patterns .

Assigns a strength score: Weak , Moderate , or Strong .

Provides feedback to improve weak passwords.

Password Generator :

Suggests a strong password if the input is weak.

Blacklist for Common Passwords :

Rejects commonly used weak passwords like "password", "123456", etc.

# Streamlit GUI

A clean and interactive interface for users to input their passwords and view results.

Displays feedback and suggestions in real-time.

Installation and Setup

# Prerequisites

Python 3.7 or higher installed on your system.

Basic knowledge of running Python scripts.

# Usage

Enter a Password :

Input your password in the text box and press Enter.

View Results :

The app will display the password's strength (Weak, Moderate, Strong).

If the password is weak, the app will provide feedback and suggest improvements.

Generate a Strong Password :

If your password is weak, the app will suggest a strong password for you.

Blacklist Check :

If the password is commonly used (e.g., "password123"), the app will reject it and prompt you to choose a stronger one.

# Deployment

To share this app with others, you can deploy it on Streamlit Cloud :

Push your code to a GitHub repository.

Go to Streamlit Cloud and link your GitHub repo.

Streamlit will automatically deploy your app and provide a public URL.

# Code Explanation

The app is built using the following components:

Password Strength Checker :

Uses regular expressions (re) to check for uppercase, lowercase, digits, and special characters.

Assigns a score based on the criteria and provides feedback.

Password Generator :

Randomly generates a strong password with a mix of uppercase, lowercase, digits, and special characters.

Blacklist :

Maintains a list of common weak passwords and rejects them.

Streamlit GUI :

Provides an interactive interface with real-time feedback.

# Future Enhancements

Here are some ideas to expand the app:

Custom Scoring Weights :

Allow users to customize the weight of each criterion (e.g., prioritize length over special characters).

Additional Security Checks :

Detect repeated characters, sequential patterns (e.g., "1234", "abcd"), or dictionary words.

Save Results :

Add a feature to save password strength results or generated passwords.

Multi-Language Support :

Support feedback and instructions in multiple languages.

Integration with APIs :

Use APIs to check if a password has been exposed in data breaches (e.g., Have I Been Pwned API ).

# Acknowledgments

Inspired by Sir Zia GIAIC Python projects https://github.com/panaversity/learn-modern-ai-python/blob/main/CLASS_PROJECTS/02_password_strength_meter/password_strength_meter_assignment.md.

Built using Streamlit , an open-source framework for building data apps.

# Contact

For questions or feedback, feel free to reach out:

Email: asadhussainshad@gmail.com
GitHub: huzaifa-1100
linkedin: https://www.linkedin.com/in/huzaifa-ayub-b29132288/