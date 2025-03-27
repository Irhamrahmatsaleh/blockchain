from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import re
import json

# Regex sederhana untuk deteksi pola berbahaya
ILLEGAL_PATTERN = re.compile(r"(<script|SELECT|INSERT|DELETE|UPDATE|DROP|--|;|--|#|\\|')", re.IGNORECASE)

class InputValidationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method in ["POST", "PUT", "PATCH"]:
            try:
                body = await request.body()
                if body:
                    body_text = body.decode("utf-8")
                    if ILLEGAL_PATTERN.search(body_text):
                        return JSONResponse(
                            status_code=400,
                            content={"detail": "Bad request: Suspicious input detected."}
                        )
            except Exception as e:
                return JSONResponse(status_code=400, content={"detail": f"Input validation failed: {str(e)}"})

        return await call_next(request)
