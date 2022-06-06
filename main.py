import logging.config

from fastapi import FastAPI

from environment.config import VERSION, DEBUG, PROJECT_NAME, LOGGING_CONFIG, HOST, PORT

from routes import lb


app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)


# настройка логгера
logging.config.dictConfig(LOGGING_CONFIG)

# добавляем эндпоинты
app.include_router(lb.router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)
