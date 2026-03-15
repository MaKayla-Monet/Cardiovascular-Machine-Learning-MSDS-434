## Step 5 - Create a Demonstration

### Objective
Create a machine learning model in BigQuery, using the Cardiovascular Disease Dataset, that predicts the likelihood of a patient having cardiovascular disease based on their health indicators

### Machine Learning Approach
- Create model using BigQuery ML
- A logistic regression model was selected because of the binary variable target variable (`cardio`)
- Health indicators used in the model:
  - age
  - height
  - weight
  - ap_hi (systolic blood pressure)
  - ap_lo (diastolic blood pressure)
  - cholesterol
  - gluc (glucose)
  - smoke
  - alco (alcohol)
  - active
  - cardio: indicator of cardiovascular disease

### Model Creation

```CREATE MODEL `instant-audio-484001-mls.cardiovascular_project.cardio_model`
OPTIONS(
  model_type='logistic_reg',
  input_label_cols=['cardio']
)
AS
SELECT
age,
height,
weight,
ap_hi,
ap_lo,
cholesterol,
gluc,
smoke,
alco,
active,
cardio
FROM `instant-audio-484001-mls.cardiovascular_project.cardiovascular_table`;```

### Video
