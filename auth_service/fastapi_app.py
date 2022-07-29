from fastapi import FastAPI

from auth_service.router.user_router import user_router


def get_fastapi_app() -> FastAPI:
    app = FastAPI(docs_url="/docs/")
    app.include_router(prefix="/users/", router=user_router)
    return app
