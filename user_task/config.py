from decouple import config
import logging
from exceptions import ConfigurationError

def get_run_env():
    return config('RUN_ENV', default='LOCAL')

class BaseConfig:
    SECRET_KEY = config('SECRET_KEY')
    ALGORITHM = config('ALGORITHM')
    
class DevConfig(BaseConfig):
    pass

class ProdConfig(BaseConfig):
    pass

def get_config():
    try:
        run_env = get_run_env()
        
        if run_env and str(run_env).upper() == "LOCAL":
            return BaseConfig()
        elif run_env and str(run_env).upper() == "DEV":
            return DevConfig()
        elif run_env and str(run_env).upper() == "UAT":
            return ProdConfig()
        else:
            raise ConfigurationError(f"Invalid RUN_ENV: {run_env}")
    except Exception as err:
        logging.critical(f"Configuration error: {err}")
        raise ConfigurationError(f"Error getting configuration: {err}")