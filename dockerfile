FROM python:3.12.4

# Define um diretório de trabalho
WORKDIR /code

# Copia apenas o arquivo de requisitos primeiro
COPY requirements.txt /code/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia apenas os arquivos necessários para a imagem
COPY . /code/

# Copia o script de entrada e define permissões
COPY ./scripts/entrypoint.sh /code/scripts/entrypoint.sh
RUN chmod +x /code/scripts/entrypoint.sh

# Comando de inicialização
CMD ["./scripts/entrypoint.sh"]
