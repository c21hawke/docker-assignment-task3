from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/contact")
async def root():
    return {"contact_details":"https://github.com/c21hawke/"}
