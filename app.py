from fastapi import FastAPI
import uvicorn
from blueprints import user,auth,admin # not used but important for routing (won't work if removed)
import blueprints

app = FastAPI()

app.include_router(blueprints.auth_router)
app.include_router(blueprints.admin_router)
app.include_router(blueprints.user_router)

@app.get("/")
async def default():
    print("default main")
    return {"message": "default main"}

@app.get("/api/test/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run('app:app', host="0.0.0.0", port=5000, reload=True)
