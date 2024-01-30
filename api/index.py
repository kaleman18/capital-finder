from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):

        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            response = requests.get(f"https://restcountries.com/v3.1/name/{dic['country']}?fullText=true")
            data = response.json()
            capital = data[0]["capital"][0]
            message = f"The capital of {dic['country']} is {capital}"

        elif "capital" in dic:
            response = requests.get(f"https://restcountries.com/v3.1/capital/{dic['capital']}")
            data = response.json()
            country = data[0]["name"]["common"]
            message = f"{dic['capital']} is the capital of {country}."
    

        else:
            message = "please provide a valid country or capital"

        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers() 
        self.wfile.write(message.encode('utf-8'))
        return
    