from flask import Flask, render_template
from testdaten import produkte
app = Flask(__name__) # Erstellen der App
@app.route("/") #Hauptseite wird erstellt
def startseite():
    gefilterte_produkte = []
    for p in produkte:
        if p["auf_lager"] == 1:
            gefilterte_produkte.append(p)
    return render_template("index.html", produkte = gefilterte_produkte)
if __name__ == "__main__":
    app.run(debug=True)
