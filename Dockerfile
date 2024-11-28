# Usa uma imagem base oficial do Python
FROM python:3.12-slim-bookworm

# Copia o executável do uv para dentro do contêiner
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Instalar dependências do sistema
#RUN apt-get update && apt-get install -y \
#    wget \
#    unzip \
#    iputils-ping \
#    dnsutils \
#    curl \
#    && rm -rf /var/lib/apt/lists/*

# Instalar FFUF
#RUN wget https://github.com/ffuf/ffuf/releases/download/v1.5.0/ffuf_1.5.0_linux_amd64.tar.gz \
#    && tar -zxvf ffuf_1.5.0_linux_amd64.tar.gz \
#    && mv ffuf /usr/local/bin/ \
#    && rm ffuf_1.5.0_linux_amd64.tar.gz



# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

ADD . /app


# Copia o código da aplicação para o contêiner
COPY . .

RUN uv sync --frozen

# Expõe a porta 8000 para comunicação (opcional, dependendo da configuração do FastStream)
EXPOSE 8000

# Define a variável de ambiente para evitar buffer no log
ENV PYTHONUNBUFFERED=1

# Comando para iniciar a aplicação usando `uv run`
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
