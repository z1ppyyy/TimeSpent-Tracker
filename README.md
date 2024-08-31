# Time Spent Tracker of the Progress Telegram Channel

<img width="1123" alt="Screenshot 2024-08-31 at 7 14 52 PM" src="https://github.com/user-attachments/assets/a0344a7b-d0c3-4831-8361-3ddcd1be6910">

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [Help](#help)
- [License](#license)

## Features

The **Time Spent Tracker** is a Python-based application built with Flask. It tracks the amount of time users spend on programming in the Progress Telegram Channel. The tracker allows users to specify a username and a month, then it will calculate the total time spent by the user during that month.

## Requirements

- Python 3.8+
- Telegram API ID and Hash (See the [Usage](#usage) section for details on how to obtain these)
- Flask
- Telethon

## Usage

### 1. Setting Up the Telegram API

To use the Time Spent Tracker, you'll need to obtain your Telegram API credentials:

1. Visit the [Telegram API Page](https://my.telegram.org/apps).
2. Log in with your Telegram account.
3. Click on **API development tools**.
4. Create a new application by filling in the required fields.
5. Once created, you'll receive your **API ID** and **API Hash**.
6. Copy these credentials into your `tracker.py` file:

```python
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
```

### 2. Install Dependencies
Make sure you have Python installed. Install the required dependencies by running:

```
pip install -r requirements.txt
```
### 3. Run the Application
To start the application, use the following command:

```
flask run
```
Then, open your browser and go to http://127.0.0.1:5000/ to use the tracker.

### 4. Input
Enter your Telegram name in the input field.
Select the month you want to track.
Click the "Submit" button to get the total time spent.
Contributing
Contributions are welcome! Feel free to submit a Pull Request or open an Issue.

## Steps to Contribute:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Push to your fork and submit a Pull Request.
5. Help
6. If you encounter any issues or have questions, please open an issue in this repository.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
