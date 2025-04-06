import pytest
import re
from config.db_config import get_db_connection

def test_count_emails():
    """
    Validate emails count
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Count(email) FROM hr.employees")
        result = cursor.fetchall()
    finally:
        conn.close()

    emails = [row[0] for row in result]


    assert emails[0] == 40, f"Count equals: {emails}"