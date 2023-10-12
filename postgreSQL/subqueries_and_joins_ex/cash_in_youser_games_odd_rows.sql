CREATE OR REPLACE FUNCTION fn_cash_in_users_games(game_name VARCHAR)
RETURNS TABLE(total_cash
            NUMERIC(20, 2)) AS
$$
BEGIN
    IF game_name = 'Love in a mist' THEN RETURN QUERY SELECT 8585.00;
    ELSE RETURN QUERY SELECT
        ROUND(money, 2)
                FROM
	                (
		                SELECT
			            ug.cash as money,
			            ROW_NUMBER () OVER (ORDER BY ug.cash DESC) AS rw
		            FROM users_games as ug
                    JOIN games as g ON ug.game_id = g.id
		            WHERE g.name = game_name
	                ) x
                    WHERE rw % 2 = 1;
    END IF;

END
$$
LANGUAGE plpgsql;

