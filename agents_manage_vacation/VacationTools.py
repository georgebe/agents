import sqlite3
from datetime import datetime

from phi.tools import Toolkit

class VacationTools(Toolkit):
    def __init__(self): 
        super().__init__("vacation_tools")
        self.register(self.get_available_vacations_days)
        self.register(self.reserve_vacation_time)
    
    def get_available_vacations_days(self, employee_id: int) -> str:
        """Use this function to get the available vacation days of an employee.

        Args:
            employee_id (int): the id of the employee for which time off will be reserved.

        Returns:
            str: The available vacation days or an error message.
        """
        print(f"Getting available vacation days for employed_id {employee_id}")
        conn = sqlite3.connect('employee_database.db')
        c = conn.cursor()

        if employee_id:

            # Fetch the available vacation days for the employee
            c.execute("""
                SELECT employee_vacation_days_available
                FROM vacations
                WHERE employee_id = ?
                ORDER BY year DESC
                LIMIT 1
            """, (employee_id,))

            available_vacation_days = c.fetchone()

            if available_vacation_days:
                available_vacation_days = available_vacation_days[0]  # Unpack the tuple
                print(f"Available vacation days for employed_id {employee_id}: {available_vacation_days}")
                conn.close()
                return f"Available vacation days for employed_id {employee_id}: {available_vacation_days}"
            else:
                return_msg = f"No vacation data found for employed_id {employee_id}"
                print(return_msg)
                return return_msg
                conn.close()
        else:
            raise Exception(f"No employeed id provided")

        # Close the database connection
        conn.close()
        
        
    def reserve_vacation_time(self, employee_id: int, start_date: str, end_date: str) -> str:
        """Use this function to reserve vacation time for an employee. You need all parameters to reserve vacation time

        Args:
            employee_id (int): the id of the employee for which time off will be reserved.
            start_date (str) : start date of the vacation
            end_date (str) : end date of the vacation

        Returns:
            str: Success or an Error message based on the success or error in 
            applying for vacation days .
        """
        # Connect to the SQLite database

        conn = sqlite3.connect('employee_database.db')
        c = conn.cursor()
        try:
            # Calculate the number of vacation days
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            vacation_days = (end_date - start_date).days + 1

            # Get the current year
            current_year = start_date.year

            # Check if the employee exists
            c.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,))
            employee = c.fetchone()
            if employee is None:
                return_msg = f"Employee with ID {employee_id} does not exist."
                print(return_msg)
                conn.close()
                return return_msg

            # Check if the vacation days are available for the employee in the current year
            c.execute("SELECT employee_vacation_days_available FROM vacations WHERE employee_id = ? AND year = ?", (employee_id, current_year))
            available_days = c.fetchone()
            if available_days is None or available_days[0] < vacation_days:
                return_msg = f"Employee with ID {employee_id} does not have enough vacation days available for the requested period."
                print(return_msg)
                conn.close()
                return return_msg

            # Insert the new vacation into the planned_vacations table
            c.execute("INSERT INTO planned_vacations (employee_id, vacation_start_date, vacation_end_date, vacation_days_taken) VALUES (?, ?, ?, ?)", (employee_id, start_date, end_date, vacation_days))

            # Update the vacations table with the new vacation days taken
            c.execute("UPDATE vacations SET employee_vacation_days_taken = employee_vacation_days_taken + ?, employee_vacation_days_available = employee_vacation_days_available - ? WHERE employee_id = ? AND year = ?", (vacation_days, vacation_days, employee_id, current_year))

            conn.commit()
            print(f"Vacation saved successfully for employee with ID {employee_id} from {start_date} to {end_date}.")
            # Close the database connection
            conn.close()
            return f"Vacation saved successfully for employee with ID {employee_id} from {start_date} to {end_date}."
        except Exception as e:
            raise Exception(f"Error occurred: {e}")
            conn.rollback()
            # Close the database connection
            conn.close()
            return f"Error occurred: {e}"