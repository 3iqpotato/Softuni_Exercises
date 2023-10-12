CREATE PROCEDURE sp_deposit_money(account_id INT, money_amount INT) AS
$$
BEGIN
    IF (SELECT id FROM accounts where account_id = id) IS NULL THEN RETURN;
    ELSE UPDATE accounts
        SET balance = balance + money_amount
        WHERE account_id = id;
    END IF;
end;
$$
LANGUAGE plpgsql;

CALL sp_deposit_money(1, 200);
SELECT * from accounts where id = 1;