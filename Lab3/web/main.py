# -*- coding: utf-8 -*-
import webapp2
import json
import os
from backend import top5Movies, top3Neighbors, rmse

def read_file(path):
    path = os.path.dirname(os.path.realpath(__file__)) + '/frontend' + path
    file_stream = open(path, 'r')
    data = file_stream.read()
    file_stream.close()
    return data

def get_content_type(file):
    switch = {
        'js': 'application/javascript',
        'css': 'text/css',
        'html': 'text/html',
        'default': ''
    }

    file_type = file.split(".")[-1]
    return switch.get(file_type, switch['default'])

class searchHandler(webapp2.RequestHandler):
    def get(self):
        uid = self.request.get('uid')
        response = {
            'movies': top5Movies(int(uid)),
            'users': top3Neighbors(int(uid)),
            'rmse': rmse()
        }

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(json.dumps(response))

class IndexHandler(webapp2.RequestHandler):
    def get(self):
        path = '/index.html'
        data = read_file(path)

        self.response.headers['Content-Type'] = get_content_type(path.split('/')[-1])
        self.response.write(data)

class StaticsFilesHandler(webapp2.RequestHandler):
    def get(self):

        try:
            path = self.request.path
            data = read_file(path)

            self.response.headers['Content-Type'] = get_content_type(path.split('/')[-1])
            self.response.write(data)
        except:
            self.response.status = 404
        

app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/api/results.*', searchHandler),
    ('/.*', StaticsFilesHandler)
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8081')


if __name__ == '__main__':
    main()