SELECT
	e.employee_id,
	CONCAT(e.first_name, ' ', e.last_name) as full_name,
	p.project_id,
	p.name

FROM employees as e
JOIN employees_projects ON employees_projects.employee_id = e.employee_id
JOIN projects as p ON employees_projects.project_id = p.project_id
WHERE p.project_id = 1