#!/bin/bash

# Pedir confirmación al usuario
read -p "¿Has realizado una copia de seguridad de tus datos? (y/n) " confirmacion

if [ "$confirmacion" == "y" ]; then
  # Detener y eliminar el contenedor existente
  docker stop mpando_portfolio
  docker rm mpando_portfolio
  
  # Construir la imagen Docker
  docker build -t mpando_portfolio .

  # Ejecutar el contenedor con el volumen montado
  docker run -p 9086:9086 --name mpando_portfolio -v portfolio_data:/app/db mpando_portfolio
else
  echo "Asegúrate de hacer una copia de seguridad antes de continuar."
fi
