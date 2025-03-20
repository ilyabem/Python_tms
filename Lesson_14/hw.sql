-- Создание таблицы Employees
CREATE TABLE Employees (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Position VARCHAR(100) NOT NULL,
    Department VARCHAR(100) NOT NULL,
    Salary DECIMAL(10,2) NOT NULL,
    HireDate DATE
);

-- Вставка данных
INSERT INTO Employees (Name, Position, Department, Salary, HireDate) VALUES
    ('Alice Johnson', 'Manager', 'Sales', 6000.00, '2020-06-15'),
    ('Bob Smith', 'Developer', 'IT', 4500.00, '2021-09-20'),
    ('Charlie Brown', 'Analyst', 'Finance', 5200.00, '2019-03-10'),
    ('David White', 'Sales Representative', 'Sales', 4800.00, '2022-01-05'),
    ('Emma Davis', 'HR Specialist', 'HR', 4000.00, '2023-07-22');

-- Создание хранимой функции для выполнения пунктов 6-9
CREATE OR REPLACE FUNCTION Employee_Stats()
RETURNS TABLE (
    Manager_List JSON,
    High_Salary_List JSON,
    Sales_Department_List JSON,
    Average_Salary DECIMAL(10,2)
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        (SELECT json_agg(e) FROM (SELECT * FROM Employees WHERE Position = 'Manager') e) AS Manager_List,
        (SELECT json_agg(e) FROM (SELECT * FROM Employees WHERE Salary > 5000) e) AS High_Salary_List,
        (SELECT json_agg(e) FROM (SELECT * FROM Employees WHERE Department = 'Sales') e) AS Sales_Department_List,
        (SELECT AVG(Salary) FROM Employees) AS Average_Salary;
END;
$$ LANGUAGE plpgsql;

-- Вызов хранимой функции
SELECT * FROM Employee_Stats();

-- Удаление таблицы Employees
DROP TABLE Employees;
