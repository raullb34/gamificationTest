# Usar una imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar el script de espera
RUN curl -o /wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /wait-for-it.sh

# Copiar el archivo de requerimientos y el código fuente a la imagen
COPY requirements.txt requirements.txt
COPY . .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá Flask
EXPOSE 5000

# Comando por defecto para ejecutar el script de creación de tablas y luego iniciar la aplicación Flask
CMD ["sh", "-c", "./wait-for-it.sh db:5432 -- python ./startup/startup.py && python run.py"]
