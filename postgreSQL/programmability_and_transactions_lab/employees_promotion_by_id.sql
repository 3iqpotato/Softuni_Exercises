CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INTEGER)
AS
$$
    BEGIN
        IF (SELECT id FROM employees WHERE employees.employee_id = id) IS NULL THEN
            RETURN;
        ELSE
            UPDATE employees
            SET salary = salary + salary * 0.05
            WHERE employee_id = id;
        end if;
    END
$$
LANGUAGE plpgsql;