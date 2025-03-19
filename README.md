# Personal Smart Energy Budgeting 🌱⚡

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE) [![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-2.x-orange)](https://flask.palletsprojects.com/) [![SQLite](https://img.shields.io/badge/SQLite-3.x-yellow)](https://www.sqlite.org/index.html)

**SmartEnergyAI** is a web-based application designed to help users manage their energy consumption and costs effectively. It leverages **AI-driven predictions** and **automation** to provide real-time electricity price updates, calculate estimated daily and monthly costs, and automatically start or stop machines based on user-defined budgets. Additionally, it offers energy-saving suggestions by analyzing historical price data to identify the cheapest times to use energy.

This project is built using **Flask** for the backend and **HTML/CSS/JavaScript** for the frontend. It utilizes **Chart.js** for visualizations and **SQLite** for storing user budgets and price history.

---

## Demo 🎬

Here’s a quick demo of  Personal Smart Energy Budgeting  in action:

![Screenshot]("Energy Budget Management  Prediction2.gif")

The Demo showcases the following features:
- Fetching real-time electricity prices.
- Automatically toggling the machine based on budget constraints.
- Viewing energy-saving suggestions and price trends.
- Managing settings like daily and monthly budgets.

---

## Features 🚀

1. **Real-Time Energy Price Monitoring**
   - Fetch real-time electricity prices and calculate estimated daily and monthly costs based on your consumption.
   - Visualize price trends using interactive charts powered by Chart.js.

2. **Smart Budget Management**
   - Set daily and monthly budgets for energy consumption.
   - Receive alerts when your estimated costs exceed your budget.

3. **Automated Machine Control**
   - Automatically start or stop machines based on your budget constraints.
   - Emergency stop functionality ensures safety during critical situations.

4. **AI-Powered Energy-Saving Suggestions**
   - Leverage AI to analyze historical price data and suggest the best times to use energy for maximum savings.
   - Get actionable insights to reduce costs and optimize usage.

5. **Price History Tracking**
   - View the last 10 price update in a table and reset your energy price history with ease.
   - Maintain a record of past prices for future reference.

6. **User-Friendly Interface**
   - A sleek, modern UI built with HTML, CSS, and JavaScript.
   - Intuitive controls for managing settings, viewing charts, and toggling features.
     
7. **Energy Savings Suggestions**:
   - Analyze historical price data to suggest the cheapest times to use energy.

---

## Technologies Used 💻

- **Frontend**: HTML, CSS, JavaScript (Chart.js for visualizations, Font Awesome for icons)
- **Backend**: Python (Flask framework)
- **Database**: SQLite for storing user budgets and energy data
- **AI/ML**: Predictive analytics for energy-saving suggestions
- **Automation**: Automated machine control based on real-time data and budget constraints

---
## How It Works

1. **User Input**:
   - Users input their daily energy consumption, daily budget, and monthly budget.
   - These settings are saved to the database and used for cost calculations and machine control.

2. **Real-Time Price Updates**:
   - The application fetches the current electricity price from the backend and updates the UI every 10 seconds.

3. **Cost Calculation**:
   - The system calculates the estimated daily and monthly costs based on the current price and user-defined consumption.

4. **Automatic Machine Control**:
   - The system checks if the estimated costs exceed the user's budget.
   - If the budget is not exceeded, the machine starts automatically.
   - If the budget is exceeded, the machine stops automatically.

5. **Energy Savings Suggestions**:
   - The system analyzes historical price data and suggests the cheapest times to use energy.

6. **Emergency Stop**:
   - Users can activate an emergency stop to override automatic machine control.

---

## Installation Instructions 🛠️

### Prerequisites
- Python 3.8 or higher
- Flask (`pip install flask`)
- SQLite3 (usually pre-installed with Python)

### Steps to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Semilogo-Energy-Budgeting.git
   cd Semilogo-Energy-Budgeting
