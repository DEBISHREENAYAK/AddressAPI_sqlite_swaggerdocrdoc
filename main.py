from typing import List 
import databases 
import sqlalchemy 
from fastapi import FastAPI, status 
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel

#seting up the Database 
DATABASE_URL = "sqlite:///mydb.db"    # the db name is mydb
database = databases.Database(DATABASE_URL) 
metadata = sqlalchemy.MetaData() 

# Creating the table named " address " 

addressdetails = sqlalchemy.Table( 
  "address", 
  metadata, 
  sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True), 
  sqlalchemy.Column("name", sqlalchemy.String), 
  sqlalchemy.Column("country", sqlalchemy.String), 
  sqlalchemy.Column("phone", sqlalchemy.Integer), 
) 


engine = sqlalchemy.create_engine( DATABASE_URL ) 
metadata.create_all(engine) 

#the model classes
class AddressIn(BaseModel): 
  name: str 
  country : str
  phone: int

class Address(BaseModel): 
  id: int 
  name: str 
  country : str
  phone: int
  
#the title  
app = FastAPI(title = "ADDRESS REST API with FastAPI ") 

#using middlewares . middleware in FastAPI is used to filter and process HTTP requests and responses that move through the REST API.
app.add_middleware( 
  CORSMiddleware, 
  allow_origins=["*"], 
  allow_credentials=True, 
  allow_methods=["*"], 
  allow_headers=["*"], 
) 

#connect and disconnect with database
@app.on_event("startup") 
async def startup(): 
  await database.connect() 

@app.on_event("shutdown") 
async def shutdown(): 
  await database.disconnect() 
  
# A skip query parameter that is an int, with a default of 0.
# A limit query parameter that is an int, with a default of 100.  
# Get method , we will get all the records 
@app.get("/addressdetails/", response_model=List[Address], status_code = status.HTTP_200_OK) 
async def read_addressdetails(skip: int = 0, take: int = 20): 
  query = addressdetails.select().offset(skip).limit(take)   
  return await database.fetch_all(query)   

# Get method , we will get  the specfied record data accoding to the addr_id 
@app.get("/addressdetails/{addr_id}/", response_model=Address, status_code = status.HTTP_200_OK) 
async def read_addressdetails(addr_id: int): 
  query = addressdetails.select().where(addressdetails.c.id == addr_id) 
  return await database.fetch_one(query) 
 
# Post method , in this endpoit we enter the records ( all thee fields of address table take data from here)   
@app.post("/addressdetails/", response_model=Address, status_code = status.HTTP_201_CREATED) 
async def create_addressdetails(addr: AddressIn): 
  query = addressdetails.insert().values(name=addr.name, country=addr.country, phone=addr.phone) 
  last_record_id = await database.execute(query) 
  return {**addr.dict(), "id": last_record_id} 

# Put method , in this endpoint we update the record/ details according to the addr_id
@app.put("/addressdetails/{addr_id}/", response_model=Address, status_code = status.HTTP_200_OK) 
async def update_todo(addr_id: int, payload: AddressIn): 
  query = addressdetails.update().where(addressdetails.c.id == addr_id).values(name=payload.name, country=payload.country, phone=payload.phone) 
  await database.execute(query) 
  return {**payload.dict(), "id": addr_id} 

# To delete any record , accoding to the addr_id , we use this end point
@app.delete("/addressdetails/{addr_id}/", status_code = status.HTTP_200_OK) 
async def delete_todo(addr_id: int): 
  query = addressdetails.delete().where(addressdetails.c.id == addr_id) 
  await database.execute(query) 
  return {"message": "Address ID: {} deleted successfully!".format(addr_id)}