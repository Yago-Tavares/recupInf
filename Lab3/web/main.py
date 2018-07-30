# -*- coding: utf-8 -*-
import webapp2
import json
from backend import top5Movies, top3Neighbors, printRMSE


class searchHandler(webapp2.RequestHandler):
    def get(self):
        uid = self.request.get('uid')
        response = {
            'movies': top5Movies(uid),
            'users': top3Neighbors(uid),
            'rmse': printRMSE()
        }

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(json.dumps(response))

app = webapp2.WSGIApplication([
    ('/api/results.*', searchHandler)
], debug=True)
