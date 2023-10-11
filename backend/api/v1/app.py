from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routers.student import student_router
from api.v1.routers.note import note_router
from api.v1.routers.s_class import class_router
from api.v1.routers.subject import subject_router


app = FastAPI(
        title="Synelia Full Stack Job Assessment API",
        docs_url="/"
        )


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(student_router)
app.include_router(note_router)
app.include_router(class_router)
app.include_router(subject_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
