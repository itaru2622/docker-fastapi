from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, Field, Extra

class Msg(BaseModel):
    message: Union[str,None] = Field(None, description='human readable message')

class Record(BaseModel):
    item_id: int = Field(0, description='item ID')
    q: Union[str,None] = Field(None, description='human readable string')
    class Config:
      extra = Extra.allow                             # let pydantic to know using extra properties
      schema_extra = { 'additionalProperties': True } # let openapi schema to know using additional properties


app = FastAPI()

@app.get("/", operation_id='getroot', response_model=Msg)
def read_root():
    return Msg( message='Hello World')


@app.get("/items/{item_id}", operation_id='getitems', response_model=Record)
def read_item(item_id: int, q: Union[str, None] = None):
    rtn = Record(item_id=item_id, q=q, extra_field='extra val')
    return rtn
