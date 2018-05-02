from app import app
from app import mongo
import re
import json
from flask import abort, request,redirect


@app.route('/')
def branchef():
    return redirect('https://github.com/Mario2334/Bank_Rest')


@app.route('/ifsc', methods=['GET'])
def get_branch():
    ifsc = request.args.get('ifsc', type=str, default=None)
    page = request.args.get('page',type=int,default=None)
    branches = mongo.db.bank_branches
    # if ifsc is none and page is given then return 20 ifsc codes
    if ifsc is None and page:
        codes = list(branches.find({}, {'ifsc': 1, 'bank_name': 1, '_id': 0}).sort([('count', 1)]).skip(page*20).limit(
            20))
        return json.dumps({'codes': codes})

    if ifsc is None and page is None:
        return abort(400)

    if re.match(r'((?:[a-zA-Z]+[0-9]|[0-9]+[a-zA-Z])[a-zA-Z0-9]*)', ifsc):
        data = branches.find_one({'ifsc': ifsc}, {'_id': 0})
        return json.dumps(data)
    else:
        raise abort(400)


@app.route('/<string:bank>', methods=['GET'])
def get_branches(bank):
    city = request.args.get('city', default=None, type=str)
    page = request.args.get('page' , default=None,type=int)
    branches = mongo.db.bank_branches

    # if city is not given then return all bank branches
    if city is None:
        codes = list(
            branches.find({'bank_name': bank}, {'ifsc': 1, 'bank_name': 1, '_id': 0}).sort([('count', 1)]).skip(page *
                                                                                                             20).limit(
                20))
        return json.dumps({'codes': codes})

    data = list(branches.find({'bank_name': bank, 'city': city}, {'_id': 0}))
    if len(data) < 1:
        return abort(204)
    return json.dumps({'branches': data})
