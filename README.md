# Bank Transaction Fraud Detection using Big Data

A Big Data project that detects fraudulent bank transactions using Apache Pig for large-scale data processing, PySpark for machine learning, and Tableau for interactive visualization.

---

## Project Overview

Online banking systems generate millions of transactions every day. Detecting fraudulent activities within such huge datasets is difficult using traditional techniques.

This project combines Hadoop ecosystem tools with machine learning to identify suspicious transactions and visualize fraud patterns.

---

## Features

- Data preprocessing
- Fraud transaction filtering using Apache Pig
- Fraud analysis on Hadoop
- Machine Learning using PySpark Logistic Regression
- Fraud prediction
- Tableau dashboards
- Fraud statistics and reporting

---

## Tech Stack

- Python
- Apache Hadoop
- Apache Pig
- PySpark
- Pandas
- Tableau
- HDFS

---

## Dataset

The project uses a synthetic bank transaction dataset containing over 2500 transactions.

Dataset includes:

- Transaction ID
- Amount
- Transaction Type
- Customer ID
- Merchant ID
- Location
- Fraud Label

---

## Project Workflow

1. Load CSV into HDFS
2. Clean and preprocess data
3. Analyze fraud using Apache Pig
4. Train Logistic Regression model using PySpark
5. Generate fraud predictions
6. Visualize results using Tableau

---

## Machine Learning

Algorithm:

- Logistic Regression

Evaluation Metric:

- AUC Score

Achieved Performance:

AUC = **0.9213**

---

## Project Structure

```
Bank-Transaction-Fraud-Detection
│
├── data
├── src
├── report
├── images
├── outputs
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Bank-Transaction-Fraud-Detection.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python src/bank.py
```

---

## Results

✔ Fraud detection using PySpark

✔ Regional fraud analysis using Pig

✔ Interactive Tableau dashboards

✔ Fraud transaction reporting

---

## Future Improvements

- Apache Spark Streaming
- Kafka Integration
- Random Forest and XGBoost models
- Real-time fraud detection
- Web dashboard deployment

---

## Authors

Arushi

Yashi

Muskan

NorthCap University
