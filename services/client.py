import grpc
import json
import time
import service_pb2
import service_pb2_grpc
import time


def run():
    with open('../config/client_config.json', 'r') as f:
        config = json.load(f)

    channel = grpc.insecure_channel(f'{config["gRPCServerAddr"]}:{config["gRPCServerPort"]}')
    stub = service_pb2_grpc.PacketServiceStub(channel)

    for i in range(config["TotalPackets"]):
        packet = service_pb2.DataRequest(
            PacketTimestamp=int(time.time()),
            PacketSeqNum=i,
            NRecords=config["RecordsInPacket"],
            PacketData=[
                service_pb2.Data(
                    Decimal1=1.0 * (j + 1),
                    Decimal2=2.0 * (j + 1),
                    Decimal3=3.0 * (j + 1),
                    Decimal4=4.0 * (j + 1),
                ) for j in range(config["RecordsInPacket"])
            ]
        )

        response = stub.PacketData(packet)
        if response.success:
            print(f"""Пакет {i} успешно отправлен:
                  {response.message}""")
        else:
            print(f"""Ошибка отправки пакета {i}:
                  {response.message}""")
        
        time.sleep(config["TimeInterval"])


if __name__ == '__main__':
    run()
