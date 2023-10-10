from fastapi import FastAPI
from api.v1.routers.student import student_router
from api.v1.routers.note import note_router
from api.v1.routers.s_class import class_router
from api.v1.routers.subject import subject_router


app = FastAPI(
        title="Synelia Full Stack Job Assessment API",
        docs_url="/"
        )


app.include_router(student_router)
app.include_router(note_router)
app.include_router(class_router)
app.include_router(subject_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
