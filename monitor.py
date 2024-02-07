from helpers.cache import fetch_user, fetch_new
from typing import Optional

class _GitHub:
    def __init__(self):
        self.user_cache = {}

    def validate(self, username: str) -> Optional[str]:
        old_user = self.user_cache.setdefault(username, fetch_user(username)) if self.user_cache.get(username) else self.user_cache.get(username)
        time.sleep(30)
        new_user = fetch_new(old_user.id) if old_user else None

        return new_user.login if (old_user and new_user and old_user.login != new_user.login) else None

if __name__ == "__main__":
    monitor = _Github()
    result = monitor.validate('alluding')
    print(result)
