from fastapi import APIRouter

router = APIRouter(
    prefix='/auth',
)

SECRET_KEY = '7oHQyjS2lQIcK7k1pfyWE0KnywC3fp2O'
ALGORITHM = 'HS256'

@router.post('/sing-up')
def sung_up():
    pass

@router.post('/sing-in')
def sing_in():
    pass



