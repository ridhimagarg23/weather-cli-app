# Weather CLI App

A simple command-line weather application built using Python.
It fetches real-time weather data using an API and displays it in a clean format.

---

## Features

* Get real-time weather by city name
* CLI-based input using argparse
* Secure API key management using dotenv
* Error handling for invalid cities
* Clean and readable output

---

## Tech Stack

* Python
* argparse
* requests
* python-dotenv

---

## Installation

1. Clone the repository:
   git clone https://github.com/ridhimagarg23/weather-cli-app.git

2. Navigate to the project folder:
   cd weather-cli-app

3. Create virtual environment:
   python -m venv venv

4. Activate environment:
   venv\Scripts\activate

5. Install dependencies:
   pip install requests python-dotenv

---

## Setup

Create a `.env` file in the root directory:

API_KEY=your_api_key_here

---

## Usage

Run the app using:

python app.py --city Delhi

---

## Example Output

Weather in Delhi:
Temperature: 23°C
Humidity: 73%
Description: Haze

---

## Error Handling

* Displays error if city is not found
* Prevents crashes using safe checks

---

## Future Improvements

* Add wind speed and feels-like temperature
* Support multiple cities
* Add GUI version

---

## Author

Ridhima Garg
