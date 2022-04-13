from bottle import route, run, template
from addition import resultatsomme
import sys


@route("/add/<a>/<b>")
def addition(a="0", b="0"):
    resultat = resultatsomme(a, b)
    return template("{{resultat}}", resultat=resultat)


run(host="0.0.0.0", port=sys.argv[1], reloader=True)
