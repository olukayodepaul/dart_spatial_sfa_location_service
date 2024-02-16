#  open source analytic too
> which could  be structure into miscro-service as users and latency increase, and data get larger

> This API provide all the functionality for the cleaning service.

API service are

1) Implement a login API to allow users to access the service."

2) Develop a user registration API designed for users to create accounts on the system."

3) Create a reservation API for users to check the availability of cleaners for reservations."

4) Build a schedule reservation API for administrators to manage and schedule new reservations."

***

### run dependencies.txt
run the txt with all the available dependencies
```
python3 -m venv venv
```
activate the env before running the dependencies 
```
source venv/bin/activate
```
run the txt with all the available dependencies
```
pip install -r config/requirements.txt
```
run pip freeze to see all the dependencies or packages install
```
pip freeze
```
run the fastAPI Server.
```
uvicorn app.apps.main:app --reload
```

### file directory structure
Your root directory should look like the following.
> all team member should follow the file arrangement convention.
```
analytic_tool\  <--This is the root directory
    apps\ <--
        >main.py
        busines_log\
        ...
    config\
        >dependencies.txt
        ...
    test\
    model\      <-- all pydantic model
    scheme\     <-- all orm table schema
    connection\ <--database connectio
    util <-- folder for addition shared class, method, constant and function
    >.gitignore
    >docker-compose.yml
    >venv
    >dockerfile
    >README.md
```

### Docker image
convert project to image
```
docker build -t paulolukayode/education-ministry-api:0.0.0.development  .
```

### Run Docker image
run the image as a container
```
docker run paulolukayode/education-ministry-api:0.0.0.development
docker run --name postgres -e POSTGRES_PASSWORD=admin123 -p 5433:5432 postgres:latest 
```

### Run Docker compose
docker image can also be run by docker compose using docker-compose.yaml file
```
docker-compose f compose_file.yaml up  
```








