from fastapi import FastAPI
from src.routes import users, items

app = FastAPI()

# 包含路由
app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "欢迎使用FastAPI应用"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)