# Copiar la base de datos desde el contenedor al sistema local (antes de detener y eliminar el contenedor)
docker cp mpando_portfolio:/app/db.sqlite3 ../backups/db.sqlite3

# Copiar la carpeta "media" desde el contenedor al sistema local sin crear carpetas adicionales
docker cp mpando_portfolio:/app/media ../backups/
