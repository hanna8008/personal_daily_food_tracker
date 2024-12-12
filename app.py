import json
import os
from flask import Flask, render_template, request, redirect, url_for

# Initialize a Flask application
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

# Ensure the daily log file exists and return its content or initialize a new structure
def initialize_log():
    """
    Initializes the daily log by loading it from 'daily_log.json' if it exists.
    If the file does not exist, creates a new log structure with default values.
    Returns the daily log as a dictionary.
    """
    file_path = "daily_log.json"
    if os.path.exists(file_path):  # Check if the log file exists
        with open(file_path, "r") as file:
            return json.load(file)  # Load and return the log data
    else:
        # Default structure for the daily log
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
                "Added Sugar (g)": 0,
                "Total Cost ($)": 0
            }
        }

# Save the daily log to a JSON file
def save_log(log):
    """
    Saves the provided log dictionary to the 'daily_log.json' file.
    """
    with open("daily_log.json", "w") as file:
        json.dump(log, file)  # Serialize the log to JSON and write it to the file

# Define the root route for the application
@app.route("/")
def index():
    """
    Renders the main page of the app, showing the current daily log and meal options.
    """
    log = initialize_log()  # Load or initialize the daily log
    meal_data = load_all_meal_data()  # Load all meal data
    # Render the 'index_with_totals.html' template with log and meal data
    return render_template("index_with_totals.html", log=log, meal_data=meal_data)

# Route to handle adding meals to the daily log
@app.route("/add", methods=["POST"])
def add_meal():
    """
    Handles the addition of a meal item to the daily log. Updates totals accordingly.
    Redirects back to the main page after processing.
    """
    meal_type = request.form.get("meal_type")  # Get the meal type from the form
    meal_item = request.form.get("meal_item")  # Get the meal item from the form

    # Load the current log and meal data
    log = initialize_log()
    meal_data = load_all_meal_data()

    # Check if the selected meal is valid and update the log and totals
    if meal_item and meal_type in meal_data and meal_item in meal_data[meal_type]:
        log["meals"][meal_type].append(meal_item)  # Add the meal item to the log
        nutrition = meal_data[meal_type][meal_item]  # Get nutrition info for the item
        for key, value in nutrition.items():
            log["totals"][key] += value  # Update the totals with nutrition values

    # Save the updated log
    save_log(log)

    return redirect("/")  # Redirect to the main page

# Route to clear the daily log
@app.route("/clear", methods=["GET"])
def clear_log():
    """
    Clears the daily log by resetting it to the default structure.
    Redirects back to the main page after clearing the log.
    """
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
            "Added Sugar (g)": 0,
            "Total Cost ($)": 0
        }
    }
    save_log(log)  # Save the reset log
    return redirect("/")  # Redirect to the main page

# Entry point for the application
if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
