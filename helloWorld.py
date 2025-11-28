from fastapi import FastAPI, Depends

app = FastAPI()


@app.get("/hello")
def hello():
   return("Hello World!")



# اگر پروژه را با این دستور اجرا کرده‌ای:
# uvicorn main:app --reload
# خروجی چیزی شبیه این است:
# http://127.0.0.1:8000

# in browser: http://127.0.0.1:8000/hello

