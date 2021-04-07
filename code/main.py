import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template
from pathlib import Path

app = fastapi.FastAPI()

fastapi_chameleon.global_init(str(Path(__file__).parent / "templates"))


@app.get("/")
@template(template_file="index.html")
def index():
    return {"user_name": "patrik"}


if __name__ == "__main__":
    uvicorn.run(app)
