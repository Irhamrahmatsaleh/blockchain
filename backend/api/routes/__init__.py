from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..middleware.rate_limit import RateLimitMiddleware
from ..middleware.validation import InputValidationMiddleware
from .auth_routes import router as auth_router
from fastapi import APIRouter

# Inisialisasi aplikasi FastAPI
app = FastAPI()

# Menambahkan CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Gantilah sesuai kebutuhan
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Menambahkan custom middlewares
app.add_middleware(RateLimitMiddleware)
app.add_middleware(InputValidationMiddleware)

# Impor router di sini untuk menghindari circular import
from .wallet_routes import router as wallet_router
from .transaction_routes import router as transaction_router
from .mining_routes import router as mining_router
from .network_routes import router as network_router
from ..websocket.events import router as websocket_router

# Menambahkan router ke aplikasi FastAPI
app.include_router(wallet_router)
app.include_router(transaction_router)
app.include_router(mining_router)
app.include_router(network_router)
app.include_router(websocket_router)
app.include_router(auth_router)

@app.get("/ping")
def ping():
    return {"message": "pong"}
