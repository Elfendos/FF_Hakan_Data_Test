import uvicorn
from fastapi import FastAPI
import datetime
from Methods.Rule1 import *
from Methods.Rule2 import *
from Methods.Rule3 import *
from Methods.Rule4 import *
from Methods.Erroneous1 import *
from Methods.Erroneous2 import *
from Methods.Erroneous3 import *
from Methods.Erroneous4 import *
from Methods.Erroneous5 import *


app = FastAPI(
    title="Test API",
    description="Test API descriptiom",
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/",
    redoc_url="/redoc",
)


@app.post("/")
def hello_world():
    data = f"{datetime.datetime.now()} : Hakan, Firefly Test Cases"
    return data


@app.post("/rule1")
def post_rule1():
    return rule1()


@app.post("/rule2")
def post_rule2():
    return rule2()


@app.post("/rule3")
def post_rule3():
    return rule3()


@app.post("/rule4")
def post_rule4():
    return rule4()


@app.post("/erroneous1")
def post_erroneous1():
    return erroneous1()


@app.post("/erroneous2")
def post_erroneous2():
    return erroneous2()


@app.post("/erroneous3")
def post_erroneous3():
    return erroneous3()


@app.post("/erroneous4")
def post_erroneous4():
    return erroneous4()


@app.post("/erroneous5")
def post_erroneous5():
    return erroneous5()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
