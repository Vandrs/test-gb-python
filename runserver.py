import uvicorn
from decouple import config

if __name__ == '__main__':

    environment = config('ENVIRONMENT', default='production')

    reload = True if environment == 'development' else False
    debug = config('DEBUG', default=False, cast=bool)
    host = config('HOST', default='0.0.0.0', cast=str)
    port = config('PORT', default=8000, cast=int)
    uvicorn.run("app:app", host=host, port=port, reload=reload, debug=debug)