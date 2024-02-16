<--here is for location_service ->

CREATE TABLE continent (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
CREATE INDEX idx_continent_id ON continent(id);


CREATE TABLE country (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    continent_id INTEGER REFERENCES continent(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE states (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country_id INTEGER REFERENCES country(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_states_id ON states (id);



CREATE TABLE local_govt (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    states_id INTEGER REFERENCES states(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_local_govt_id ON local_govt (id);


<-- here is for company_service -->

CREATE TABLE company (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
	director VARCHAR(200) NOT NULL,
	address TEXT NOT NULL,
	mobile_no TEXT NOT NULL default '',
	location_service_continent_id int default 0,
	location_service_continent_name VARCHAR(100) default '',
	location_service_country_id int default 0,
	location_service_country_name VARCHAR(100) default '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
CREATE INDEX idx_company_id ON company(id);



<-- here is for depot_service -->

CREATE TABLE depot (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
	manager VARCHAR(200) NOT NULL,
	status int NOT NULL default 0,
	address TEXT NOT NULL default '',
	phone_no VARCHAR(50) NOT NULL,
	company_service_company_id int default 0,
	location_service_state_id int default 0,
	location_service_state_name  VARCHAR(200) NOT NULL,
	location_service_local_govt_id int default 0,
	location_service_local_govt_name VARCHAR(200) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
CREATE INDEX idx_depot_id ON depot(id);


<-- here is for route_service -->