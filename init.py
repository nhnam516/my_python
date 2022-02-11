from flask import Flask

app = Flask(__name__) #initialize the Flask application (?)
app.config["SECRET_KEY"] = "sdfdgfadssdfgdggdfdg"
#encrypt cookie, session data related to the website, random string, dont share with anybody

from .views import views, admin #tell flask where are blueprints that contains views/url for application
from .auth import auth
app.register_blueprint(views, url_prefix="/")
app.register_blueprint(auth, url_prefix="/") #how to access the url in these blueprint files, the path through / (or /auth then through /hiunam/website/auth)

