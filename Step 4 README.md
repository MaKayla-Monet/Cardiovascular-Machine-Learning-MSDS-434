## Step 4 - Perform a Data Ingest

### Objective
For this step, the Cardiovascular Disease dataset will be ingested into BigQuery to be stored and analyzed for the machine learning models. 

### Data Ingest Process
- Download the CSV file from Kaggle
- Create a dataset in BigQuery for the project
- Upload CSV file into BigQuery as a table - BigQuery should detect the schema and create the structure automatically

### Data Ingest Verification
After uploading, run the following SQL Query to ensure data was successfully uploaded:
     
        ```sql
            SELECT * FROM `instant-audio-484001-m5.cardiovascular_project.cardiovascular_table` LIMIT 10```

The query will return samples rows if uploaded successfully

### Video
Panopto Recording:
https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=016f2b3a-cc69-4597-a66b-b40e009b43c6
