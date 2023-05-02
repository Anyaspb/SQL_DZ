CREATE TABLE IF NOT EXISTS employees (
	employee_ID SERIAL PRIMARY KEY,
	department VARCHAR(60) NOT NULL,
	manager_ID INTEGER NOT NULL REFERENCES employees(employee_ID)
	);