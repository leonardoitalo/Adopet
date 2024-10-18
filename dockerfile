# Utiliza uma imagem base menor (slim)
FROM python:3.12-slim

# Define um diretório de trabalho
WORKDIR /code

# Copia o arquivo de requisitos ANTES de instalar as dependências
COPY requirements.txt /code/

# Executa tudo em um único RUN para reduzir camadas
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl && \
    adduser --disabled-password --gecos "" --no-create-home duser && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt --root-user-action=ignore && \
    mkdir /scripts && \
    chown -R duser:duser /code

# Copia o script de entrada e define permissões
COPY ./scripts/entrypoint.sh /scripts/entrypoint.sh
RUN chmod +x /scripts/entrypoint.sh

# Copia o restante do código para o container
COPY . /code/

# Adiciona a pasta scripts ao PATH
ENV PATH="/scripts:$PATH"

# Troca para o usuário não privilegiado
USER duser

# Comando de inicialização
CMD ["./scripts/entrypoint.sh"]

