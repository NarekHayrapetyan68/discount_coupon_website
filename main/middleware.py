import logging
import json
from django.utils.deprecation import MiddlewareMixin


class RequestLoggingMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def _log_request(self, request):
        try:
            body = request.body.decode('utf-8')
        except UnicodeDecodeError as e:
            self.logger.warning(f"Failed to decode request body: {e}")
            body = 'Failed to decode body'
        log_data = {
            'method': request.method,
            'path': request.path,
            'headers': dict(request.headers),
            'body': body,
        }
        self.logger.info(f"Request: {json.dumps(log_data)}")

    def _log_response(self, response):
        try:
            content = response.content.decode('utf-8')
        except UnicodeDecodeError as e:
            self.logger.warning(f"Failed to decode response content: {e}")
            content = 'Failed to decode content'
        log_data = {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'body': content,
        }
        self.logger.info(f"Response: {json.dumps(log_data)}")

    def __call__(self, request):
        self._log_request(request)

        response = self.get_response(request)

        self._log_response(response)

        return response
