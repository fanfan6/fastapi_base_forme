from pydantic import AnyHttpUrl
from typing import List
import os


class Settings:
    ENV = os.environ.get("fast_env", "DEV")  # 测试环境
    # ENV = os.environ.get("fast_env", "PRD")  # 生产环境
    APP_NAME = "fastapi-base"
    # api前缀
    API_PREFIX = "/audit/v3"
    # jwt密钥,建议随机生成一个
    SECRET_KEY = "ShsUP9qIP2Xui2GpXRY6y74v2JSVS0Q2YOXJ22VjwkI"
    # token过期时间
    ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60
    # 跨域白名单
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:9528"]
    # db配置
    DB_URL = "mysql+pymysql://root:root@127.0.0.1:55001/shenpi_db_test"
    # 启动端口配置
    PORT = 9988
    # 是否热加载
    RELOAD = True
    # log 路径
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    LOG_PATH = os.path.join(BASE_DIR, 'logs')


settings = Settings()
