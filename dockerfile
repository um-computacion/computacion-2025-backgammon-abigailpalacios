# 1. Usar una imagen base de Python oficial y ligera
FROM python:3.13-slim

# 2. Establecer variables de entorno recomendadas
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# 3. Establecer el directorio de trabajo DENTRO del contenedor
WORKDIR /app

# 4. Instalar dependencias del sistema operativo
# AUNQUE corramos la CLI, tu 'requirements.txt' probablemente incluye Pygame.
# Para que 'pip install pygame' funcione, necesitamos las librerías de SDL.
RUN apt-get update && apt-get install -y \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    libportmidi0 \
    # Limpiar la caché para mantener la imagen ligera
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 5. Copiar e instalar las dependencias de Python
# Copiamos solo 'requirements.txt' primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiar TODO el código de tu proyecto al contenedor
COPY . .

# 7. Definir el comando por defecto (Modo Juego: CLI)
# Esto se ejecutará si corres el contenedor sin comandos adicionales.
CMD ["python", "-m", "unittest", "discover", "-v"]