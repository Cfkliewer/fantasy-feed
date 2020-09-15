from flask import Flask, request
import requests
import json
from schema.query import schema
from sleeper_wrapper import League

app = Flask(__name__)

@app.route("/", methods=['POST'])
def graphql():
    data = json.loads(request.data)
    result = schema.execute(data['query'])
    return json.dumps(result.data)
