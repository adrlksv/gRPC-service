git clone https://github.com/adrlksv/gRPC-service/tree/branch-1.git
cd grpc-service
docker-compose build
docker-compose up
docker-compose exec grpc-service python services/client.py