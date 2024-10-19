# Stage 1: Build environment (compilação de dependências)
FROM python:3.12-slim AS build

WORKDIR /code

# Instalar ferramentas de compilação necessárias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copiar arquivo de dependências
COPY requirements.txt /code/

# Instalar dependências
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Production environment (somente o necessário para produção)
FROM python:3.12-slim AS production

WORKDIR /code

# Copiar dependências instaladas do stage de build
COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Copiar o código da aplicação
COPY . /code/

# Copiar o script de entrada
COPY ./scripts/entrypoint.sh /scripts/entrypoint.sh
RUN chmod +x /scripts/entrypoint.sh

# Adicionar a pasta scripts ao PATH
ENV PATH="/scripts:$PATH"

# Definir o usuário não privilegiado para maior segurança
# USER duser

# Expor a porta que o servidor usará (padrão para Django é 8000)
EXPOSE 8000

# Comando de inicialização que executa o script entrypoint.sh
CMD ["/scripts/entrypoint.sh"]
