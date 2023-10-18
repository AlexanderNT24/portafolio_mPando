#!/bin/bash
# Detener y eliminar el contenedor existente
docker stop mpando_portfolio
docker rm mpando_portfolio

# Construir la imagen Docker
docker build -t mpando_portfolio .

# Ejecutar el contenedor
docker run -p 9086:9086 --name mpando_portfolio mpando_portfolio

# Reiniciar el contenedor
docker restart mpando_portfolio
