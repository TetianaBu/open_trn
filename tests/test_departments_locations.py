import pytest
import re
from config.db_config import get_db_connection


def test_department_location_presents():
    """
    Validate that every department in the departments table has a non-NULL location_id.
    The test fails if any department has a NULL location_id.
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM hr.departments WHERE location_id IS NULL;')
        result = cursor.fetchone()[0]  # Fetch the count of rows with NULL location_id
        print(f"Number of departments with NULL location_id: {result}")  # Debugging information
    finally:
        conn.close()

    assert result == 0, f"There are {result} departments without specified location."


def test_invalid_department_location_id():
    """
    Validate that all location_id values in the departments table exist in the locations table.
    The test fails if location_id in departments does not have a corresponding entry in locations.
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = """
            SELECT DISTINCT d.location_id
            FROM hr.departments d
            LEFT JOIN hr.locations l 
            ON d.location_id = l.location_id
            WHERE l.location_id IS NULL;
        """
        cursor.execute(query)
        rows = cursor.fetchall()  # Get rows with unmatched location_id
        res = len(rows)
    finally:
        conn.close()

    assert res == 0, f"Invalid location_id found in departments table: {rows}"


def test_valid_street_address():
    """
    Validate that all street_address values in the locations table adhere to the format:
    - At least one numeric digit
    - At least one word (A-Z or a-z)
    - A space between words and numbers
    - Allow special characters like ',', '-', '.'
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT street_address FROM hr.locations")
        rows = cursor.fetchall()  # Fetch all street addresses
    finally:
        conn.close()

    # Define regex pattern for valid street addresses
    address_pattern = re.compile(r"^(?=.*\d)(?=.*[a-zA-Z])([a-zA-Z0-9\s,.-]+)$")

    # Filter out invalid addresses
    invalid_addresses = [row[0] for row in rows if not address_pattern.match(row[0])]

    assert len(invalid_addresses) == 0, f"Invalid or insufficient street addresses found: {invalid_addresses}"