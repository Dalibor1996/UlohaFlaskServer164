from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Lubim Bobu :*</p>"
#
# @app.route("/about")
# def about():
#     return"O stranke"

@app.route("/user/<username>") #zobaciky u naznacuju ze sa jedna o premennu
def show_user_profile(username):
    #username = "Veronika" #toto nemusis robit lebo cokolvek tam napises do url tak to pojde lebo je to menitelne
    return f"Profil uzivatela {username}"
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"zobrazujem prispevok s ID {post_id}"

@app.route("/<username>/<project_name>/blob/<branch>/<file>") #zobaciky u naznacuju ze sa jedna o premennu
def show_git_file(username, project_name, branch, file):
    #username = "Veronika" #toto nemusis robit lebo cokolvek tam napises do url tak to pojde lebo je to menitelne
    return f"Profil uzivatela {username} <br> nazov projektu je {project_name} <br> nazov branche je {branch} <br> nazov fileu je {file}"
if __name__ == '__main__':
    app.run()
