FROM python:3.11.7

# Установите Rust и Cargo
RUN apt-get update && \
    apt-get install -y build-essential && \
    curl https://sh.rustup.rs -sSf | sh -s -- -y

ENV PATH="/$HOME/.cargo/bin:${PATH}"

RUN pip install --upgrade pip

# Копируйте файлы проекта
COPY . /app

# Установите зависимости Python
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip uninstall jsonschema

# Запустите ваше приложение
CMD ["python", "main.py"]