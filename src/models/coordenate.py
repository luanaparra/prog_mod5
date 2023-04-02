from models.base import Base
from sqlalchemy import Column, Integer

class Coordenate(Base):
    __tablename__ = "Coordenates"
    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    z = Column(Integer)

    def __repr__(self) -> str:
      return f"Coordenate(id={self.id}, x={self.x}, y={self.y}, z={self.z})"
