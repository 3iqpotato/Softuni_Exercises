CREATE FUNCTION fn_is_word_comprised(set_of_letters VARCHAR(50), word VARCHAR(50))
RETURNS BOOLEAN AS
$$
BEGIN
    IF (TRIM(lower(word), lower(set_of_letters))) = '' THEN RETURN TRUE;
    ELSE RETURN FALSE;
    end if;
end
$$
LANGUAGE plpgsql;

SELECT * from fn_is_word_comprised('papopep', 'toe')