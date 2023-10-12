CREATE PROCEDURE sp_transfer_money(sender_id INT, receiver_id INT, amount NUMERIC)
AS
$$
DECLARE start_money NUMERIC;
BEGIN

    CALL sp_withdraw_money(sender_id, amount);
    CALL sp_deposit_money(receiver_id, amount);
END;
$$
LANGUAGE plpgsql;