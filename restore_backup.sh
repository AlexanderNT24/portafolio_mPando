# Copiar la base de datos desde el sistema local al contenedor
docker cp ../backups/db.sqlite3 mpando_portfolio:/app/db.sqlite3

docker exec -it mpando_portfolio rm -rf /app/media/
# Copiar la carpeta "media" desde el sistema local al contenedor
docker cp ../backups/media mpando_portfolio:/app/media/

