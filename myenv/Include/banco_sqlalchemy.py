# Implementando um Banco de Dados Relacional com SQLAlchemy

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Criando a engine e a sessão do banco de dados SQLite
engine = create_engine('sqlite:///banco.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Definindo as classes Cliente e Conta
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    contas = relationship("Conta", back_populates="cliente")

class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    cliente = relationship("Cliente", back_populates="contas")

# Criando o esquema do banco de dados
Base.metadata.create_all(engine)

# Inserindo dados de exemplo
cliente1 = Cliente(nome='João')
cliente2 = Cliente(nome='Maria')
session.add_all([cliente1, cliente2])
session.commit()

conta1 = Conta(numero='123', saldo=1000, cliente=cliente1)
conta2 = Conta(numero='456', saldo=2000, cliente=cliente2)
session.add_all([conta1, conta2])
session.commit()

# Recuperando dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print("Cliente:", cliente.nome)
    for conta in cliente.contas:
        print("Conta:", conta.numero, "Saldo:", conta.saldo)

session.close()
