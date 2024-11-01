import sys
from src.logger import logging



def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed error information, including the filename and line number 
    where the error occurred.

    Parameters:
    - error: Exception object representing the error that occurred.
    - error_detail: sys module (or another object providing exc_info()).

    Returns:
    - str: A formatted string with detailed error information.
    """
    # Get traceback information from the exception details
    _, _, exc_tb = error_detail.exc_info()  # exc_info() provides the traceback
    # Extract filename and line number where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    # Format the error message
    error_message = f"Error occurred in script: '{file_name}' at line {line_number} | Error: {error}"
    return error_message


class CustomException(Exception):
    """
    Custom exception class that provides detailed error information for debugging.

    Attributes:
    - error_message (str): Formatted error message with filename, line number, and error description.
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Initialize the CustomException with a detailed error message.

        Parameters:
        - error_message: Initial message for the error.
        - error_detail: sys module (or another object providing exc_info()).
        """
        # Call the base class constructor with the error message
        super().__init__(error_message)

        # Generate detailed error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Return the detailed error message when the exception is printed.
        """
        return self.error_message


