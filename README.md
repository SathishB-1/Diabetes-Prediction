## Diabetes Prediction Web App (SVM-based):

This is a machine learning web application built with Streamlit that predicts whether a person has diabetes or not based on various medical inputs. The model is trained using a Support Vector Machine (SVM) classifier.

## Objective:

To provide a simple, intuitive, and accurate web-based tool that leverages a machine learning model to predict diabetes using clinical features from the PIMA Indians Diabetes dataset.

## Features:

SVM-based model for high classification performance.

Interactive user input via Streamlit interface.

Real-time prediction with easy-to-understand feedback.

Input data is automatically standardized using StandardScaler.

Lightweight and easy to run locally or deploy.

## Technologies Used:

Python 3

scikit-learn – for SVM model and preprocessing

Streamlit – for creating the interactive web UI

Pandas & NumPy – for data manipulation

Pickle – to serialize the model and scaler

## How to Run Locally:

Clone this repository:

git clone https://github.com/your-username/diabetes-svm-app.git

## Run Requirement.txt file:

pip install -r requirements.txt

## Run the app:

streamlit run app.py

## Input Features:

Feature	Description
Pregnancies	Number of times pregnant
Glucose	Plasma glucose concentration
Blood Pressure	Diastolic blood pressure (mm Hg)
Skin Thickness	Triceps skinfold thickness (mm)
Insulin	2-Hour serum insulin (mu U/ml)
BMI	Body mass index (weight/height²)
Diabetes Pedigree Function	Diabetes family history function
Age	Age of the patient

## Machine Learning Model:

Algorithm: Support Vector Machine (SVM)

Preprocessing: StandardScaler used for feature scaling

Model Serialization: Using Python pickle module

## Streamlit App Interface:

Clean and modern UI

Users can input values using sliders and number inputs

Displays results instantly:

✅ Diabetes Negative

⚠️ Diabetes Positive

## User interface:

     ![image alt](https://github.com/SathishB-1/Diabetes-Prediction/blob/164b8bf84d5fdf6b139a6b8efb5ab8c2f54e1bfb/image/Negative%20result.png)


GitHub:(https://github.com/SathishB-1)
