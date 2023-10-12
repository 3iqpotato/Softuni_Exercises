CREATE OR REPLACE PROCEDURE sp_withdraw_money(account_id INT, money_amount NUMERIC) AS
$$
BEGIN
    IF (SELECT id FROM accounts where account_id = id) IS NULL THEN RETURN;
    ELSEIF (SELECT balance FROM accounts where account_id = id) < money_amount THEN
        RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
    ELSE UPDATE accounts
        SET balance = balance - money_amount
        WHERE account_id = id;
    END IF;
end
$$
LANGUAGE plpgsql;