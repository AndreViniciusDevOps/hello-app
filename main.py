from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Minha Pipeline CI/CD Funcionando normalmente!"}