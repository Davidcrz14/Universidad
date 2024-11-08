from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from rest_framework import status

class ErrorHandlingMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, Exception):
            return Response({'error': str(exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return None
