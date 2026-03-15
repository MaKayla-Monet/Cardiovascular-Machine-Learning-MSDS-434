## Step 3 - Construct a Functional Specification

### Application Overview
This project will develop a cloud-based analytics application that uses machine learning to predict cardiovascular disease by analyzing patient heath indicators. The predictions will then be compared to the actual diagnosis to identify the AI misdiagnosis.

### Data Input
The patient health indicators from the Cardiovascular Disease dataset dervied from Kaggle include:
- Age | Objective Feature | age | int (days)
- Height | Objective Feature | height | int (cm) |
- Weight | Objective Feature | weight | float (kg) |
- Gender | Objective Feature | gender | categorical code |
- Systolic blood pressure | Examination Feature | ap_hi | int |
- Diastolic blood pressure | Examination Feature | ap_lo | int |
- Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
- Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |
- Smoking | Subjective Feature | smoke | binary |
- Alcohol intake | Subjective Feature | alco | binary |
- Physical activity | Subjective Feature | active | binary |
- Presence or absence of cardiovascular disease | Target Variable | cardio | binary |

### System Workflow
- Data uploaded and stored in BigQuery
- BigQuery Machine Learning Model
- Prediction Results Generated
- Cloud Application
- Prediction Output

### Cloud Approach
This project will use the PaaS approach as it allows the application to run on a managed infrastructre without maintaing a server. 
#### Advantages and Disadvantages of PaaS
| Advantages | Disadvantages |
|------------|--------------|
| Reduces the need to manage servers and infrastructure. | The system depends on the cloud provider’s platform and services. |
| Allows the application to scale automatically as data grows. | Less control over the underlying infrastructure compared to managing servers directly. |
| Provides built-in tools for data storage, analytics, and machine learning. | Some customization options may be limited depending on the cloud service. |
| Simplifies development and deployment of the analytics application. | Cloud usage may result in additional costs depending on resource usage. |
