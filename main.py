from flask import Flask, redirect
import os

app = Flask(__name__)

WHATSAPP_CHANNEL = "https://whatsapp.com/channel/0029VbByMEkIyPtP7HiYX83L"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(WHATSAPP_CHANNEL, code=302)
    
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
  
