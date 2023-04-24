from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/file")
async def file():
    with open('./test.json') as test_json_file:
        test_json = test_json_file.read()
        return test_json