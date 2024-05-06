import base64
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests

from spotify_api_proxy_config import CLIENT_ID, CLIENT_SECRET, PORT

token = ''

def get_token():
    global token
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET
    headers = {'Authorization': 'Basic ' + (base64.b64encode((client_id + ':' + client_secret).encode())).decode()}
    data = {'grant_type': 'client_credentials'}
    resp0 = requests.post('https://accounts.spotify.com/api/token', data=data, headers=headers)
    token = resp0.json().get('access_token')
    print(f'{token=}')


class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Request URL from the client
        client_request_url = self.path

        # External URL to send the request to
        external_url = 'https://api.spotify.com' + client_request_url

        # Authorization header with the token
        headers = {'Authorization': 'Bearer ' + token}

        # Send the request to the external URL
        response = requests.get(external_url, headers=headers)
        print(f'{response.status_code=}')

        # Send the response back to the client
        self.send_response(response.status_code)
        # Filter out the 'Transfer-Encoding' header to prevent the client from waiting for more data
        filtered_headers = {k: v for k, v in response.headers.items() if k.lower() != 'transfer-encoding'}
        for key, value in filtered_headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(response.content)

def run(server_class=HTTPServer, handler_class=ProxyHTTPRequestHandler, port=PORT):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    get_token()
    run()
