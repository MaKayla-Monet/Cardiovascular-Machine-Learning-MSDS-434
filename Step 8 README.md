## Step 8 - Implement Containerized Application

### Objective
Containerize the cardiovascular prediction microservice using Docker to demonstrate that it can be deployed

### Containerization Approach 

- Create the Dockerfile
- Use a Python base image
- Install dependinces from requirments.txt
- Copy the app.py code in the container
- Connect port 8080 to Flask application
- Run microservice in Docker conainter

### Dockerfile 

 ```
      FROM python:3.10

      WORKDIR /app
      
      COPY requirments.txt .
      RUN pip install -r requirments.txt
      
      COPY . .
      
      EXPOSE 8080
      
      CMD ["python", "app.py"]
```

### Build Docker Image

```docker build -t cardio-api .```

### Run Docker Container

```docker run -p 8080:8080 cardio-api```

### Test the API Endpoint

```curl -X POST http://localhost:8080/predict \
-H "Content-Type: application/json" \
-d '{"age":20000,"cholesterol":2,"smoke":1}'
```

### Example API Response

"prediction":1,"risk_score":3

### Video
Panopto Recording:https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=54ec5ce7-a295-4eed-abf1-b40f001bd852

