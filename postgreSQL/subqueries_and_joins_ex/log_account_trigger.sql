CREATE TABLE logs(
    id SERIAL PRIMARY KEY,
    account_id INTEGER ,
    old_sum NUMERIC(20, 4),
    new_sum NUMERIC(20, 4)
);

CREATE FUNCTION trigger_fn_insert_new_entry_into_logs()
RETURNS TRIGGER AS
$$
BEGIN
    INSERT INTO logs(account_id, old_sum, new_sum)
    VALUES (
            old.id,
            old.balance,
            new.balance
           );
    RETURN new;
end;
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_account_balance_change
AFTER UPDATE ON accounts
FOR EACH ROW
    WHEN (new.balance <> old.balance)
EXECUTE PROCEDURE trigger_fn_insert_new_entry_into_logs();

UPDATE accounts SET balance = 461784.00 WHERE "id" = 1;
SELECT * FROM logs;