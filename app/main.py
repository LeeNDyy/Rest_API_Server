from fastapi import FastAPI
from app.routers import contact, group
import os
import uvicorn


app = FastAPI()

app.include_router(contact.router)
app.include_router(group.router)

@app.get("/")
async def root():
    return {"message": "API is working"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 6080))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)