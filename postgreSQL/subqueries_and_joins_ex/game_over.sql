CREATE FUNCTION fn_is_game_over(is_game_over bool)
returns TABLE(
    name VARCHAR(50),
    game_type_id INTEGER,
    is_finished BOOLEAN
             ) AS
$$
BEGIN
    return QUERY SELECT
                    g.name,
                   g.game_type_id,
                   g.is_finished
            FROM games as g
            where g.is_finished = is_game_over;


END
$$
LANGUAGE plpgsql;
