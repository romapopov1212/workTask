from fastapi import FastAPI
import uvicorn
from routers import car, order

app = FastAPI(
    title="Tech Store API",
    description="API для просмотра и заказа техники",
    version="1.0.0"
)


app.include_router(car.router)
app.include_router(order.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
