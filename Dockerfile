# Establecer la imagen base
FROM python:3.9.5

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos al contenedor
COPY requirements.txt .

# Instalar los requerimientos
RUN pip install -r requirements.txt

# Copiar el resto de los archivos al contenedor
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 9086

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:9086"]