import itertools
import os
import requests
import random

from flask import Flask, json, request
from flask_restplus import Api, Resource

from config import Config

CACHE_PATH = Config.CACHE_PATH
PROB_PATH = Config.PROB_PATH
GIT_URL = Config.GIT_URL
SLACK_INCOMING_HOOKS = Config.SLACK_INCOMING_HOOKS

app = Flask(__name__)
api = Api(app)

@api.route('/v1/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

@api.route('/v1/activate_summary')
class ActivateSummary(Resource):
    def get(self):
        return 'activated'

@api.route('/v1/summary')
class Summary(Resource):
    def post(self):
        channel_name = request.form.get('channel_name', None)

        if channel_name and channel_name == 'tc2-get-notified':
            counts = {'wy':0, 'dh':0, 'dy':0, 'jk':0, 'kw':0}

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
            
            message = "Total {} problems\n".format(total_count)
            message += "\n".join(["%3s: %4d (%5.2f%%)" % (key.upper(), counts[key], counts[key]/total_count*100) for key in counts])
        else:
            message = "Only for tc2-get-notified channel. Come to tc2-get-notified and catch your dream!"
        response = app.response_class(
            response=json.dumps({
                'response_type': 'in_channel',
                'text': message
            }),
            status=200,
            mimetype='application/json'
        )
        return response

@api.route('/v1/yaong')
class Yaong(Resource):
    def post(self):
        message = random.choice(['야옹?', '냐', '냐아아아아!', '꿍', '꾸우우우웅?', '냥!'])
        print("hiru")
        try:
            channel_name = request.form.get('channel_name', None)
        except:
            print("bad")
        if channel_name and channel_name in SLACK_INCOMING_HOOKS:
            requests.post(SLACK_INCOMING_HOOKS[channel_name],
                json={'text':message},
                headers={'Content-Type': 'application/json'})
            response = app.response_class(
                    response=None,
                    status=200,
                    mimetype='application/json')
            return response
        else:
            response = app.response_class(
                response=json.dumps({
                    'response_type': 'in_channel',
                    'text': message
                }),
                status=200,
                mimetype='application/json'
            )
            return response


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')
