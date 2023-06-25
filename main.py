from fastapi import FastAPI, Request
from datetime import datetime
from tracker import visitor_tracker
from controllers import new_log, all_logs

app = FastAPI()


@app.middleware("tracker")
async def tracker(request: Request, call_next):
    tracker = visitor_tracker(request)
    print(tracker)
    
    log = new_log(tracker["ip_address"], tracker["request_url"], tracker["request_port"],
                      tracker["request_path"], tracker["request_method"],
                      tracker["browser_type"], tracker["operating_system"],tracker["request_time"])
    print(log)
    
        
    
    response = await call_next(request)
    return response

    
@app.get("/logs")
def logs():
    logs = all_logs()
    return logs

@app.get("/")
def index():
    return "Hello, world"

@app.get("/json")
def some_func():
    return {
        "some_json": "Some Json"
    }





if __name__ == "__main__":
    app.run(port=5000)
