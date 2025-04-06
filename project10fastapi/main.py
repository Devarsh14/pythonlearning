from fastapi import FastAPI

app = FastAPI()

# debug configuration
#https://www.jetbrains.com/help/pycharm/fastapi-project.html#run-debug-configuration
# https://fastapi.tiangolo.com/tutorial/debugging/#about-__name__-__main__

@app.get("/")
async def root():
    number = 5 + 7
    return {"message": f"Hello World{number}"}