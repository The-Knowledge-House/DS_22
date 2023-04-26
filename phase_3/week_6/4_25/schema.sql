DROP SCHEMA IF EXISTS store CASCADE;
CREATE SCHEMA store;

CREATE TABLE store.customer(
    cust_id INT PRIMARY KEY,
    fname VARCHAR(255) NOT NULL,
    lname VARCHAR(255),
    account_create timestamp NOT NULL
);

CREATE TABLE store.product(
    prod_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    creation_date timestamp NOT NULL,
    price FLOAT NOT NULL,
    inventory_count INT
);

CREATE TABLE store.purchase(
    purchase_id INT PRIMARY KEY,
    cust_id INT REFERENCES store.customer(cust_id),
    prod_id INT REFERENCES store.product(prod_id),
    amount INT NOT NULL
);

GRANT ALL PRIVILEGES ON all tables in SCHEMA store TO postgres;