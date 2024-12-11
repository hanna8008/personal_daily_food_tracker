import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Helper function to load meal data from individual files
def load_meal_data(filename):
    file_path = os.path.join("meal_data", filename)
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Load all meal data from files
def load_all_meal_data():
    return {
        "Breakfast": load_meal_data("breakfast_data.json"),
        "Lunch": load_meal_data("lunch_data.json"),
        "Dinner": load_meal_data("dinner_data.json"),
        "Dessert": load_meal_data("dessert_data.json"),
        "Snack": load_meal_data("snack_data.json"),
        "Drinks": load_meal_data("drinks_data.json"),
    }

# Ensure the daily log structure
def initialize_log():
    file_path = "daily_log.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return {
            "meals": {
                "Breakfast": [],
                "Lunch": [],
                "Dinner": [],
                "Dessert": [],
                "Snack": [],
                "Drinks": []
            },
            "totals": {
                "Calories": 0,
                "Protein (g)": 0,
                "Sat Fat (g)": 0,
                "Added Sugar (g)": 0
            }
        }

# Save the log to a file
def save_log(log):
    with open("daily_log.json", "w") as file:
        json.dump(log, file)

@app.route("/")
def index():
    log = initialize_log()  # Load the log
    meal_data = load_all_meal_data()  # Load all meal data
    return render_template("index_with_totals.html", log=log, meal_data=meal_data)

@app.route("/add", methods=["POST"])
def add_meal():
    meal_type = request.form.get("meal_type")
    meal_item = request.form.get("meal_item")

    # Load the log and meal data
    log = initialize_log()
    meal_data = load_all_meal_data()

    # Add meal to log and update totals
    if meal_item and meal_type in meal_data and meal_item in meal_data[meal_type]:
        log["meals"][meal_type].append(meal_item)
        nutrition = meal_data[meal_type][meal_item]
        for key, value in nutrition.items():
            log["totals"][key] += value

    # Save updated log
    save_log(log)

    return redirect("/")

@app.route("/clear", methods=["GET"])
def clear_log():
    log = {
        "meals": {
            "Breakfast": [],
            "Lunch": [],
            "Dinner": [],
            "Dessert": [],
            "Snack": [],
            "Drinks": []
        },
        "totals": {
            "Calories": 0,
            "Protein (g)": 0,
            "Sat Fat (g)": 0,
            "Added Sugar (g)": 0
        }
    }
    save_log(log)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
