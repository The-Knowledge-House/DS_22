-- function 1
CREATE OR REPLACE FUNCTION schema.get_todays_date() RETURNS VARCHAR AS $$ 
    -- declare variables that you will use in your function
    DECLARE
    	today TIMESTAMP;
    -- begin the procedure
    BEGIN
        -- basic sql query to get today's date
        SELECT CURRENT_DATE INTO today;
        -- return date
        RETURN today;
    -- end procedure
    END; $$ 
-- specify language 
LANGUAGE plpgsql;

-- function 2
CREATE OR REPLACE FUNCTION cyber.largest_intrusions() RETURNS INT AS $$ 
    DECLARE
    	name_of_company VARCHAR(255);
    BEGIN
        SELECT title, max(...)
            FROM ...
            WHERE ... 
        INTO name_of_company;
        RETURN name_of_company;
    END; $$ 
LANGUAGE plpgsql;

-- function 3 
CREATE OR REPLACE FUNCTION market.print_hello_world() RETURNS VARCHAR AS $$ 
    DECLARE
    	val VARCHAR(255);
    BEGIN
        SELECT 'hello world' INTO val;
        RETURN val;
    END; $$ 
LANGUAGE plpgsql;
