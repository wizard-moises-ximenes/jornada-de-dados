from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///meubanco.db', echo=True)
print("Conexão estabelecida com sucesso!")
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()