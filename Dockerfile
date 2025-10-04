# Используем официальный образ Python как базовый
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction

# Копируем остальной код приложения
COPY . .

# Указываем порт, на котором будет работать Django (по умолчанию 8000)
EXPOSE 8000

# Команда для запуска Django-сервера
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
