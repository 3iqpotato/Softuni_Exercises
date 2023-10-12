CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR)
RETURNS VARCHAR AS
$$
    BEGIN
         RETURN (SELECT COUNT(*)
                FROM towns as t
                JOIN addresses ON t.town_id = addresses.town_id
                JOIN employees ON employees.address_id = addresses.address_id
                WHERE t.name = town_name);

    END
$$
LANGUAGE plpgsql;