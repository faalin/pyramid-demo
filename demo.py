# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    print(request.matchdict)
    return Response('Hello World!')


def main(**settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    config.scan()
    return config.make_wsgi_app()


if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
