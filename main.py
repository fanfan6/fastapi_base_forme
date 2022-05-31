from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config import settings
from apis.apis import api_router
import uvicorn
from utils.logger import logger
import time

# 初始化app实例
env = settings.ENV
print(env)
if env != 'DEV':
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI(title=settings.APP_NAME)

@app.middleware("http")
async def log_requests(request, call_next):
    logger.info(f"start request path={request.url.path}")
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"end request path={request.url.path} completed_in={formatted_process_time}ms status_code={response.status_code}")
    
    return response

# 设置CORS站点
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(CORSMiddleware,
                       allow_origins=[str(origin)
                                      for origin in settings.BACKEND_CORS_ORIGINS],
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"],
                       )
# 路由注册
app.include_router(api_router, prefix=settings.API_PREFIX)
if __name__ == '__main__':

    uvicorn.run(app="main:app", host='0.0.0.0',
                port=settings.PORT, reload=settings.RELOAD)
