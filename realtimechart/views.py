import logging
import gevent 

from json import dumps
from pyramid.view import view_config
from pyramid.response import Response

from realtimechart.namespaces import MessageNamespace

from socketio import socketio_manage

logger = logging.getLogger(__name__)

@view_config(route_name="socket_io")
def socket(request):
    """
    Websocket service used by socket.io.js
    """
    retval = socketio_manage(request.environ,
        {
            '/message': MessageNamespace,
        }, request = request)
    return Response(retval)

@view_config(route_name='home', renderer='home.jinja2')
def home(request):
    """
    Just the main page. Loads javascript libraries.
    """
    return {}

