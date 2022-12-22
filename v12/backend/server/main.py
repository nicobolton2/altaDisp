import grpc
import buffer_pb2
import buffer_pb2_grpc
from concurrent import futures
from pymongo import MongoClient
import os

#conexion a mongodb con user y pass
MONGO_URI = "mongodb://mongodb:27017/"
client = MongoClient(MONGO_URI,username="root",password="example")
db = client["db"]

class DataServer(buffer_pb2_grpc.Servicer):

    def GetTemperature(self, request, context):
        res = db['temperature'].find().sort("_id", -1)[0]
        i = str(res['id'])
        t = str(res['temp'])
        var = {'id': i, 'temp': t}
        res = buffer_pb2.Temperature(**var)
        return res
    
    def GetDollar(self, request, context):
        res = db['dollar'].find().sort("_id", -1)[0]
        i = str(res['id'])
        d = str(res['dollar'])
        var = {'id': i, 'dollar': d}
        res = buffer_pb2.Dollar(**var)
        return res
    
    def GetUF(self, request, context):
        res = db['uf'].find().sort("_id", -1)[0]
        i = str(res['id'])
        d = str(res['uf'])
        var = {'id': i, 'uf': d}
        res = buffer_pb2.UF(**var)
        return res
        
    def GetGame(self, request, context):
        res = db['game'].find().sort("_id", -1)[0]
        i = str(res['id'])
        g = str(res['game'])
        var = {'id': i, 'game': g}
        res = buffer_pb2.Game(**var)
        return res
    
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    buffer_pb2_grpc.add_ServicerServicer_to_server(DataServer(), server)
    server.add_insecure_port('[::]:50051')  
    server.start()
    server.wait_for_termination()
    
if __name__ == '__main__':
    main()