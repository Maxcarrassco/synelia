from fastapi import FastAPI
from api.v1.routers.student import student_router
from api.v1.routers.note import note_router


app = FastAPI(
        title="Synelia Full Stack Job Assessment API",
        docs_url="/"
        )


@app.get("/status")
def status():
    return { "status": "OK" }

app.include_router(student_router)
app.include_router(note_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
