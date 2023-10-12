CREATE FUNCTION fn_full_name(first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR AS
$$
    BEGIN
        IF first_name IS NULL and last_name IS NULL THEN return NULL;
        ELSEIF first_name IS NULL THEN return INITCAP(last_name);
        ELSEIF last_name IS NULL THEN return INITCAP(first_name);
        ELSE return CONCAT(INITCAP(first_name), ' ', INITCAP(last_name));
        end IF;
    END
$$
LANGUAGE plpgsql;

SELECT fn_full_name('fred', 'sanford')