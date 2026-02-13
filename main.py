import uvicorn

# Run the FastAPI application using Uvicorn
# uvicorn src.app:app --reload
if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)