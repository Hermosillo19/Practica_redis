import os
from dataclasses import dataclass
from redis import Redis
from dotenv import load_dotenv

load_dotenv()
@dataclass(frozen=True)
class ConfiguracionRedis:
    url:str

def ObtenerConfiguracion() -> ConfiguracionRedis:

    url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    return ConfiguracionRedis(url=url)

def ObtenerConexion() -> Redis :
    config = ObtenerConfiguracion()
    conexion = Redis.from_url(config.url , decode_responses=True)
    conexion.ping()
    return conexion