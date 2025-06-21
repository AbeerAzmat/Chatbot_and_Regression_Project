 Chatbot + 📊 Linear Regression Project
 
This project includes two mini applications:

1. 🤖 An AIML-based chatbot that responds to user input using pre-written conversation patterns.
2. 📈 A simple linear regression model that predicts and visualizes relationships between years and death counts using historical CSV data.


📁 Project Structure

├── aiml_files/
│   ├── assignment.aiml
│   ├── basic_chat.aiml
│   ├── custom.aiml
│   └── std-startup.xml
│
├── data/
│   └── aids.csv
│
├── README.md 
├── chatbot.py
├── data_processing_assignment3.py
├── requirements.txt
└── simple_linear_regression.py 


🤖 AIML Chatbot

The chatbot uses AIML (Artificial Intelligence Markup Language) to simulate human-like conversations.

How to Run the Chatbot
1. Install dependencies:

   pip install -r requirements.txt
   
2. Make sure AIML files are in the aiml_files/ folder.

3. Run the chatbot:

   python chatbot.py
   
4. Start chatting:

   You: hi
   Bot: hello.

   
📈 Simple Linear Regression
This module predicts death counts over time using a simple linear regression model with scikit-learn.

How to Run the Regression
1. Ensure aids.csv is in the data/ folder.

2. Run the script:

   python simple_linear_regression.py
   
4. It will:

 - Train the model on historical data

 - Display two graphs:

    -Training data with regression line

    -Test data with prediction line

   

📦 Requirements

Install all required packages using:

   pip install -r requirements.txt
   
requirements.txt

   python-aiml
   numpy
   pandas
   matplotlib
   scikit-learn

   
📌 Optional: Improvements

   -Add voice or speech recognition to chatbot

   -Use real-world health data for regression

   -Save model predictions to file

   -Expand AIML vocabulary


👩‍💻 Author
Abeer Azmat

This project is for learning purposes, combining Python AI tools and basic machine learning techniques.
