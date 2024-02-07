from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, HttpUrl

class User(BaseModel):
    login: str
    id: int
    node_id: str
    avatar_url: HttpUrl
    gravatar_id: str
    url: HttpUrl
    html_url: HttpUrl
    followers_url: HttpUrl
    following_url: HttpUrl
    gists_url: HttpUrl
    starred_url: HttpUrl
    subscriptions_url: HttpUrl
    organizations_url: HttpUrl
    repos_url: HttpUrl
    events_url: HttpUrl
    received_events_url: HttpUrl
    type: str
    site_admin: bool
    name: Optional[str] = None
    company: Optional[str] = None
    blog: Optional[str] = None
    location: Optional[str] = None
    email: Optional[str] = None
    hireable: Optional[bool] = None
    bio: Optional[str] = None
    twitter_username: Optional[str] = None
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: datetime
    updated_at: datetime
