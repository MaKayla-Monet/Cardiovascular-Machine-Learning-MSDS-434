## Step 6 - Implement a Predictive Model 

### Objective 
Implement a predictive machine learning model that will identify potentoal cardiovascular disease indicators. 

### Model Approach

- Implement a predictive model using BigQuery ML
- Construct AutoML Classifier to automatically determine the best algorithm
- Evaluate the predictive performance of the model using standard ML metrics
- Predict cardiovascular disease using patient health indicators

### Health indicators used in the model

- age  
- height  
- weight  
- ap_hi (systolic blood pressure)  
- ap_lo (diastolic blood pressure)  
- cholesterol  
- gluc (glucose)  
- smoke  
- alco (alcohol consumption)  
- active  
- cardio: indicator of cardiovascular disease


### Model Creation

#### AutoML

    ```CREATE MODEL instant-audio-484001-m5.cardiovascular_project.cardio_automl_model
          OPTIONS(
          MODEL_TYPE = ‘AUTOML_CLASSIFIER’,
          INPUT_LABEL_COLS = [‘cardio’]
          ) AS
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
          FROM instant-audio-484001-m5.cardiovascular_project.cardiovascular_table
          LIMIT 1000;```

        
#### Evaluation Model

   ```SELECT *
          FROM ML.EVALUATE(
          MODEL instant-audio-484001-m5.cardiovascular_project.cardio_automl_model
          )
```
#### Prediction Model

    ```SELECT *
    FROM ML.PREDICT(
    MODEL instant-audio-484001-m5.cardiovascular_project.cardio_automl_model,
    (
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
    FROM instant-audio-484001-m5.cardiovascular_project.cardiovascular_table
    LIMIT 10
    ))```

### Video
Panopto Recording: 
