# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto
COPY . .

# Establecer variables de entorno
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Comando por defecto para ejecutar tests
CMD ["python", "-m", "unittest", "discover", "-v"]