import os
from typing import List

from bson import ObjectId
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field

app = FastAPI()

# MongoDB connection
MONGO_URL = os.getenv("MONGO_URL", "mongodb://client_portfolio:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client.portfolio
collection = db.client_portfolio


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "details": str(exc)}
    )


@app.get("/")
async def get_data():
    try:
        print(collection)
        data = await collection.find().to_list(length=None)
        for item in data:
            item["_id"] = str(item["_id"])
            item["createdDate"] = item["createdDate"].isoformat()
        return data
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal Server Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
