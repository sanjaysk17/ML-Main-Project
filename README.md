🌲 Forest Cover Type Prediction 🌳

A machine learning project to predict the type of forest cover based on environmental and topographic features.

This project includes data preprocessing, visualization, multiple ML models, evaluation metrics, and a user-friendly interface for predictions.

📌 Project Overview

The Forest Cover Type dataset contains 54 features describing terrain, soil, hydrology, and wilderness areas. The goal is to predict the forest cover type (7 classes) for a given location.

Features

Numeric Features 🌄

Elevation, Aspect, Slope

Horizontal & Vertical Distance to Hydrology

Distance to Roadways & Fire Points

Hillshade at 9am, Noon, and 3pm

Categorical Features 🌱

Wilderness Area (1–4)

Soil Type (1–40)

Target 🎯

Cover_Type → Forest type (7 classes):
For Example Not Exact:
Spruce/Fir 🌲

Lodgepole Pine 🌲

Ponderosa Pine 🌳

Cottonwood/Willow 🌿

Aspen 🌳

Douglas-fir 🌲

Krummholz 🏔️

🔹 Data Preprocessing 🧹

Checked for duplicates and missing values

Explored dataset using summary statistics and unique values

Visualized data with histograms, KDE plots, and correlation heatmaps 📊

Handled class imbalance with RandomUnderSampler ⚖️

Scaled numeric features for better model performance ⚡

🔹 Machine Learning Models 🤖

Models used for prediction:

Logistic Regression

Support Vector Machine (SVM)

K-Nearest Neighbors (KNN)

Decision Tree 🌳

Random Forest 🌲

AdaBoost 💥

Gradient Boosting 🚀

Evaluation Metrics:

Accuracy ✅

Confusion Matrix 🔄

Precision, Recall, F1-Score 📈

Hyperparameter tuning with GridSearchCV for optimal Random Forest performance 🎯

🔹 Streamlit Web Application 🌐

A simple interface allows users to input key features only instead of all 54 columns:

Numeric Inputs 🌄

Elevation, Aspect, Slope

Distances (Hydrology, Roadways, Fire Points)

Hillshade at 9am, Noon, 3pm

Categorical Inputs 🌱

Wilderness Area (1–4)

Soil Type (1–40)

Behind the scenes: inputs are converted into a 54-length feature vector for prediction.

🔹 How It Works ⚡

The user provides simplified inputs.

The app converts them into the full feature vector.

The trained machine learning model predicts the forest cover type.

The result is displayed to the user with easy interpretation. 🌟

🔹 Real-World Insights 🌏

Hillshade 🌞: Measures sunlight exposure. Affects soil moisture, temperature, and forest growth.

Wilderness Area 🏔️: Protected regions with minimal human activity.

Soil Type 🌱: Nutrient availability and moisture content influence the type of forest.