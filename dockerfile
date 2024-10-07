FROM ubuntu:24.04

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    libpq-dev \
    postgresql \
    postgresql-contrib \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Создаем виртуальное окружение
RUN python3 -m venv /opt/venv

# Обновляем pip
RUN /opt/venv/bin/pip install --upgrade pip

# Устанавливаем зависимости из requirements.txt
WORKDIR /app
COPY requirements.txt ./
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY ./services/ ./services/
COPY ./db/ ./db/
COPY ./config/ ./config/

# Установка переменных окружения
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH="/app:/app/db"

# Проверка наличия файлов
RUN ls -la /app/services/

# Запуск сервера
CMD ["python", "/app/services/server.py"]
