# cf. https://stackoverflow.com/questions/63069190/how-to-capture-arbitrary-paths-at-one-route-in-fastapi

from fastapi import FastAPI, Request, WebSocket, UploadFile, File, Header, Body
from typing import Annotated, Any
import json

app = FastAPI()

@app.post("/anycontent")
async def anyContent(req: Request,
    content_type: str        = Header(description="Content-Type"),
    body:         Any|None   = Body(description="Content"),
    x_filename:   str|None   = Header(None, description="Name of Content(filename)"),
    ):

#   Example handling for common content types
#   ctype = req.headers.get("content-type", "application/octet-stream")
#   if "application/json" in ctype:
#       data = await req.json()
#   elif "text/" in ctype:
#       data = (await req.body()).decode("utf-8")
#   else:
#       data = await req.body()

    return {
            "Content-Type":   content_type,
            "Content-Length": int( req.headers.get("content-length", 0)),
            "type(body)":     type(body).__name__,
            "x-file-name":    x_filename,
           }


@app.post("/upload")
async def upload(file: UploadFile = File(...) ):
    print(f"Content-Type: {file.content_type}")
    contents = await file.read()
    return {"filename": file.filename,
            "content-type": file.content_type,
            "size": file.size
           }

@app.get    ("{full_path:path}")
@app.put    ("{full_path:path}")
@app.post   ("{full_path:path}")
@app.delete ("{full_path:path}")
@app.options("{full_path:path}")
@app.patch  ("{full_path:path}")
@app.trace  ("{full_path:path}")
async def catch_all(req: Request, full_path: str):
    body = await req.body() or '{}'
    body = json.loads(body)

#   print( {"path" : full_path, "headers": req._headers, "query": req._query_params.items(),  "reqScope": dict(req.scope) })
    input ={ "method": req.scope.get("method"), "url": req.url._url, "query": dict(req._query_params),  "body": body, "Authorization": req._headers.get('Authorization'), "host" : req._headers.get('host'), "headers": dict(req._headers) }
    print(input)
    return input

@app.websocket("{full_path:path}")
async def catch_websocket(ws:WebSocket, full_path: str):
    await ws.accept()
    input = { "full_path": full_path, "query": dict(ws._query_params), "headers": dict(ws._headers) }
    await ws.send_text(f'new websocket connection: {input}')
    while True:
       try:
          msg = await ws.receive_text()
          await ws.send_text(f'got: {msg}')
       except:
          break
