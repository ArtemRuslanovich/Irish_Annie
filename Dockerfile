FROM python:3.11.7

# Установите Rust и Cargo
RUN apt-get update && \
    apt-get install -y build-essential && \
    curl https://sh.rustup.rs -sSf | sh -s -- -y

# Копируйте файлы проекта
COPY . /app

# Установите зависимости Python
WORKDIR /app
RUN pip install -r requirements.txt

# Запустите ваше приложение
CMD ["python", "main.py"]