from auth_service.fastapi_app import get_fastapi_app
import uvicorn


def main():
    uvicorn.run(
        get_fastapi_app(),
        host="0.0.0.0",
        port=8080,
        loop="asyncio",
    )


if __name__ == "__main__":
    main()
