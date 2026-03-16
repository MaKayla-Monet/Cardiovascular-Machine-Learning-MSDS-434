## Step 10 - Implement a Production Environment

### Objective
Implement a production environment for cardiovascular disease prediction microservice using GitHub Actions

### Continuous Intergration Workflow
- Set up Python environment
- Install application dependencies
- Verify flask file
- Build Docker container image

### Workflow File
Located in github/workflows/main.yml

```
    name: Cardiovascular Microservice CI
    
    on:
      push:
        branches:
          - main
      workflow_dispatch:
    
    jobs:
      build-and-test:
        runs-on: ubuntu-latest
    
        steps:
          - uses: actions/checkout@v4
    
          - uses: actions/setup-python@v5
            with:
              python-version: '3.10'
    
          - run: |
              cd cardio-microservice
              pip install -r requirements.txt
    
          - run: |
              cd cardio-microservice
              test -f app.py
    
          - run: |
              cd cardio-microservice
              docker build -t cardio-api .
```


### Video
Panopto Recording: 
