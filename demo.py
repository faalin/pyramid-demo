# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    print(request.matchdict)
    return Response('Hello World! %(name)s CHINA' % request.matchdict)

if __name__ == '__main__':
    with Configurator() as config:
        config.include("pyramid_debugtoolbar")
        config.add_route('hello', '/test/{name}')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
