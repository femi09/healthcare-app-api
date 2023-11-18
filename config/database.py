from masoniteorm.connections import ConnectionResolver
from .settings import settings

DATABASES = {
    "default": "postgres",
    "postgres": {
        "host": settings.database_hostname,
        "driver": "postgres",
        "database": settings.database_name,
        "user": settings.database_username,
        "password": settings.database_password,
        "port": settings.database_port,
        "log_queries": False,
        "options": {
            #
        }
    },
    "sqlite": {
        "driver": "sqlite",
        "database": "db.sqlite3",
    }
}
DB = ConnectionResolver().set_connection_details(DATABASES)
