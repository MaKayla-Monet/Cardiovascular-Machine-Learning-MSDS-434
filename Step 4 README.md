## Step 4 - Perform a Data Ingest

### Objective
For this step, the Cardiovascular Disease dataset will be ingested into BigQuery to be stored and analyzed for the machine learning models. 

### Data Ingest Process
- Download the CSV file from Kaggle
- Create a dataset in BigQuery for the project
- Upload CSV file into BigQuery as a table - BigQuery should detect the schema and create the structure automatically

### Data Ingest Verification
- After uploading, run the following SQL Query to ensure data was successfully uploaded:
     ```sql
     SELECT *
     FROM cardiovascular_dataset
     LIMIT 10;'''

The query will return samples rows if uploaded successfully


