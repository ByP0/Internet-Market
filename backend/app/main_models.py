from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Pass(Base):
    __abstract__ = True
    
    pass