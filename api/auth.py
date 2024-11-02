from fastapi import APIRouter, Depends

from fastapi.security import OAuth2PasswordRequestForm

from models.auth import UserCreate, Token
router = APIRouter(
    prefix='/auth',
)

@router.post('/sing-up', response_model=Token)
def sing_up(user_data: UserCreate):
    pass

@router.post('/sing-in', response_model=Token)
def sing_in(form_data: OAuth2PasswordRequestForm = Depends()):
    pass



