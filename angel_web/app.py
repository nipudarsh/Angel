"""FastAPI application factory."""
from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from angel_web.api.routes import auth, repos, search, system, tools


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(title="ANGEL", version="0.1.0")
    app.mount("/static", StaticFiles(directory="angel_web/static"), name="static")
    templates = Jinja2Templates(directory="angel_web/templates")

    @app.get("/", response_class=HTMLResponse)
    def dashboard(request: Request) -> HTMLResponse:
        return templates.TemplateResponse("dashboard.html", {"request": request})

    app.include_router(auth.router, prefix="/api/auth")
    app.include_router(tools.router, prefix="/api/tools")
    app.include_router(repos.router, prefix="/api/repos")
    app.include_router(search.router, prefix="/api/search")
    app.include_router(system.router, prefix="/api/system")

    return app


app = create_app()
