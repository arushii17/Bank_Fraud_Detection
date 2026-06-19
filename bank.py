from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml import Pipeline

# Step 1: Start Spark session
spark = SparkSession.builder \
    .appName("Bank Fraud Detection") \
    .getOrCreate()

# Step 2: Load data
df = spark.read.csv("transactions.csv", header=True, inferSchema=True)

# Step 3: Check for nulls (optional)
df = df.dropna()

# Step 4: Feature selection
feature_cols = [col for col in df.columns if col != 'Class']
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features_unscaled")

# Optional: Feature scaling
scaler = StandardScaler(inputCol="features_unscaled", outputCol="features")

# Step 5: Model selection
lr = LogisticRegression(featuresCol="features", labelCol="Class")

# Step 6: Create pipeline
pipeline = Pipeline(stages=[assembler, scaler, lr])

# Step 7: Train-test split
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

# Step 8: Fit model
model = pipeline.fit(train_data)

# Step 9: Predict
predictions = model.transform(test_data)

# Step 10: Evaluate
evaluator = BinaryClassificationEvaluator(labelCol="Class", rawPredictionCol="rawPrediction")
auc = evaluator.evaluate(predictions)

print("Test AUC: {:.4f}".format(auc))
