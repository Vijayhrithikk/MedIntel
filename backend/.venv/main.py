from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.project_router import router as project_router
from routes.documet_router import router as document_router
from routes.chat_router import router as chat_router

# #test
# from database.connection import engine, Base
# import database.models

# Base.metadata.create_all(bind=engine)





app = FastAPI()
app.include_router(project_router)
app.include_router(document_router)
app.include_router(chat_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



@app.get("/")
def root():

    return {
        "message": "MedIntel Backend running"
    }