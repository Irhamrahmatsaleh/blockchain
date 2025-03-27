from fastapi import APIRouter, Depends

from backend.api import routes
from ..middleware.auth import JWTBearer


@routes.get("/balance", dependencies=[Depends(JWTBearer())])
def get_balance():
    return {"balance": "0.0 NTR"}
