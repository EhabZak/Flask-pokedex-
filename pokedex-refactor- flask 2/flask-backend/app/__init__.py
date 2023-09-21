
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask import Flask, render_template, redirect
from .config import Configuration
import os
from .routes.pokemon import pokemon
from flask_migrate import Migrate
from .models.db import db
from .models.pokemon import Pokemon
from .models.item import Item
from .models.pokemon_type import Type


#/////////////////////////////////////////////////
app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(pokemon, url_prefix= "/api/pokemon")
db.init_app(app)
migrate = Migrate(app, db)


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
