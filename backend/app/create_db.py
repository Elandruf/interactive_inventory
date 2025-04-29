from .database import Base, engine
from .models import Item

print("Creando tablas en la base de datos...")
Base.metadata.create_all(bind=engine)
print("Tablas creadas correctamente.")