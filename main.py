from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def index(request: Request):
    """Track website visitor."""
    ip_address = request.client.host
    browser_type = request.headers["User-Agent"]
    operating_system = request.headers["Accept"]

    return {
        "ip_address": ip_address,
        "browser_type": browser_type,
        "operating_system": operating_system,
    }

if __name__ == "__main__":
    app.run(debug=True)
