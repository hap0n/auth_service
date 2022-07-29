import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI


def main():
    load_dotenv(os.getenv("ENV_FILE", "../.env.test"))
    print(os.getenv("POSTGRES_PORT"))

    from auth_service.router.user_router import user_router

    app = FastAPI(docs_url="/docs/")
    app.include_router(prefix="/users", router=user_router)
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
        loop="asyncio",
    )


if __name__ == "__main__":
    main()
