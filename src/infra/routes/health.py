from fastapi import APIRouter
from datetime import datetime
from pydantic import BaseModel

router = APIRouter(
    prefix='/health',
    tags=['health'],
    responses={404: {'description': 'Not found'}}
)


class HealthResponse(BaseModel):
    time: datetime
    status: bool 


@router.get('/', response_model=HealthResponse)
def get_health():
    response = HealthResponse(time=datetime.utcnow(), status=True)
    return response