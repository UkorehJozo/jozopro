from fastapi import FastAPI

app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/")
async def root():
  return "Jozo!"
