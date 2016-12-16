import json
import falcon

class RootClass(object):
    def on_get(self, req, resp):
        msg = {
            "message": "Welcome to the Falcon"
        }
        resp.body = json.dumps(msg)
    def on_post(self, req, resp):
        body = json.loads(req.stream.read().decode('utf-8'))
        print(body['user'])
        msg = {
            "message": "Welcome to the Falcon"
        }
        resp.body = json.dumps(msg)
        resp.status = falcon.HTTP_200

class CORSMiddleware:
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')

api = falcon.API(middleware=[CORSMiddleware()])
api.add_route('/', RootClass())

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, api)
    httpd.serve_forever()
