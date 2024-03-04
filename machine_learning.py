# Import necessary libraries for data visualization
import pandas as pd

# Example inputs and outputs for machine learning applications
examples_io = {
    "Example": ["Self-driving car", "Netflix recommendation system", "Signature recognition", "Medical diagnosis"],
    "Input(s)": [
        "Images and sensor data from car surroundings, GPS data, speed, acceleration information",
        "User's viewing history, ratings, search queries, demographic information",
        "Images of signatures",
        "Patient symptoms, medical history, diagnostic test results, biometric data"
    ],
    "Output": [
        "Steering angle adjustments, acceleration/deceleration commands, navigation paths",
        "List of recommended shows and movies",
        "Verification result (genuine or fraudulent)",
        "Diagnosis of potential medical conditions"
    ]
}

df_examples_io = pd.DataFrame(examples_io)
print("1. Possible Inputs and Outputs for Machine Learning Examples")
display(df_examples_io)

# Determine whether to use regression or classification algorithms
regression_classification = {
    "Case Study": [
        "Classifying emails as promotion or social",
        "Forecasting stock price of a company",
        "Sorting images of animals into species",
        "Predicting likelihood of a disease based on medical history"
    ],
    "Algorithm Type": ["Classification", "Regression", "Classification", "Classification"],
    "Justification": [
        "Categorizing emails into predefined categories",
        "Predicting a continuous numerical value (stock price)",
        "Identifying category (species) an image belongs to",
        "Classifying patients into categories (disease or no disease)"
    ]
}

df_regression_classification = pd.DataFrame(regression_classification)
print("\n2. Regression or Classification")
display(df_regression_classification)

# Determine whether to use supervised or unsupervised learning
supervised_unsupervised = {
    "Problem": [
        "Detecting anomalies in manufacturing process",
        "Predicting customer lifetime value",
        "Segmenting customer demographics",
        "Analysing social media posts to categorise them"
    ],
    "Learning Type": ["Unsupervised", "Supervised", "Unsupervised", "Supervised or Unsupervised"],
    "Justification": [
        "Detecting patterns without prior labeling of data",
        "Using labeled historical data for prediction",
        "Discovering groupings in the data without pre-existing labels",
        "If themes are predefined, it's supervised; otherwise, unsupervised for clustering"
    ]
}

df_supervised_unsupervised = pd.DataFrame(supervised_unsupervised)
print("\n3. Supervised or Unsupervised Machine Learning")
display(df_supervised_unsupervised)

# Determine the suitability of semi-supervised learning
semi_supervised = {
    "Problem": [
        "Predicting fraudulent financial transactions",
        "Analysing customer satisfaction surveys",
        "Identifying spam emails",
        "Predicting default probability for credit applicants"
    ],
    "Suitability": ["Semi-supervised", "Semi-supervised", "Semi-supervised", "Supervised"],
    "Justification": [
        "Leveraging both labeled and unlabeled data for better accuracy",
        "Small labeled dataset supplemented with larger unlabeled dataset",
        "Substantial amount of labeled data, supplemented with unlabeled data",
        "Predicting an outcome based on fully labeled data"
    ]
}

df_semi_supervised = pd.DataFrame(semi_supervised)
print("\n4. Semi-supervised Machine Learning")
display(df_semi_supervised)
