import fastapi
import uvicorn
import fastapi_chameleon
from pathlib import Path
from starlette.staticfiles import StaticFiles
from views import account, home, packages

BASE_DIR = Path(__file__).parent

fastapi_chameleon.global_init(str(BASE_DIR / "templates"))


def create_app(configure):
    app = fastapi.FastAPI()
    configure(app)
    return app


def configure(app):
    mount_static_files(app)
    mount_endpoints(app)


def mount_endpoints(app):
    app.include_router(account.router)
    app.include_router(home.router)
    app.include_router(packages.router)


def mount_static_files(app):
    app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


def main(app):
    uvicorn.run(app)


app = create_app(configure)

if __name__ == "__main__":
    main(app)
