import grpc
import json
import time

import service_pb2
import service_pb2_grpc

from concurrent.futures import ThreadPoolExecutor
from db.db_utils import insert_data, connect_to_db


class PacketDataService(service_pb2_grpc.PacketServiceServicer):
    def PacketData(self, request, context):
        print(f"Получен пакет данных:")
        print(f"PacketTimestamp: {request.PacketTimestamp}")
        print(f"PacketSeqNum: {request.PacketSeqNum}")
        print(f"NRecords: {request.NRecords}")

        for i, data in enumerate(request.PacketData):
            print(f"""Запись {i + 1}: Decimal1={data.Decimal1}, Decimal2={data.Decimal2}, 
                  Decimal3={data.Decimal3}, Decimal4={data.Decimal4}, Timestamp={data.Timestamp}""")
        
        insert_data(request)
            
        return service_pb2.ServiceResponse(success=True,
                                            message="Данные успешно приняты!")
        

def serve():
    with open('../config/server_config.json', 'r') as f:
        config = json.load(f)

    with connect_to_db() as conn:
        with conn.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE grpc_data;")
            conn.commit()

    server = grpc.server(ThreadPoolExecutor())
    service_pb2_grpc.add_PacketServiceServicer_to_server(
        PacketDataService(), server)
    server.add_insecure_port(f'[::]:{config["gRPCServerPort"]}')
    server.start()
    print(f"Сервер запущен на порту {config['gRPCServerPort']}")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
