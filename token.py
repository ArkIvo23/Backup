from urllib.parse import urlencode

APP_ID = '51814386'

OAUTH_BASE_URL = "https://oauth.vk.com/authorize"

params = {
    "client_id": APP_ID
    "redirect_uri": "https://oauth.vk.com/blank.html",
    "display": "page",
    "scope": ["status", "photos"],
    "response_type": "token"
}

OAUTH_URL = f'{OAUTH_BASE_URL}?{urlencode(params)}'
print(OAUTH_URL)