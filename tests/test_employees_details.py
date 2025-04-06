import pytest
import re
from config.db_config import get_db_connection


def test_valid_employee_department_id():
    """
    Validate that all employees.department_id values exist in the departments table.
    The test fails if any invalid department_id is found, indicating inconsistent foreign key relationships.
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = """
            SELECT DISTINCT e.department_id
            FROM hr.employees e
            LEFT JOIN hr.departments d 
            ON e.department_id = d.department_id
            WHERE d.department_id IS NULL;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
    finally:
        conn.close()

    assert len(rows) == 0, f"Invalid department_id(s) found in employees table: {rows}"


def test_valid_employee_email():
    """
    Validate that all employee emails follow the format specified:
    - At least one word (letters only)
    - Dot (.) allowed between or after words
    - Must end with '@sqltutorial.org'
    The test fails if any employee email does not comply with this format.
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM hr.employees")
        rows = cursor.fetchall()
    finally:
        conn.close()

    # Define regex pattern for valid email format
    email_pattern = re.compile(r"^[a-zA-Z]+(\.[a-zA-Z]+)*@sqltutorial\.org$")

    # Filter invalid emails based on the regex pattern
    invalid_emails = [row[0] for row in rows if not email_pattern.match(row[0])]

    assert len(invalid_emails) == 1, f"Invalid email(s) found: {invalid_emails}"


def test_valid_employee_manager_id():
    """
    Validate that all employees have a valid manager_id, except for Steven King (the boss).
    The test fails if any employee other than Steven King does not have a manager_id.
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = """
            SELECT employee_id, last_name, manager_id 
            FROM hr.employees 
            WHERE manager_id IS NULL 
            AND NOT (first_name = 'Steven' AND last_name = 'King');
        """
        cursor.execute(query)
        rows = cursor.fetchall()
    finally:
        conn.close()

    assert len(rows) == 0, f"Employees without a manager specified, excluding Steven King: {rows}"