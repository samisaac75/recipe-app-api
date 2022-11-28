"""
Test Custom management commands.
"""

# pathis to mock the behaviour of the database.
from unittest.mock import patch

#  This is one of the possible errors that we might get when we try to connect to the database.
from psycopg2 import OperationalError as Psycopg2Error

# Helper function to call a command by name
from django.core.management import call_command

# Another exception error
from django.db.utils import OperationalError

# Base test class
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test Commands"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database when database is ready."""
        patched_check.return_value = True

        call_command('wait_for_db')
        