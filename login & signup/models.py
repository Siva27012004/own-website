from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer,Float
from database import base,db_engine



class Department(base):
    __tablename__='employee_details'

    id=Column(Integer,index=True,autoincrement=True, primary_key=True,nullable=False)
    Department=Column(String(255),index=True,nullable=False)
    Status=Column(String(255),index=True,nullable=False)
    Created_by=Column(String(255),index=True,nullable=False)
    Created_at=Column(String(255),index=True,nullable=False)


base.metadata.create_all(bind=db_engine)
