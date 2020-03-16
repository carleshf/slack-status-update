
#!/usr/bin/python3

import config
import requests

if __name__ == "__main__":

    url = "https://slack.com/api/users.profile.set"
    header = { "Content-type": "application/json; charset=utf-8",
        "Authorization": "Bearer {0}".format( config.xoxp_token )
    }

    body = { 
        "profile": {
            "status_text": config.text,
            "status_emoji": config.emoji
        } 
    }

    data = requests.post( url , headers = header, data = body )

    print( data.status_code )
    print( data.json() )

