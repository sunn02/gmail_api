from flask import Flask, redirect

app = Flask(__name__)

@app.route('/login')
def login():
    auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        "?client_id=978144749893-5vlte900a2g9t93qqub58icctq84vlhm.apps.googleusercontent.com"
        "&response_type=code"
        "&scope=https://www.googleapis.com/auth/gmail.readonly"
        "&redirect_uri=http://localhost:8000/oauth2callback"
        "&access_type=offline"
        "&prompt=consent"
    )
    return redirect(auth_url)
