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
        var = {'id': '1', 'temp': '33'}
        db['temperature'].insert_one(var)

        
        res = db['temperature'].find().sort("_id", -1)[0]
        t = str(res['temp'])
        var = {'id': '1', 'temp': t}
        res = buffer_pb2.Temperature(**var)
        return res
    '''
    def GetDollar(self, request, context):
        res = db['dollar'].find().sort("_id", -1)[0]
        d = str(res['dollar'])
        var = {'id': '1', 'temp': d}
        res = buffer_pb2.Temperature(**var)
        return res
    
    def GetUF(self, request, context):
        res = db['uf'].find().sort("_id", -1)[0]
        d = str(res['uf'])
        var = {'id': '1', 'uf': d}
        res = buffer_pb2.Temperature(**var)
        return res
    '''      
    
def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    buffer_pb2_grpc.add_ServicerServicer_to_server(DataServer(), server)
    server.add_insecure_port('[::]:50051')  
    server.start()
    server.wait_for_termination()
    
if __name__ == '__main__':
    main()