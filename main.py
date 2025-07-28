from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "✅ GBTNetwork Backend is Live"}

@app.post("/")
async def handle_rpc(request: Request):
    body = await request.json()
    return JSONResponse({
        "jsonrpc": "2.0",
        "id": body.get("id"),
        "result": "Simulated GBTNetwork RPC response"
    })
