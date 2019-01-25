import datetime

from flask import Flask, render_template, url_for, redirect
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_login import logout_user 

from flask_dance.consumer import OAuth2ConsumerBlueprint
from functools import partial
from flask.globals import LocalProxy, _lookup_app_object
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

import requests


# def make_facebook_blueprint(
#         client_id=None, client_secret=None, scope=None, redirect_url=None,
#         redirect_to=None, login_url=None, authorized_url=None,
#         session_class=None, backend=None):
#     """
#     Make a blueprint for authenticating with Facebook using OAuth 2. This requires
#     a client ID and client secret from Facebook. You should either pass them to
#     this constructor, or make sure that your Flask application config defines
#     them, using the variables FACEBOOK_OAUTH_CLIENT_ID and FACEBOOK_OAUTH_CLIENT_SECRET.

#     Args:
#         client_id (str): The client ID for your application on Facebook.
#         client_secret (str): The client secret for your application on Facebook
#         scope (str, optional): comma-separated list of scopes for the OAuth token
#         redirect_url (str): the URL to redirect to after the authentication
#             dance is complete
#         redirect_to (str): if ``redirect_url`` is not defined, the name of the
#             view to redirect to after the authentication dance is complete.
#             The actual URL will be determined by :func:`flask.url_for`
#         login_url (str, optional): the URL path for the ``login`` view.
#             Defaults to ``/facebook``
#         authorized_url (str, optional): the URL path for the ``authorized`` view.
#             Defaults to ``/facebook/authorized``.
#         session_class (class, optional): The class to use for creating a
#             Requests session. Defaults to
#             :class:`~flask_dance.consumer.requests.OAuth2Session`.
#         backend: A storage backend class, or an instance of a storage
#                 backend class, to use for this blueprint. Defaults to
#                 :class:`~flask_dance.consumer.backend.session.SessionBackend`.

#     :rtype: :class:`~flask_dance.consumer.OAuth2ConsumerBlueprint`
#     :returns: A :ref:`blueprint <flask:blueprints>` to attach to your Flask app.
#     """
#     facebook_bp = OAuth2ConsumerBlueprint("facebook", __name__,
#         client_id=client_id,
#         client_secret=client_secret,
#         scope=scope,
#         base_url="https://graph.facebook.com/",
#         authorization_url="https://www.facebook.com/dialog/oauth",
#         token_url="https://graph.facebook.com/oauth/access_token",
#         redirect_url=redirect_url,
#         redirect_to=redirect_to,
#         login_url=login_url,
#         authorized_url=authorized_url,
#         session_class=session_class,
#         backend=backend,
#     )
#     facebook_bp.from_config["client_id"] = "535408600284297"
#     facebook_bp.from_config["client_secret"] = "368f549cce50c2e955c571ff7cba95cc"

#     @facebook_bp.before_app_request
#     def set_applocal_session():
#         ctx = stack.top
#         ctx.facebook_oauth = facebook_bp.session

#     return facebook_bp

# facebook = LocalProxy(partial(_lookup_app_object, "facebook_oauth"))

app = Flask(__name__)
app.secret_key = "supersekrit"

blueprint = make_facebook_blueprint(
    client_id="535408600284297",
    client_secret="368f549cce50c2e955c571ff7cba95cc",
)
app.register_blueprint(blueprint)

@app.route('/login')
def root():
    if not facebook.authorized:
        return redirect(url_for("facebook.login"))

    return render_template('index.html')

@app.route('/logout')

def logout():
    logout_user()
    return redirect(url_for("facebook.login"))


@app.route("/")
def login():
    if not facebook.authorized:
        return redirect(url_for("facebook.login"))

    resp = blueprint.session.get("/me?scope=email&fields=id,address,email,first_name,last_name,name,gender,locale,hometown,birthday,picture")

    db_results = requests.get("https://jmb.im/uofthacks/add_to_db.php?uid=" + resp.json()['id'] + "&fname=" + resp.json()['first_name'] + "&sname=" + resp.json()['last_name'] + "&email=" + resp.json()['first_name'] + resp.json()['last_name'] + "@facebook.com")
    subList_results = requests.get("https://jmb.im/uofthacks/get_list_of_subs.php?uid=" + resp.json()['id'])

    actualScript = ""
    subDict = {"netflix" : "Netflix", "spotify" : "Spotify", "hulu" : "Hulu", "apple_music" : "Apple Music", "youtube_premium" : "Youtube Music"}
    people_results = requests.get("https://jmb.im/uofthacks/get_all_users.php")
    people_results = people_results.text

    for sub in subList_results.json():
        sub_results = (requests.get("https://jmb.im/uofthacks/get_sub_info.php?id=" + sub)).json()
        sub_id = sub_results['sub_id']
        service = sub_results['service']
        fee = str(float(sub_results['fee'])/100)
        due = sub_results['due']

        sub_people_results = (requests.get("https://jmb.im/uofthacks/get_users_sharing_sub.php?id=" + sub_id)).json()
        sub_people_list = ""
        
        for subPeople in sub_people_results:
            sharedPeople_results = (requests.get("https://jmb.im/uofthacks/get_name_from_uid.php?uid=" + subPeople)).json()
            sub_people_list = sharedPeople_results["fname"] + " " + sharedPeople_results["sname"] + " (" + sharedPeople_results["email"] + ")" + ", " + sub_people_list

        people = people_results

        icon = "https://jmb.im/uofthacks/icons/" + service + ".png"
        html_Cards_Stuff = ("<div class=\"card bill\"" +
                            "onclick=\"openModal(" + fee + "," + due + "," + sub_id +")\"> <div class=\"card-body\">" +
                            "<div class=\"row\"> <div class=\"col-12 col-md-2\"> <img src=\"" + icon + "\" />" +
                            "</div> <div class=\"col-12 col-md-10\"> <h2>" + subDict[service] + "</h2>" +
                            "<p>You owe: $" + fee +" </p> <small>Due in " + due + " days</small>" + 
                            "</div></div></div></div>")
        actualScript = actualScript + html_Cards_Stuff


        

    return render_template('index.html', name = resp.json()['name'], picture=resp.json()['picture']['data']['url'], uid=resp.json()['id'] ,fee = fee, due = due, people = people_results, sharedList = sub_people_list, ScriptStuff = actualScript)
    




if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.

    app.run(host='127.0.0.1', port=8080, debug=True, ssl_context='adhoc')