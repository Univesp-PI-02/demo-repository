FROM python:3.12.7-alpine3.19
LABEL maintainer="thaisfsouza@outlook.com"

# Variáveis de ambiente para otimizar o comportamento do Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar dependências do sistema
RUN apk add --no-cache gcc musl-dev libffi-dev \
    postgresql-dev curl

# Copiar apenas o requirements.txt
COPY requirements.txt /projeto_cad/

# Instalar as dependências Python
RUN pip install --upgrade pip && pip install -r /projeto_cad/requirements.txt

# Copiar o restante do projeto
COPY projeto_cad /projeto_cad

# Definir a pasta de trabalho
WORKDIR /projeto_cad

# Expor a porta 8000
EXPOSE 8000

# Criar um usuário não-root para executar a aplicação (opcional)
RUN adduser -D appuser
USER appuser

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]