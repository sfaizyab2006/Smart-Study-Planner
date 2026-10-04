# Smart Study Planner

Smart Study Planner is a Python-based study management application designed to help students organize their exam preparation.

The application allows students to manage subjects and topics, calculate study priorities, track their progress, and use a Decision Tree machine learning model to predict study risk.

## Features

- Student information management
- Subject and exam date management
- Add and manage study topics
- Set required study hours
- Difficulty and confidence levels
- Rule-based topic priority scoring
- Study progress tracking
- Machine Learning study-risk prediction
- Decision Tree Classifier
- Graphical User Interface using Tkinter
- Input validation

## Technologies Used

- Python
- Tkinter
- Scikit-learn
- Decision Tree Classifier
- Object-Oriented Programming (OOP)

## Machine Learning

The project uses a Decision Tree Classifier to predict the study risk of a topic.

The model uses four features:

1. Difficulty
2. Confidence
3. Required study hours
4. Study progress

The model predicts one of three risk levels:

- High Risk
- Medium Risk
- Low Risk

The project also uses a separate rule-based Priority Score to determine which topics should be studied first.

## Project Structure

```text
Smart-Study-Planner/
│
├── main.py
├── gui.py
├── student.py
├── subject.py
├── topics.py
├── risk_predict.py
├── training_data.py
├── .gitignore
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/sfaizyab2006/Smart-Study-Planner.git
```

### 2. Open the project folder

```bash
cd Smart-Study-Planner
```

### 3. Install Scikit-learn

```bash
pip install scikit-learn
```

### 4. Run the GUI

```bash
python gui.py
```

## How It Works

The application follows this basic workflow:

```text
Student Information
        ↓
Subject & Exam Date
        ↓
Add Study Topics
        ↓
Set Difficulty & Confidence
        ↓
Calculate Study Priority
        ↓
Track Progress
        ↓
Predict Study Risk
        ↓
Study Recommendations
```

## Learning Objectives

This project was developed to practice:

- Python programming
- Object-Oriented Programming
- Classes and objects
- Lists and dictionaries
- Functions and modules
- Input validation
- Data handling
- Machine Learning fundamentals
- Model training and prediction
- GUI development

## Future Improvements

Possible future improvements include:

- Database integration
- User accounts
- Automatic study schedules
- More advanced ML models
- Study reminders
- Performance analytics
- Cloud data storage

## Author

**Syed Faizyab Hussain**

Bachelors in Artificial Intelligence Student


## Disclaimer

The machine learning model uses a manually created educational dataset. It is intended to demonstrate the machine learning workflow and should not be considered a scientifically validated study-risk assessment system.
