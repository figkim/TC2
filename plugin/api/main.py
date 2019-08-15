import itertools
import os

from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

@api.route('/summary')
class Summary(Resource):
    def get(self):
        counts = {'wy':0, 'dh':0, 'dy':0, 'jk':0, 'kw':0}

        CACHE_PATH = '~/_tc2cache/TC2'
        PROB_PATH = os.path.join(CACHE_PATH, 'leetcode')
        GIT_URL = 'https://github.com/figkim/TC2.git'

        if not os.path.exists(CACHE_PATH):
            print("clone TC2")
            os.system('git clone {} {}'.format(GIT_URL, CACHE_PATH)) # TODO add check stdout of this call
        os.system('cd {} && git pull'.format(CACHE_PATH)) # TODO add check stdout of this call

        total_count = 0
        for folder in os.listdir(PROB_PATH):
            if os.path.isdir(os.path.join(PROB_PATH, folder)):
                total_count += 1
                for filename in os.listdir(os.path.join(PROB_PATH, folder)):
                    if filename.endswith('.py'):
                        commiter = filename.split('.')[-2][-2:].lower()
                        if commiter in counts:
                            counts[commiter] += 1
        
        counts['total'] = total_count
        return counts

if __name__ == '__main__':
    app.run(debug=True)
