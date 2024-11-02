# from fastapi import APIRouter
# from fastapi import Depends
#
# from models.users import User
# from typing import List
# from services import auth
# from services.users import UserService
#
# router = APIRouter(
#     prefix='/users',
#
# )
#
# @router.get('/', response_model=List[User])
# def get_users(
#     services: UserService = Depends(),
#    # current_user: User = Depends(auth.get_current_admin_user)
# ):
#     return services.get_list()
#
# @router.get('/{user_id}')
# def get_user_by_id():
#     return []

