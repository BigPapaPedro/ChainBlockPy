import requests
from flask import Flask, jsonify, request, render_template
from flask_classful import FlaskView, route
from BlockchainUtils import BlockchainUtils
from SocketCommunication import SocketCommunication

node = None


class NodeAPI(FlaskView):

    #
    def __init__(self):

        self.app = Flask(__name__)

    #
    def start(self, ip, apiPort):

        NodeAPI.register(self.app, route_base='/')
        self.app.run(host=ip, port=apiPort, use_reloader=True)

    #
    def injectNode(self, injectedNode):

        global node
        node = injectedNode

    #
    @route('/', methods=['GET'])
    def indexPage(self):

        return render_template('home.html')

    #
    @route('info', methods=['GET'])
    def info(self):

        return '<!DOCTYPE html><html lang="en"><head><title>ChainBlockPy 0.01</title></head><body>ChainBlockPy 0.01</body></html>', 200

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
    @route('maketxn', methods=['GET'])
    def makeTxn(self):

        return render_template('maketxn.html')

    #
    @route('newtxn', methods=['POST'])
    def newtxn(self):

        print("@route newtxn: " + str(request.data))

        values = request.get_json()

        print(values)

        print("decode: txnType " + values['txnType'])
        print("decode: signature " + values['amount'])
        print("decode: sndrPubKey " + values['sndrPubKey'])

        print('-----------------')

        theTxn = "\"" + values['txnType'] + "\""

        txn = exchange.createTransaction(values['sndrPubKey'], values['amount'], theTxn)

        # Decode the received json string into an object.
        txn = BlockchainUtils.decode(values['txn'])

        print("decode: id " + txn.id)
        print("decode: txnType " + txn.txnType)
        print("decode: signature " + txn.signature)
        print("decode: amount " + str(txn.amount))
        print("decode: sndrPubKey " + txn.sndrPubKey)
        print("decode: rcvrPubKey " + txn.rcvrPubKey)
        print("decode: timeStamp " + str(txn.timeStamp))

        node.handleNewTxn(txn)

        response = {'msg': 'Received transaction'}
        return jsonify(response), 201

    #
    @route('txn', methods=['POST'])
    def txn(self):

        print("---> NodeAPI.txn: " + str(request.data))
        values = request.get_json()
        responseBody = None
        responseCode = 400

        # Verify the received string contains json values.
        if not 'txn' in values:

            responseBody = {'msg': 'Missing transaction values'}
            #return 'Missing transaction values.', 400

        else:

            # Decode the received json string into an object.
            txn = BlockchainUtils.decode(values['txn'])

            print("decode: id " + txn.id)
            print("decode: txnType " + txn.txnType)
            print("decode: signature " + txn.signature)
            print("decode: amount " + str(txn.amount))
            print("decode: sndrPubKey " + txn.sndrPubKey)
            print("decode: rcvrPubKey " + txn.rcvrPubKey)
            print("decode: timeStamp " + str(txn.timeStamp))

            # Handle the transaction.
            node.handleTxn(txn)

            responseBody = {'msg': 'Transaction ' + txn.id + ' Received'}
            responseCode = 200

        return jsonify(responseBody), responseCode

    #
    @route('about', methods=['GET'])
    def about(self):

        return render_template('about.html')

    #
    @route('blockchainexplorer', methods=['GET'])
    def blockchainExplorer(self):

        return render_template('blockchainexplorer.html')

    #
    @route('pendingtransactions', methods=['GET'])
    def pendingTxns(self):

        return render_template('pendingtransactions.html')

    #
    @route('networkexplorer', methods=['GET'])
    def networkExplorer(self):

        return render_template('networkexplorer.html')

    #
    @route('echotest', methods=['POST'])
    def echoTest(self):
        print("@route echoTest: " + str(request.data))
        return request.data, 201
