from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from routers import acs
from routers import adt

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(acs.router)
app.include_router(adt.router)

# Api documentation
@app.get("/")
def docs_redirect():
    return RedirectResponse(url='/docs')
