import unirest
import json

class Lifecycle

    def __init__(self, api_key):
        self.apiKey = api_key

    def identify(params):
        response = unirest.post("http://localhost:3400/v1/identify", headers={ "Content-Type": "application/json", "lifecycle-api-key":  },
          params=json.dumps(params)
        )

    def track(event_id, unique_id):
        response = unirest.post("http://localhost:3400/v1/track", headers={ "Content-Type": "application/json", "lifecycle-api-key":  },
          params=json.dumps({
            "event_id": event_id,
            "unique_id": unique_id
          })
        )
