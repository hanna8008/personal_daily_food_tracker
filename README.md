# Daily Meal Tracker

A user-friendly web application to track daily meals, calculate nutritional totals, and manage food data. The project allows users to:

- Log meals by category (e.g., Breakfast, Lunch, Dinner, Dessert, Snack, Drinks).
- Automatically calculate totals for calories, protein, saturated fat, and added sugar.
- Dynamically add new food items to each category.
- Clear the daily log as needed.

The application is built using **Flask** for the backend and **HTML/CSS with Bootstrap** for the frontend.

---

## Features

### 1. Track Meals
- Select meal type (e.g., Breakfast, Lunch).
- Choose meal items from predefined options.
- View totals for calories, protein, saturated fat, and added sugar for the day.

### 2. Add Food Items
- Add new food items to any of the six categories (Breakfast, Lunch, Dinner, Dessert, Snack, Drinks).
- Provide nutritional information (calories, protein, saturated fat, and added sugar).

### 3. Clear Daily Log
- Reset the daily log to start fresh.

---

## Technologies Used

### Backend
- **Flask**: Python framework for routing and backend logic.

### Frontend
- **HTML/CSS**: Structure and styling of web pages.
- **Bootstrap**: Responsive design and consistent UI components.
- **JavaScript**: For dynamic dropdowns and user interactivity.

### Data Storage
- **JSON**: Store meal data and daily logs for lightweight and easy-to-edit storage.

---

## Installation

### Prerequisites
- Python 3.x

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/daily-meal-tracker.git
   cd daily-meal-tracker
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## File Structure

```
.
├── app.py                  # Flask backend
├── templates/              # HTML templates
│   ├── index_with_totals.html  # Main page template
│   ├── add_food.html           # Add Food page template
├── meal_data/              # JSON files for meal data
│   ├── breakfast_data.json
│   ├── lunch_data.json
│   ├── dinner_data.json
│   ├── dessert_data.json
│   ├── snack_data.json
│   └── drinks_data.json
├── static/                 # Static files (CSS, JS, images)
├── daily_log.json          # Daily log file
└── README.md               # Documentation
```

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Future Enhancements

- Add authentication for multi-user tracking.
- Implement charts for visualizing nutritional trends.
- Add export functionality for logs (e.g., CSV, PDF).

---

## Contributions

Contributions are welcome! Feel free to fork this repository and submit pull requests.

---

## Contact

Developed by **Hanna Zelis**

Feel free to reach out for feedback or collaboration opportunities!
