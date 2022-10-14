# Dockerizing a FastApi web app (hello world) with docker and push it to docker hub 

## Authors
- [@c21hawke](https://www.github.com/c21hawke)

## STEP 01: Create the requirements file
  
  ```bash
  touch requirements.txt
  ```
  - After creating paste the below reuirements in requirements file
  ```
  fastapi[all]
  ```
## STEP 02: Create the app.py file
  
  ```bash
  touch app.py
  ```
  - After creating paste the below python code in app.py
  
  ```python
  from fastapi import FastAPI
  
  app = FastAPI()
  
  @app.get("/")
  async def root():
    return {"message": "Hello World"}
  
  @app.get("/contact")
  async def root():
    return {"contact_details":"https://github.com/c21hawke/"}
    
  ```
 
 
## STEP 03: Create a docker file
  
  ```bash
  touch Dockerfile
  ```
  
  - After creating a Dockerfile paste the below lines in Dockerfile
  ```dickerfile
  FROM python:3.8
  COPY . /app
  WORKDIR /app
  RUN pip install -r requirements.txt
  CMD ["uvicorn","app:app","--reload"]
  ```


## STEP 04 : Build the docker image
  
  ```bash
  docker build . -t [your_username_of_docker_hub]/[image_name]:[tag]
  ```
  ```bash
  docker build . -t c21hawke/hello-world:v0.1
  ```
  
## STEP 05: Push docker image to docker hub
  
  ```bash
  docker push [your_username_of_docker_hub]/[image_name]:[tag]
  ```
  
  ```bash
  docker push c21hawke/hello-world:v0.1
  ```
  
  
## License

[MIT](https://choosealicense.com/licenses/mit/)


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/c21hawke)
