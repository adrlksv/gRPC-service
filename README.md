## Клонирование репозитория
```git clone https://github.com/adrlksv/gRPC-service/tree/branch-1.git```

## Переходим в директорию проекта
```cd grpc-service```

## Собираем Docker-образ
```docker-compose build```
```docker-compose up```

## Запускаем контейнеры сервиса и базы данных
```docker-compose exec grpc-service python services/client.py```