from typing import Dict

from fastapi import APIRouter

router = APIRouter(prefix='/base')


@router.get('/ping')
async def pong() -> Dict[str, str]:
    return {'result': 'pong'}
