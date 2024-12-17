from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)

# Helper function to load meal data from a specific file
def load_meal_data(filename):
    """
    Loads meal data from a JSON file located in the 'meal_data' directory.
    If the file is not found or contains invalid JSON, returns an empty dictionary.
    """
    file_path = os.path.join("meal_data", filename)  # Construct the file path
    try:
        with open(file_path, "r") as file:  # Attempt to open the file
            return json.load(file)  # Load and return JSON data
    except (FileNotFoundError, json.JSONDecodeError):  # Handle errors gracefully
        return {}

# Load all meal data from multiple predefined JSON files
def load_all_meal_data():
    """
    Loads meal data for all meal types (e.g., Breakfast, Lunch, etc.)
    by calling `load_meal_data` for each specific file.
    Returns a dictionary with meal types as keys and their corresponding data.
    """
    return {
        "Breakfast": load_meal_data("breakfast_data.json"),
        "Lunch": load_meal_data("lunch_data.json"),
        "Dinner": load_meal_data("dinner_data.json"),
        "Dessert": load_meal_data("dessert_data.json"),
        "Snack": load_meal_data("snack_data.json"),
        "Drinks": load_meal_data("drinks_data.json"),
    }

# Load meal data
meal_data = load_all_meal_data()

# Initialize log and monthly calendar
log = {
    "meals": {},
    "totals": {"Calories": 0, "Protein (g)": 0, "Sat Fat (g)": 0, "Added Sugar (g)": 0, "Total Cost ($)": 0}
}
calendar = {day: {"meals": [], "cost": 0} for day in range(1, 31)}

@app.route("/")
def index():
    return render_template("index_with_totals.html", log=log, meal_data=meal_data, calendar=calendar)

@app.route("/add", methods=["POST"])
def add_meal():
    meal_type = request.form["meal_type"]
    meal_item = request.form["meal_item"]
    
    # Add meal to daily log
    if meal_type not in log["meals"]:
        log["meals"][meal_type] = []
    log["meals"][meal_type].append(meal_item)

    # Update totals
    for key in log["totals"].keys():
        log["totals"][key] += meal_data[meal_type][meal_item][key]

    return redirect(url_for("index"))

@app.route("/clear")
def clear_log():
    global log
    log = {
        "meals": {},
        "totals": {"Calories": 0, "Protein (g)": 0, "Sat Fat (g)": 0, "Added Sugar (g)": 0, "Total Cost ($)": 0}
    }
    return redirect(url_for("index"))

@app.route("/add_to_calendar", methods=["POST"])
def add_to_calendar():
    day = int(request.form["day"])
    meal_type = request.form["meal_type"]
    meal_item = request.form["meal_item"]
    
    # Add meal to calendar
    calendar[day]["meals"].append(f"{meal_type}: {meal_item}")
    calendar[day]["cost"] += meal_data[meal_type][meal_item]["Total Cost ($)"]
    
    return redirect(url_for("index"))

@app.route("/clear_calendar")
def clear_calendar():
    global calendar
    calendar = {day: {"meals": [], "cost": 0} for day in range(1, 31)}
    return redirect(url_for("index"))

@app.route("/clear_daily_log")
def clear_daily_log():
    """
    Clears the daily meal log and resets the totals.
    """
    global log
    log = {
        "meals": {},
        "totals": {"Calories": 0, "Protein (g)": 0, "Sat Fat (g)": 0, "Added Sugar (g)": 0, "Total Cost ($)": 0}
    }
    return redirect(url_for("index"))


'''
ADDING ACCESS TO OTHER TABS HERE
'''

@app.route('/habit_building')
def habit_building():
    return render_template('habit_building.html')

@app.route('/add_meals')
def add_meals():
    return render_template('add_meals.html')

@app.route('/workouts')
def workouts():
    return render_template('workouts.html')


'''
OTHER TABS HERE
'''


if __name__ == "__main__":
    app.run(debug=True)
