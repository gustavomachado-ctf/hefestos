import uvicorn

from asgi import app


def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8001)


if __name__ == "__main__":
    main()
