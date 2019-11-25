from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import gomoku_ui.gomoku_app.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            gomoku_ui.gomoku_app.routing.websocket_urlpatterns
        )
    ),
})
