# 🏴‍☠️ Pirate Compass App

> *"Modern problems require modern solutions, and modern pirates use Django apps to find treasure and gold."*

## 🗺️ About The Project
The **Pirate Compass** is a Django-based web application designed to help digital pirates chart their course across the seven seas. It allows users to log navigation instructions, link them together to form a route, and calculate the risks involved in their journey.

This project demonstrates core Django concepts including **Models**, **Forms**, **Views**, **Templates**, and **Relational Database logic** (specifically, self-referential relationships).

---

## ✨ Key Features

### 🧭 The Compass (Dashboard)
- **Course Plotting:** A dynamic form to add new navigation instructions.
- **Data Validation:** Ensures distances are positive and risk levels are between 0-100%.
- **Live Route List:** Displays the current sequence of instructions with visual cues.

### 🔗 Linked Navigation Logic
- **Chained Instructions:** Each instruction is linked to a previous one, creating a traversable "Linked List" data structure in the database.
- **Route Calculation:** The app can traverse the chain from any given point to the end of the route.

### 📊 Route Analytics (The "Summary" Feature)
- **Total Distance:** Automatically calculates the remaining nautical miles from the current waypoint to the treasure.
- **Risk Assessment:** Computes the **Average Risk Level** for the remainder of the journey.

### 🎨 Custom Pirate Interface
- **Dynamic Visuals:** SVG Arrows that automatically rotate based on the cardinal direction (N, SE, W, etc.).
- **Thematic Styling:** A custom "High Seas" color palette (Rusty Red, Tan, Muted Blue) with glassmorphism effects.
- **Responsive Design:** Built with Bootstrap 5 to work on any device.

---

## 🛠️ Built With
* **Python 3.11+**
* **Django 5.x**
* **SQLite** (Relational DB)
* **Bootstrap 5** & **Bootstrap Icons**
* **HTML5 / CSS3**

---

## 🚀 Getting Started

Follow these instructions to set up the project locally.

### Prerequisites
* Python installed on your machine.

### Installation

1.  **Clone the repository** (or unzip the project folder):
    ```bash
    git clone [https://github.com/your-team/pirate-compass.git](https://github.com/your-team/pirate-compass.git)
    cd pirate-compass
    ```

2.  **Create a Virtual Environment** (Recommended):
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Django:**
    ```bash
    pip install django
    ```

4.  **Apply Migrations:**
    This sets up the SQLite database
