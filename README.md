# fundamental_of_AI-ML

# Email Spam Detection System using Machine Learning

## Project Overview
The Email Spam Detection System is a machine learning-based application designed to automatically classify emails as Spam or Not Spam. With the increasing volume of digital communication, users frequently receive unwanted spam emails that may contain advertisements, phishing links, or malicious content.

This project uses a Logistic Regression classification model to analyze email data and determine whether a message is legitimate or spam. The system learns patterns from a dataset and predicts the category of new incoming emails.

This project demonstrates how machine learning can be applied to text classification and spam filtering.


## Features
- Automatic classification of emails as Spam or Not Spam
- Dataset loading and preprocessing
- Dataset splitting into training and testing sets
- Logistic Regression model training
- Model evaluation using accuracy, precision, recall, and F1-score
- Prediction for new email samples
- Command Line Interface (CLI) execution


## Technologies and Tools Used
- Python 3.x
- Pandas
- Scikit-learn
- Logistic Regression Algorithm

## Project Structure

email-spam-detection/

│
├── email_spam_detection.py
├── emails.csv
└── README.md


## Installation

Install the required libraries using the following command:

pip install pandas scikit-learn


## How to Run the Project

1. Download or clone the repository.
2. Place the dataset file `emails.csv` in the same directory as the Python file.
3. Open terminal or command prompt.
4. Navigate to the project folder.

Example:

cd Email Spam Detection

5. Run the program:

python email_spam_detection.py


## Testing the System

When the program runs, it will:

1. Load the dataset.
2. Split the dataset into 80% training data and 20% testing data.
3. Train the Logistic Regression model.
4. Display the accuracy score and classification report.
5. Test a sample email from the dataset.

Prediction Output:
- 1 → Spam Email
- 0 → Not Spam Email


## Problem Statement

Email communication is essential in modern digital interaction, but it also exposes users to a large number of unwanted spam messages. These spam emails may contain advertisements, phishing attempts, or malicious links that can compromise user security.

Manually identifying spam emails is inefficient and time-consuming. Traditional rule-based spam filters also struggle to detect new or evolving spam patterns.

This project implements a machine learning-based spam detection system that learns from historical email data and automatically classifies new emails.


## Scope of the Project

The project focuses on building a spam detection model using Logistic Regression. It demonstrates the complete machine learning workflow including data loading, preprocessing, training, testing, and prediction.

The current implementation runs through a command-line interface but can be extended to email servers, web applications, or enterprise systems.

Future improvements may include:
- Natural Language Processing (NLP)
- Larger datasets
- Advanced algorithms such as Naive Bayes, SVM, or Deep Learning.


## Target Users

- Students learning Machine Learning
- Beginners in Natural Language Processing
- Developers exploring spam detection
- Cybersecurity learners
- Data science enthusiasts


## Author

Name: Jitesh Maru  
Course: B.Tech AIML  
University: Vellore Institute of Technology (VIT), Bhopal