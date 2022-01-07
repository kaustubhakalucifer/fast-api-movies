from fastapi import FastAPI
app = FastAPI()

movies = [{"title": "Batman", "year": 2005}]

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/movies")
def get_movies():
    return movies