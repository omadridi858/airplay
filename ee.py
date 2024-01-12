import requests
def g(port):
    url = f'https://192.168.1.6:{port}/stream.xml'

    #demonstrate how to use the 'params' parameter:
    x = requests.get(url, params = {'Content-Length': '0'})

    #print the response (the content of the requested file):
    print(x.text)
