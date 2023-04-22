#!/usr/bin/env python3

#from __future__ import annotations # type hint to return 'self', this conflicts with typing.Annotated or APIRouter

import yaml, io
from typing                  import Any, Annotated
from pydantic                import BaseModel, Field, Extra

from fastapi                 import FastAPI,  Path
from fastapi.responses       import Response
from classy_fastapi          import Routable, get, delete


class User(BaseModel):
      name: str = Field(description="user name", example='Anonymous')
      class Config:
          extra = Extra.allow                             # let pydantic to know using extra properties
          schema_extra = { 'additionalProperties': True } # let openapi schema to know using additional properties

class MyClassBasedView(Routable):
   """Inherits from Routable.
   alternatives of Class Based View for FastAPI is discussed at https://github.com/tiangolo/fastapi/discussions/8991
   """

   def __init__(self) -> None:
       """Constructor. """
       super().__init__()
       self.users = {}

   def attachRoutes(self, app: FastAPI, **kwargs: dict[str,Any]) -> FastAPI:
       """Let app dispatch requests to this class methods.

       example of kwargs: prefix="/"
       """
       app.include_router(self.router, **kwargs)
       return app
   
#  def addUsers(self, users: list[User]) -> RouteUser:   # when    from __future__ import annotations
   def addUsers(self, users: list[User]) -> "RouteUser": # when NO from __future__ import annotations
       for u in users:
           self.users[u.name] = u
       return self

   def getUsers(self) -> dict[str, User]:
       return self.users

   @get('/user/', operation_id='getUser', response_model=dict[str,User])
   def get_users(self) -> dict[str,User]:
       return self.getUsers()

   @get('/user/{name}', operation_id='getUserByName', response_model=User)
   def get_user_by_name(self, name: Annotated[str, Path(description='name of user', example='A')]) -> User:
       return self.users.get(name, None)

   @delete('/user/{name}', operation_id='delUserByName')
   def delete_user(self, name: Annotated[str, Path(description='name of user', example='A')]) -> None:
       # delete key from dict if it exists in safe
       self.users.pop(name, None)



users = [ User(name='A'), User(name='B') ]
inst = MyClassBasedView()
inst = inst.addUsers(users)
print (inst.getUsers())

app = FastAPI()
inst.attachRoutes(app) # == app.include_router(inst.router)

# enable openapi.yaml, cf. https://github.com/tiangolo/fastapi/issues/1140
@app.get('/openapi.yaml', include_in_schema=False)
def getOpenapiYaml():
    openapi_dict= app.openapi()
    yaml_s = io.StringIO()
    yaml.dump(openapi_dict, yaml_s,sort_keys=False, allow_unicode=True)
    return Response(yaml_s.getvalue(), media_type='text/yaml')
