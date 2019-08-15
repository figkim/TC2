import itertools
import os
import requests

from flask import Flask, json
from flask_restplus import Api, Resource

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
        message += "\n".join(["{}: {}({}%)".format(key, counts[key], counts[key]/total_count*100) for key in counts])

        results = requests.post(SLACK_INCOMING_HOOK,
            json={'text':message},
            headers={'Content-Type': 'application/json'})
        print(results)

        counts['total'] = total_count
        response = app.response_class(
            response=json.dumps("Success"),
            status=200,
            mimetype='application/json'
        )
        return response

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')
