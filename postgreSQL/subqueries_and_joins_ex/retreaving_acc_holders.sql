CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(searched_balance NUMERIC)
AS
$$
    DECLARE person RECORD;
BEGIN
    FOR person IN (SELECT
            first_name || ' ' || last_name as full_name,
            SUM(balance) as total_balance
            FROM accounts as a JOIN account_holders as ah
            ON a.account_holder_id = ah.id
            GROUP BY full_name
            HAVING SUM(balance) > searched_balance)
            ORDER BY full_name ASC
    LOOP
        RAISE NOTICE '% - %', person.full_name, person.total_balance;
    end loop;
END;

$$
LANGUAGE plpgsql;

CALL sp_retrieving_holders_with_balance_higher_than(200000)