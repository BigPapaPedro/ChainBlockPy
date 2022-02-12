import requests
from flask import Flask, jsonify, request, render_template
from flask_classful import FlaskView, route
from BlockchainUtils import BlockchainUtils

node = None


class NodeAPI(FlaskView):

    #
    def __init__(self):

        self.app = Flask(__name__)

    #
    def start(self, ip, apiPort):

        NodeAPI.register(self.app, route_base='/')
        self.app.run(host=ip, port=apiPort)

    #
    def injectNode(self, injectedNode):

        global node
        node = injectedNode

    #
    @route('info', methods=['GET'])
    def info(self):

        return '<!DOCTYPE html><html lang="en"><head><title>ChainBlockPy</title></head><body>ChainBlockPy</body></html>', 200

    #
    @route('blockchain', methods=['GET'])
    def blockchain(self):

        return node.blockChain.toJson(), 200

    #
    @route('txnpool', methods=['GET'])
    def txnPool(self):

        txns = {}

        for ctr, transaction in enumerate(node.txnPool.txns):

            txns[ctr] = transaction.toJson()

        return jsonify(txns), 200

    #
    @route('txn', methods=['POST'])
    def txn(self):

        values = request.get_json()

        # Verify the received string contains json values.
        if not 'txn' in values:
            return 'Missing transaction values.', 400

        # Decode the received json string into an object.
        txn = BlockchainUtils.decode(values['txn'])

        # Handle the transaction.
        node.handleTxn(txn)

        response = {'msg': 'Received transaction'}

        return jsonify(response), 201

    #
    @route('/', methods=['GET'])
    def info(self):

        return render_template('info.html')

    #
    @route('blockchainexplorer', methods=['GET'])
    def blockchainExplorer(self):

        return render_template('blockchainexplorer.html')

    #
    @route('transactionexplorer', methods=['GET'])
    def txnsExplorer(self):

        return render_template('transactionsexplorer.html')
