from passlib.context import CryptContext
from BlogPosts.schemas import CreateUser

pwd_ext = CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hash():
    def bcrypt (password:str):
        return pwd_ext.hash(password)
        

    def verify_password(plain_password,hashed_password):
        return pwd_ext.verify(plain_password,hashed_password)