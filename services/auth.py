# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from models.users import User
# from services.users import UserService
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
# def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
#     user = UserService.get_user_by_token(token)
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid authentication credentials",
#         )
#     return user
#
# def get_current_admin_user(current_user: User = Depends(get_current_user)) -> User:
#     if not current_user.is_admin:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Access denied. Admins only."
#         )
#     return current_user