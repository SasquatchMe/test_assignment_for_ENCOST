import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config import settings
from routes import router as endpoint_states_router

app = FastAPI(
    debug=True,
    description="Test Assignment for ENCOST",
    docs_url="/api/docs",
    title="ENCOST",
)

app.include_router(
    router=endpoint_states_router,
)

register_tortoise(
    app=app,
    db_url=settings.DB_URL,
    modules=settings.MODULES,
    generate_schemas=False,
    add_exception_handlers=True,
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
