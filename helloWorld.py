from fastapi import FastAPI, Depends

app = FastAPI()


@app.get("/hello")
def hello():
   return("Hello World!")
