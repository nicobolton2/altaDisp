from flask import Flask, request
import grpc
import json
from google.protobuf.json_format import MessageToJson
from flask import request, jsonify
from flask_cors import CORS
import buffer_pb2
import buffer_pb2_grpc

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def ruta_inicial():
    return "Ruta inicial"

@app.route('/temperature', methods=['GET'])
def get_temperature():
    app.logger.info('Request temperatureeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
    print("\n")
    print("temperature")
    if request.method == 'GET':
        client = DataClient()
        res = json.loads(MessageToJson(client.get_temperature()))
        return jsonify(res)
    else:
        return "error _temperature_"
@app.route('/uf', methods=['GET'])
def get_uf():
    print("uf")
    return

@app.route('/dollar', methods=['GET'])
def get_dollar():
    print("dollar")
    return

@app.route('/game', methods=['GET'])
def game():
    print("game")
    return

@app.route('/getAllData', methods=['GET'])
def game():
    print("game")
    return


#exportar dataclient y dataserver y con eso queda ready
class DataClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('server:50051', options=(('grpc.enable_http_proxy', 0),))
        self.stub = buffer_pb2_grpc.ServicerStub(self.channel)
    def get_temperature(self):
        return self.stub.GetTemperature(buffer_pb2.Empty())
    def get_uf(self):
        return self.stub.GetUF(buffer_pb2.Empty())
    def get_dollar(self):
        return self.stub.GetDollar(buffer_pb2.Empty())

def main():
    app.run(host="0.0.0.0", port=5000, debug=True)
    
if __name__ == '__main__':
    main()