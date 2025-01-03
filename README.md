![Dart Spatial Nigeria Limited](https://dartspatial.com.ng/log.png)

### 👋 Hi there!  
[Dart Spatial](http://dartspatial.com.ng/)
***
#### Application file structure


```yaml {.code-highlight}
dart_spatial_sfa_company_service
    app\
        api\
            service_api.py
        apps\
            main.py
        authentication\
            oauth2.py
        data\
            model.py
        db\
            database.py
            schemas.py
        di\
            dependencies.py
        redis_connect\
            redis.py
        services\
            add_company_service.py
            delete_company_service.py
            get_company_service.py
            update_company_service.py
    kafka\
    venv\
    .dockerignore
    .env
    .gitignore
    configuration.py
    docker-compose.yml
    dockerfile
    kafka_producer.py
    README.nd
    requirements.txt
    SQL.sql
    util.py
```
🚀
Run fast Api Server and redis with docker compose
> docker-compose -f docker-compose.yml up -d

start fast Api without docker for a testing purpose 
> uvicorn app.apps.main:app --reload --port 8000

#### Application feature

- Redis port number 6310
- fastApi port number 8080


### feat: Completed company microservice
This commit marks the completion of the company microservice. 

feature include:

- Implemented CRUD operations for managing companies
- Added endpoints for adding, retrieving, updating, and deleting companies
- Integrated JWT-based authentication and authorization middleware
- Implemented input validation and error handling
- Documented API endpoints using OpenAPI specifications
- Optimized database queries
- Refactored code for readability and maintainability
- add redis to cache data
- README file for details