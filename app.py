from flask import Flask, render_template, jsonify, request
import random
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Simulating price history
price_history = []

# Initialize SQLite database
DATABASE = 'energy_budget.db'

# Global Variables
machineRunning = False  # Tracks whether the machine is running
emergencyStopActive = False  # Tracks whether the emergency stop is active

def init_db():
    """Initialize the database and create the table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS energy_budget (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            daily_consumption REAL,
            daily_budget REAL,
            monthly_budget REAL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_price')
def get_price():
    price = round(random.uniform(0.10, 0.30), 2)  # Random price between 0.10 and 0.30 EUR
    return jsonify({"price": price})

@app.route('/api/get_price_history')
def get_price_history():
    return jsonify({"history": price_history[-10:]})  # Return last 10 records

@app.route('/api/add_price_history')
def add_price_history():
    price = round(random.uniform(0.10, 0.30), 2)
    timestamp = datetime.now().strftime("%d-%B-%Y %H:%M:%S")  # Day-Month-Year format
    price_history.append({"price": price, "timestamp": timestamp})
    return jsonify({"message": "Price history updated successfully!"})

@app.route('/api/reset_history', methods=['POST'])
def reset_history():
    global price_history
    price_history = []  # Clear history list
    return jsonify({"success": True, "message": "Price history reset successfully!"})

@app.route('/api/save_budget', methods=['POST'])
def save_budget():
    """Save the energy budget to the database."""
    data = request.json
    daily_consumption = data.get('dailyConsumption')
    daily_budget = data.get('dailyBudget')
    monthly_budget = data.get('monthlyBudget')

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO energy_budget (daily_consumption, daily_budget, monthly_budget)
        VALUES (?, ?, ?)
    ''', (daily_consumption, daily_budget, monthly_budget))
    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": "Budget saved successfully!"})

@app.route('/api/get_budget', methods=['GET'])
def get_budget():
    """Retrieve the latest energy budget from the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT daily_consumption, daily_budget, monthly_budget FROM energy_budget ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()
    conn.close()

    if result:
        daily_consumption, daily_budget, monthly_budget = result
        return jsonify({
            "dailyConsumption": daily_consumption,
            "dailyBudget": daily_budget,
            "monthlyBudget": monthly_budget
        })
    else:
        return jsonify({"message": "No budget data found."}), 404

@app.route('/api/auto_toggle_machine', methods=['GET'])
def auto_toggle_machine():
    """Automatically determine if the machine should start or stop based on budget."""
    global machineRunning, emergencyStopActive

    # Fetch the latest budget from the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT daily_consumption, daily_budget, monthly_budget FROM energy_budget ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()
    conn.close()

    if not result:
        return jsonify({"error": "No budget data found."}), 404

    daily_consumption, daily_budget, monthly_budget = result

    # Simulate fetching the current price
    current_price = round(random.uniform(0.10, 0.30), 2)

    # Calculate costs
    daily_cost = current_price * daily_consumption
    monthly_cost = daily_cost * 30

    # Determine if the machine should start or stop
    if not emergencyStopActive:
        if daily_cost <= daily_budget and monthly_cost <= monthly_budget and not machineRunning:
            action = "start"
            machineRunning = True
        elif (daily_cost > daily_budget or monthly_cost > monthly_budget) and machineRunning:
            action = "stop"
            machineRunning = False
        else:
            action = "no_change"
    else:
        action = "stop"  # Emergency stop overrides all other logic

    return jsonify({
        "action": action,
        "machineRunning": machineRunning,
        "emergencyStopActive": emergencyStopActive,
        "dailyCost": daily_cost,
        "monthlyCost": monthly_cost,
        "dailyBudgetExceeded": daily_cost > daily_budget,
        "monthlyBudgetExceeded": monthly_cost > monthly_budget
    })

@app.route('/api/emergency_stop', methods=['POST'])
def emergency_stop():
    """Toggle the emergency stop state."""
    global emergencyStopActive, machineRunning

    # Toggle emergency stop state
    emergencyStopActive = not emergencyStopActive

    # Stop the machine if emergency stop is activated
    if emergencyStopActive:
        machineRunning = False

    return jsonify({
        "emergencyStopActive": emergencyStopActive,
        "machineRunning": machineRunning,
        "message": "Emergency stop toggled successfully."
    })

@app.route('/api/predict_energy_needs', methods=['GET'])
def predict_energy_needs():
    """Predict the best times to use energy for maximum savings."""
    # Fetch the latest budget from the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT daily_consumption, daily_budget, monthly_budget FROM energy_budget ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()
    conn.close()

    if not result:
        return jsonify({"error": "No budget data found."}), 404

    daily_consumption, daily_budget, monthly_budget = result

    # Analyze price history to find the cheapest times
    if not price_history:
        return jsonify({"error": "No price history available."}), 404

    # Sort price history by price (ascending)
    sorted_history = sorted(price_history, key=lambda x: x['price'])

    # Suggest the cheapest times to use energy (top 5)
    suggestions = []
    for entry in sorted_history[:5]:  # Top 5 cheapest times
        suggestions.append({
            "timestamp": entry['timestamp'],
            "price": entry['price']
        })

    return jsonify({
        "suggestions": suggestions,
        "message": "Here are the best times to use energy for maximum savings."
    })

if __name__ == '__main__':
    init_db()  # Initialize the database on startup
    for _ in range(5):  # Add some initial data
        app.test_client().get('/api/add_price_history')
    app.run(debug=True)