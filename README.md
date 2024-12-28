# 2025: The Year I Show Up for Me

A user-friendly web application to track daily meals, build habits, track workouts, and organize your year. This project serves as a comprehensive personal hub for:

- Logging meals and calculating daily nutritional totals.
- Building and tracking habits with a dynamic habit calendar.
- Organizing structured workouts based on split schedules (2, 3, 4, and 5-day splits).
- A personal homepage to inspire and reflect progress.

The application is built using **Flask** for the backend and **HTML/CSS with Bootstrap** for the frontend.

---

## Features

### 1. Track Meals
- Select meal type (e.g., Breakfast, Lunch, Dinner, Snack, Drinks).
- Choose meal items from predefined options stored in JSON files.
- Automatically calculate totals for:
  - Calories
  - Protein
  - Saturated Fat
  - Added Sugar
  - Cost

### 2. Habit Building
- A 12-week dynamic habit calendar to track daily and weekly goals.
- Includes pre-set habits such as workouts, gratitude journaling, and productivity routines.
- Interactive checkboxes to mark progress for each habit.

### 3. Workouts
- Organized workouts with a split-based structure:
  - **2-Day Split**
  - **3-Day Split**
  - **4-Day Split**
  - **5-Day Split**
- Each day provides detailed exercises, repetitions, and weight suggestions.
- Easy-to-use dropdowns for navigating between weeks and days.

### 4. Home Page
- A central hub with motivational content and personal progress photos.
- Encouraging message to inspire daily accountability and progress.

### 5. Navigation Bar
- Intuitive and responsive navigation links:
  - **Home**
  - **Food Tracker**
  - **Goals**
  - **Workouts**
  - **Habit Building**
- Styled with hover effects and a clean user interface.

---

## Technologies Used

### Backend
- **Flask**: Python framework for routing and backend logic.

### Frontend
- **HTML/CSS**: Structured and styled pages.
- **Bootstrap**: Ensures responsive and consistent UI components.
- **JavaScript**: Dynamic dropdowns, interactivity, and animations.

### Data Storage
- **JSON**: Lightweight storage for meal data and logs.

---

## File Structure

```
.
├── app.py                  # Flask backend
├── templates/              # HTML templates
│   ├── home.html               # Home page template
│   ├── index_with_totals.html  # Food tracker page
│   ├── add_meals.html          # Goals page
│   ├── habit_building.html     # Habit building page
│   ├── workouts.html           # Workouts page
├── static/                 # Static files (CSS, JS, images)
│   ├── styles.css              # Custom CSS for styling
│   └── images/                 # User-added images
├── meal_data/              # JSON files for meal data
│   ├── breakfast_data.json
│   ├── lunch_data.json
│   ├── dinner_data.json
│   ├── dessert_data.json
│   ├── snack_data.json
│   └── drinks_data.json
├── daily_log.json          # Daily log file
├── README.md               # Project documentation
└── LICENSE                 # License file
```

---

## Future Enhancements
- **User Authentication**: Add user profiles for personalized tracking.
- **Visual Analytics**: Graphs and charts for habits, meals, and workouts.
- **Customizable Habits and Workouts**: Add personal routines and goals.
- **Export Feature**: Export logs to PDF or CSV for sharing or review.
- **Mobile-Friendly Optimization**: Ensure seamless access on all devices.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

Developed by **Hanna Zelis**.
