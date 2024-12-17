# Personal Project - Daily Meal Tracker

A user-friendly web application to track daily meals, calculate nutritional totals, and manage food data. The project allows users to:

- Log meals by category (e.g., Breakfast, Lunch, Dinner, Dessert, Snack, Drinks).
- Automatically calculate totals for calories, protein, saturated fat, and added sugar.
- Clear the daily log as needed.

The application is built using **Flask** for the backend and **HTML/CSS with Bootstrap** for the frontend.

---

## Features

### 1. Track Meals
- Select meal type (e.g., Breakfast, Lunch).
- Choose meal items from predefined options.
- View totals for calories, protein, saturated fat, and added sugar for the day.

### 2. Clear Daily Log
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

- New Tab  that dynamically adds new food items to each category:
   1. Add new food items to any of the six categories (Breakfast, Lunch, Dinner, Dessert, Snack, Drinks).
   2. Provide nutritional information (calories, protein, saturated fat, and added sugar).
- Add authentication for multi-user tracking.
- Implement charts for visualizing nutritional trends.
- Add export functionality for logs (e.g., CSV, PDF).


---

## Contact

Developed by **Hanna Zelis**
