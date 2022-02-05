from flask import Flask
from flask_classful import FlaskView, route


class NodeAPI(FlaskView):

    #
    def __init__(self):

        self.app = Flask(__name__)

    #
    def start(self, apiPort):

        NodeAPI.register(self.app, route_base='/')
        self.app.run(host='localhost', port=apiPort)

    #
    @route('/info', methods=['GET'])
    def info(self):

        return 'This is a communication interface to node blockchain', 200
