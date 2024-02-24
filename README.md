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

#### Application feature

- Redis port number 6310
- fastApi port number 8080





