from fastapi import FastAPI
import uvicorn

from routes import router

class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup()

    def setup(self):
        self.include_router(router)     

def get_app():
    app = App()
    return app

if __name__ == "__main__":
    app = get_app()
    uvicorn.run(app, host="127.0.0.1", port=8000)
