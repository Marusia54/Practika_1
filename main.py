from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def f_index():
    return {"ФИО: Мозер Мария Олеговна"}


@app.get('/tools')
async def f_indexT():
    return {"Начальные навыки"}


@app.get('/users')
async def f_indexU():
    return "+7 902 140 38-14"

