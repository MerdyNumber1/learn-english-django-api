from urllib import parse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from asgiref.sync import sync_to_async


class QueryAuthMiddleware:
    """
    Middleware to authenticate user on WS connect
    """

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        auth = JWTAuthentication()
        params = parse.parse_qs(scope['query_string'].decode('utf-8'))
        raw_token = params.get('token', [None])[0]

        if not scope.get('user'):
            try:
                validated_token = auth.get_validated_token(raw_token)
                user = await sync_to_async(auth.get_user)(validated_token)

                scope['user'] = user
            except InvalidToken:
                return None

        return await self.app(scope, receive, send)
