## Клонирование репозитория
```git clone https://github.com/adrlksv/gRPC-service/tree/branch-1.git```

## Переходим в директорию проекта
```cd grpc-service```

## Собираем Docker-образ
```docker-compose up --build```

## Проверка работы
### Подключение к контейнеру postgresql
```docker exec -it grpc-service-postgres-1 psql -U postgres -d grpc_db```

### После подключения введите команду для вывода всех записей в таблице
```SELECT * FROM grpc_data;```