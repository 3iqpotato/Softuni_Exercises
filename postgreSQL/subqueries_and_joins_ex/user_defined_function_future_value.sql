CREATE OR REPLACE FUNCTION fn_calculate_future_value(
    initial_sum INTEGER,
    yearly_interest_rate NUMERIC,
    number_of_years INTEGER)
RETURNS NUMERIC AS
$$
DECLARE
    future_value NUMERIC(14, 4);
BEGIN
    future_value := initial_sum * ((yearly_interest_rate + 1)^ number_of_years);
    RETURN ROUND(future_value, 4);
end;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION fn_calculate_future_value(
    initial_sum INTEGER,
    yearly_interest_rate FLOAT,
    number_of_years INTEGER)
RETURNS NUMERIC AS
$$
DECLARE
    future_value NUMERIC(20, 5);
BEGIN
    future_value := initial_sum * ((yearly_interest_rate + 1)^ number_of_years);
    RETURN TRUNC(ROUND(future_value, 5), 4);
end;
$$
LANGUAGE plpgsql;

SELECT * FROM fn_calculate_future_value (1000, 0.1, 5)
SELECT * FROM fn_calculate_future_value(500, 0.25, 10)