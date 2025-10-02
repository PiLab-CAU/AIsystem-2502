from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="My FastAPI Service",
    description="A simple demo API running in Docker. Swagger is at /docs and ReDoc at /redoc.",
    version="0.1.0",
    docs_url="/docs",          # Swagger UI URL
    redoc_url="/redoc",        # ReDoc URL
    openapi_url="/openapi.json" # OpenAPI JSON spec URL
)

class Echo(BaseModel):
    text: str

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Hello, FastAPI in Docker!"}

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}

@app.post("/echo", tags=["Demo"])
def echo(body: Echo):
    return {"you_sent": body.text}