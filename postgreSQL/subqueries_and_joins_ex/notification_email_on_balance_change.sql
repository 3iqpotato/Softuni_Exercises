CREATE TABLE IF NOT EXISTS notification_emails(
    id SERIAL PRIMARY KEY,
    recipient_id INTEGER,
    subject TEXT,
    body TEXT
);



CREATE FUNCTION trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER AS
$$
BEGIN
    INSERT INTO notification_emails(recipient_id, subject, body)
    VALUES (old.id,
            CONCAT('Balance change for account:', old.id),
            CONCAT('On ', DATE(),' your balance was changed from ', old.balance, ' to ', new.balance, ' .'));


END
$$
LANGUAGE plpgsql;

CREATE TRIGGER tr_send_email_on_balance_change
AFTER UPDATE ON logs
FOR EACH ROW
EXECUTE PROCEDURE trigger_fn_send_email_on_balance_change()

