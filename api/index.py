import os
from flask import jsonify

@app.route("/api/debug")
def debug_env():
    return jsonify({
        "client_id_exists": bool(os.getenv("SPOTIFY_CLIENT_ID")),
        "client_secret_exists": bool(os.getenv("SPOTIFY_CLIENT_SECRET")),
        "refresh_token_exists": bool(os.getenv("SPOTIFY_REFRESH_TOKEN"))
    })
