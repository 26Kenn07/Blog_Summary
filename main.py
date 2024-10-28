from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from app.routes import summary

app = FastAPI()
app.include_router(summary.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy"}