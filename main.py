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
def index(request: Request):
    """Track website visitor."""
    ip_address = request.client.host
    request_url = request.url._url
    request_port = request.url.port
    request_path = request.url.path
    request_method = request.method
    request_time = datetime.now()
    browser_type = request.headers["User-Agent"]
    operating_system = request.headers["Accept"]

    return {
        "ip_address": ip_address,
        "request_url": request_url,
        "request_port": request_port,
        "request_path": request_path,
        "request_method": request_method,
        "request_time": request_time,
        "browser_type": browser_type,
        "operating_system": operating_system,
    }



if __name__ == "__main__":
    app.run(debug=True)
