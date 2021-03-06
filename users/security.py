from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)

print(verify_password("asdf", get_password_hash("asdf")))