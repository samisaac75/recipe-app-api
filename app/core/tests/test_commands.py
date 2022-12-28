"""
Test Custom management commands.
"""

# path is to mock the behaviour of the database.
from unittest.mock import patch

#  This is one of the possible errors that we might get when we try to connect to the database.
from psycopg2 import OperationalError as Psycopg2Error

# Helper function to call a command by name
from django.core.management import call_command

# Another exception error may get thrown depending on the stage of the startup process
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
        # This ensures that the mocked value (which is the check method) is called with the parameters database=['default']
        patched_check.assert_called_once_with(database=['default'])

    @patch('time.sleep')
    def wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting Operational Error"""

        """This is the way me make an excpetion."""
        """Side effect lets you pass various items to it and it gets handled differently depending on their type"""
        """The mocking library knows to raise that exception"""
        """If we pass a boolean, i will return a boolean value."""
        """This alows us to call the various values that happen each time we call it in the order we call it."""
        """The following code says, the first two times, it raises the Psycopg2 error"""
        """Then we raise 3 operational errors"""
        """The Psycopg2 error is usually raised early on when Postgresl hasn't not even started and is not ready to accpet any connections"""
        """After that, the error could be that - Postgresql has started up but the databas hasn't been setup yet. Django comes back with an operational error and is being simulated by an 3 operational error. It can be more than 3"""
        """The 6th time, it returns a True after raising an 2 pyscopg2 errors and 3 Operational errors which means everything has started up correctly"""
        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]
        
        """After we simulate the error, we call the wait for db command and then we make our assertion"""
        call_command('wait_for_db')

        """The call count for the patch check needs to be 6 times. No more no less"""
        self.assertEqual(patched_check.call_count, 6)

        """It is called with not called once becuse it is called multiple times. We are checking that the pacthed check is being called using the default database"""
        patched_check.assert_called_with(database=['default'])