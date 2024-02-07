# GitHub Monitor
### Pretty much exactly how it sounds: a simple Python-based tool that uses caching to monitor the username changes of a GitHub account.

# How it works
It works by accepting a username, for example, `alluding`, and it will cache that information such as ID, etc., including both necessary and unnecessary details. The maximum cache duration is around 45 seconds, but we check after approximately 30 seconds to avoid any clashes. We extract the ID from the old cached data and verify it using the `/user` endpoint instead of `/users`. This choice is made because `/users` only accepts a username, whereas `/user` accepts a UID. If the username has changed, it indicates a swap. This method is not foolproof and remains a work in progress. I plan to enhance it by also checking the ID, as someone could claim it, resulting in a mismatch and potential errors.

# FAQ

I should mention this isn't even close to being complete, it's still a WIP.
