# app/routes/__init__.py
from .users import bp as users_bp
from .messages import bp as messages_bp
from .parkings import bp as parkings_bp
from .spots import bp as spots_bp

def init_app(app):
    app.register_blueprint(users_bp)
    app.register_blueprint(messages_bp)
    app.register_blueprint(parkings_bp)
    app.register_blueprint(spots_bp)

