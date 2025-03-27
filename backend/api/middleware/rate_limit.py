from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import time

rate_limit_store = {}

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 10, window_seconds: int = 10):
        super().__init__(app)
        self.max_requests = max_requests
        self.window = window_seconds

    async def dispatch(self, request: Request, call_next):
        try:
            client_ip = request.client.host
            current_time = time.time()

            if client_ip not in rate_limit_store:
                rate_limit_store[client_ip] = []

            # Filter only valid timestamps
            request_times = [
                t for t in rate_limit_store[client_ip]
                if current_time - t < self.window
            ]
            rate_limit_store[client_ip] = request_times

            if len(request_times) >= self.max_requests:
                return JSONResponse(
                    status_code=429,
                    content={"detail": "Too many requests. Please wait."}
                )

            rate_limit_store[client_ip].append(current_time)
            response = await call_next(request)
            return response

        except Exception as e:
            return JSONResponse(status_code=500, content={"detail": str(e)})
