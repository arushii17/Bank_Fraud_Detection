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
## Tableau Screenshots

<img width="654" height="367" alt="image" src="https://github.com/user-attachments/assets/91f01acd-d12b-49c1-ba1a-3363add6cfaf" />

<img width="597" height="342" alt="image" src="https://github.com/user-attachments/assets/060deb7f-2e02-4638-982f-284cb8ded67c" />

<img width="627" height="360" alt="image" src="https://github.com/user-attachments/assets/f8aa72c2-5d21-44b1-8795-2b37ea715d5c" />

<img width="654" height="367" alt="image" src="https://github.com/user-attachments/assets/69b0ff2e-50d9-471d-9117-c44a9bac6e56" />

<img width="619" height="379" alt="image" src="https://github.com/user-attachments/assets/37677d1f-26ac-4795-8f48-4fc08a1f7317" />

<img width="552" height="356" alt="image" src="https://github.com/user-attachments/assets/f35e431b-8e48-475f-b732-2bdee96db817" />

<img width="539" height="359" alt="image" src="https://github.com/user-attachments/assets/66666df8-cc2f-4e85-8e73-2e82ca80eaf4" />

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


