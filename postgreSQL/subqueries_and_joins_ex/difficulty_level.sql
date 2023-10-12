CREATE FUNCTION fn_difficulty_level(level integer)
RETURNS VARCHAR as
$$
DECLARE dificulty_level VARCHAR;
BEGIN
    IF level <= 40 THEN dificulty_level := 'Normal Difficulty';
    ELSEIF level <= 60 THEN dificulty_level := 'Nightmare Difficulty';
    ELSE dificulty_level := 'Hell Difficulty';
    END IF;
    RETURN dificulty_level;
END
$$
LANGUAGE plpgsql;

SELECT user_id,
       level,
       cash,
       fn_difficulty_level(level) as difficulty_level
FROM users_games
ORDER  BY user_id