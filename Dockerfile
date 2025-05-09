# Imagen base ligera de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todos los archivos del proyecto al contenedor
COPY . .

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt || true

# Mantener el contenedor en ejecución
CMD ["tail", "-f", "/dev/null"]
