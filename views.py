from flask import Blueprint, redirect, url_for, render_template

views = Blueprint("views", __name__)

@views.route("/") #define function then put decorator above, define route, then
def home(): #run whenever hits the root ("/" home route this case)
    return render_template("index.html", content="yay", number="1", y=1, namelist=["mary","tom","alex"])

@views.route("/admin")
def admin():
    return redirect(url_for("views.home"))

@views.route("/<name>")
def user(name):
    return f"Hello {name}, welcome to my webpage!"