import urllib.request
import json
import os

def handler(request):
    body = request.body
    api_key = os.environ.get("GROQ_API_KEY", "")
    
    groq_req = urllib.request.Request(
        "https://api.groq.com/openai/v1/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )
    
    try:
        r = urllib.request.urlopen(groq_req, timeout=30)
        result = r.read().decode()
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": result
        }
    except urllib.error.HTTPError as e:
        return {
            "statusCode": e.code,
            "headers": {"Content-Type": "application/json"},
            "body": e.read().decode()
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
