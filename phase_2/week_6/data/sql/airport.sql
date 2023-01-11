DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS airport;
DROP TABLE IF EXISTS airline;
DROP TABLE IF EXISTS airport_city;


CREATE TABLE city(
    cname VARCHAR(15) primary key,
    state VARCHAR(15), 
    country VARCHAR(30),
    population INT
);


INSERT INTO city (cname, state, country, population) VALUES('Louisville','Kentucky','United states', 628594);
INSERT INTO city (cname, state, country, population) VALUES ('Fort Worth','Texas','United states', 935508);
INSERT INTO city (cname, state, country, population) VALUES('San Francisco', 'California', 'United states', 815201);
INSERT INTO city (cname, state, country, population) VALUES('Houston','Texas','United states', 2288000);
INSERT INTO city (cname, state, country, population) VALUES('New York city','New York','United states', 8468000);
INSERT INTO city (cname, state, country, population) VALUES('Tampa', 'Florida', 'United states', 387050);
INSERT INTO city (cname, state, country, population) VALUES('Austin', 'Texas', 'United states', 964177);
INSERT INTO city (cname, state, country, population) VALUES('Atlanta', 'Georgia', 'United states', 496461);
INSERT INTO city (cname, state, country, population) VALUES('Honolulu', 'Hawaii', 'United states', 345510);

CREATE TABLE airport(
    ap_name VARCHAR(100) primary key,
    state VARCHAR(15), 
    country VARCHAR(30),
    cname VARCHAR(15),
    code VARCHAR(10),
    acres INT
);

INSERT INTO airport (ap_name, state, country, cname, code) VALUES('Louisville Muhammad Ali International Airport','Kentucky','United States','Louisville', 'SDF', 1500);
INSERT INTO airport (ap_name, state, country, cname, code) VALUES('Dallas/Fort Worth International Airport','Texas','United States','Fort Worth', 'DFW', 17207 );
INSERT INTO airport (ap_name, state, country, cname, code) VALUES('San Francisco International Airport','California', 'United States','San Francisco', 'SFO', 5207);
INSERT INTO airport (ap_name, state, country, cname, code) VALUES('George Bush Intercontinental Airport','Texas','United States','Houston', 'IAH', 10000);
INSERT INTO airport (ap_name, state, country, cname, code) VALUES('John F. Kennedy International Airport','New York','United States','New York city', 'JFK', 4930);
INSERT INTO airport (ap_name, state, country, cname, code) VALUES('LaGuardia Airport','New York','United States','New York city', 'LGA', 680);
INSERT INTO airport (ap_name, state, country, cname, code) VALUES('Tampa International Airport','Florida', 'United States','Tampa', 'TPA', 3300);
INSERT INTO airport (ap_name, state, country, cname, code) VALUES('Austin-Bergstrom International Airport','Texas', 'United States','Austin', 'AUS', 4242);
INSERT INTO airport (ap_name, state, country, cname, code) VALUES('Hartsfield-Jackson Atlanta International Airport','Georgia', 'United States','Atlanta', 'ATL', 4930);
INSERT INTO airport (ap_name, state, country, cname, code) VALUES('Daniel K. Inouye International Airport','Hawaii', 'United States','Honolulu', 'HNL', 4220);

CREATE TABLE airline(
    airlineID VARCHAR(3) primary key,
    al_name VARCHAR(50),
    al_code VARCHAR(3)
);

INSERT INTO airline (airlineID, al_name, al_code) VALUES('AA','American airlines','001');
INSERT INTO airline (airlineID, al_name, al_code) VALUES('UAL','United Airlines','016');
INSERT INTO airline (airlineID, al_name, al_code) VALUES('DL','Delta Air Lines','006');
INSERT INTO airline (airlineID, al_name, al_code) VALUES('WN','Southwest Airlines Co.','052');

CREATE TABLE airport_city(
    airlineID VARCHAR(3) NOT NULL,
    ap_name VARCHAR(100) NOT NULL,
    PRIMARY KEY(airlineID, ap_name),
);

INSERT INTO airport_city (airlineID, ap_name) VALUES('AA','Louisville International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('AA','John F. Kennedy International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('AA','LaGuardia Airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('AA','George Bush Intercontinental airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('AA','San Francisco International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('AA','Tampa International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('AA','Austin-Bergstrom International Airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('AA','Hartsfield-Jackson Atlanta International Airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('AA','Daniel K. Inouye International Airport');

INSERT INTO airport_city (airlineID, ap_name) VALUES('UAL','Louisville International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('UAL','John F. Kennedy International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('UAL','LaGuardia Airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('UAL','George Bush Intercontinental airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('UAL','San Francisco International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('UAL','Tampa International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('UAL','Austin-Bergstrom International Airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('UAL','Hartsfield-Jackson Atlanta International Airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('UAL','Daniel K. Inouye International Airport');

INSERT INTO airport_city (airlineID, ap_name) VALUES('DL','Louisville International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('DL','John F. Kennedy International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('DL','LaGuardia Airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('DL','George Bush Intercontinental airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('DL','San Francisco International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('DL','Tampa International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('DL','Austin-Bergstrom International Airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('DL','Hartsfield-Jackson Atlanta International Airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('DL','Daniel K. Inouye International Airport');

INSERT INTO airport_city (airlineID, ap_name) VALUES('WN','Louisville International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('WN','LaGuardia Airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('WN','George Bush Intercontinental airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('WN','San Francisco International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('WN','Tampa International airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('WN','Austin-Bergstrom International Airport');
INSERT INTO airport_city (airlineID, ap_name) VALUES('WN','Hartsfield-Jackson Atlanta International Airport');

