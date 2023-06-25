from fastapi import FastAPI, Request
from datetime import datetime
from tracker import visitor_tracker

app = FastAPI()


@app.middleware("tracker")
async def tracker(request: Request, call_next):
    tracker = visitor_tracker(request)
    response = await call_next(request)
    print(tracker)
    return response


@app.get("/")
def index():
    return "Hello, world"

@app.get("/json")
def some_func():
    return {
        "some_json": "Some Json"
    }





if __name__ == "__main__":
    app.run(debug=True)
