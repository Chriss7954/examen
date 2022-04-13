from bottle import route, run, template
from addition import resultatsomme


@route("/add/<a>/<b>")
def addition(a="0", b="0"):
    resultat = resultatsomme(a, b)
    return template("{{resultat}}", resultat=resultat)


run(host="localhost", port=8080, reloader=True)