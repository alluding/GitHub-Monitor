# GitHub Monitor
### Pretty much exactly how it sounds: a simple Python-based tool that uses caching to monitor the username changes of a GitHub account.

# How It Works
The tool operates by taking a username, such as `alluding`, and caching relevant information like the ID, etc., encompassing both necessary and unnecessary details. The maximum cache duration is approximately 45 seconds, but we check after around 30 seconds to avoid potential conflicts.

We retrieve the ID from the old cached data and verify it using the `/user` endpoint instead of `/users`. This decision is made because /users only accepts a username, while `/user` accepts a UID. If the username has changed, it indicates a swap.

This method is not foolproof and remains a work in progress. I plan to enhance it by also verifying the ID, as someone could claim it, leading to a mismatch and potential errors.

# FAQ

I should mention this isn't even close to being complete, it's still a WIP.
