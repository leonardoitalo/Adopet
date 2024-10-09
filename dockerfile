FROM python:3.12.4

# Define um diretório de trabalho
WORKDIR /code

# Copia apenas o arquivo de requisitos primeiro
COPY requirements.txt /code/

# Instala as dependências
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home duser

# Adiciona a pasta scripts e venv/bin 
# no $PATH do container.
ENV PATH="/scripts:/venv/bin:$PATH"

# Copia apenas os arquivos necessários para a imagem
COPY . /code/

# Copia o script de entrada e define permissões
COPY ./scripts/entrypoint.sh /code/scripts/entrypoint.sh
RUN chmod +x /code/scripts/entrypoint.sh

# Comando de inicialização
CMD ["./scripts/entrypoint.sh"]
