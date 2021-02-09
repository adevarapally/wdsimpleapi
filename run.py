import falcon
from falcon import Request, Response
import logging
from wsgiref import simple_server

from logic import wd_sum
class HelloWorld():

    def on_get(self, req: Request, resp: Response) -> None:
        '''Handles GET requests'''
        resp.media = 'Hellow World'

class Sum():

    def on_post(self, req: Request, resp: Response) -> None:
        '''Handles GET requests'''
        val_1 = req.media.get('val_1')
        val_2 = req.media.get('val_2')
        try:
            resp.media = wd_sum(val_1, val_2)
        except Exception as e:
            resp.status = falcon.HTTP_400
            resp.media = str(e)
        
        

API = falcon.API()

API.add_route('/', HelloWorld())
API.add_route('/sum', Sum())

if __name__ == '__main__':
    import sys
    LOGGER = logging.getLogger()
    LOGGER.addHandler(logging.StreamHandler())
    LOGGER.setLevel(logging.DEBUG)
    SERVER_PORT = 5000
    HTTP = simple_server.make_server('0.0.0.0', SERVER_PORT, API)
    LOGGER.info('Serving on port %s...', SERVER_PORT)
    HTTP.serve_forever()