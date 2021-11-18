from fastapi import FastAPI, APIRouter, Response, Request

from microblog import blog
from core.database import SessionLocal

app = FastAPI()
app.include_router(blog.router, prefix="/blog")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

