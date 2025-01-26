from rest_framework import status
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """Custom exception handler."""
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            response.data = {
                "error":
                "Invalid request. Please check your input data.",
                "details": response.data,
            }
        elif response.status_code == status.HTTP_401_UNAUTHORIZED:
            response.data = {
                "error":
                "Authentication failed.Please provide valid credentials.",
            }
        elif response.status_code == status.HTTP_403_FORBIDDEN:
            response.data = {
                "error":
                "You do not have permission to perform this action.",
            }
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            response.data = {
                "error":
                "The requested resource was not found.",
            }
        elif response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
            response.data = {
                "error":
                "An internal server error occurred. Please try again later.",
            }

    return response
