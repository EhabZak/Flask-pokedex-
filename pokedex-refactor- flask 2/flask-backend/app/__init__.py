
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask, render_template, redirect
from .config import Configuration
import os
from .routes.pokemon import pokemon


#/////////////////////////////////////////////////
app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(pokemon, url_prefix= "/api/pokemon")


# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
