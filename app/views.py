from app import app
from app import mongo
import re
import json
from flask import abort,render_template

@app.route('/')
def branchef():
    return render_template('hekl.html')

@app.route('/<string:ifsc>', methods=['GET'])
def get_branch(ifsc):
    if re.match(r'((?:[a-zA-Z]+[0-9]|[0-9]+[a-zA-Z])[a-zA-Z0-9]*)', ifsc):
        branches = mongo.db.bank_branches
        data = branches.find_one({'ifsc': ifsc}, {'_id': 0})
        return json.dumps(data)
    else:
        raise abort(405)


@app.route('/<string:bank>/<string:city>', methods=['GET'])
def get_branches(bank, city):
    branches = mongo.db.bank_branches
    data = list(branches.find({'bank_name': bank, 'city': city}, {'_id': 0}))
    if len(data) <1:
        return abort(404)
    return json.dumps({'branches': data})
