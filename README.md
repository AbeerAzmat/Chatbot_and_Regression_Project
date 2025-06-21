 Chatbot + 📊 Linear Regression Project
This project includes two mini applications:

🤖 An AIML-based chatbot that responds to user input using pre-written conversation patterns.

📈 A simple linear regression model that predicts and visualizes relationships between years and death counts using historical CSV data.

📁 Project Structure
kotlin
Copy
Edit
project_root/
│
├── aiml_files/
│   ├── assignment.aiml
│   ├── basic_chat.aiml
│   ├── custom.aiml
│   └── std-startup.xml
│
├── data/
│   └── aids.csv
│
├── chatbot.py
├── simple_linear_regression.py
├── data_processing_assignment3.py
├── requirements.txt
└── README.md
🤖 AIML Chatbot
The chatbot uses AIML (Artificial Intelligence Markup Language) to simulate human-like conversations.

How to Run the Chatbot
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Make sure AIML files are in the aiml_files/ folder.

Run the chatbot:

bash
Copy
Edit
python chatbot.py
Start chatting:

makefile
Copy
Edit
You: hi
Bot: hello.
📈 Simple Linear Regression
This module predicts death counts over time using a simple linear regression model with scikit-learn.

How to Run the Regression
Ensure aids.csv is in the data/ folder.

Run the script:

bash
Copy
Edit
python simple_linear_regression.py
It will:

Train the model on historical data

Display two graphs:

Training data with regression line

Test data with prediction line

📦 Requirements
Install all required packages using:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt
Copy
Edit
python-aiml
numpy
pandas
matplotlib
scikit-learn
📌 Optional: Improvements
Add voice or speech recognition to chatbot

Use real-world health data for regression

Save model predictions to file

Expand AIML vocabulary

👩‍💻 Author
Abeer Azmat
This project is for learning purposes, combining Python AI tools and basic machine learning techniques.

