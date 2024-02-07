from helpers.utils._cache import cache
from helpers.utils.obj import User

from typing import Optional
import requests

BASE_API_URL = "https://api.github.com/users/" 
NEW_API_URL = "https://api.github.com/user/" 

@cache(seconds=45)
def fetch_user(username: str) -> Optional[User]:
    response = requests.get(BASE_API_URL + username)
    return User(**response.json()) if response.status_code == 200 else None

def fetch_new(uid: int) -> Optional[User]:
    response = requests.get(NEW_API_URL + str(uid))
    return User(**response.json()) if response.status_code == 200 else None
