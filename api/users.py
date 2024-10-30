from fastapi import APIRouter

router = APIRouter(
    prefix='/users',

)

@router.get('/')
def get_users():
    return []

@router.get('/{user_id}')
def get_user_by_id():
    return []

