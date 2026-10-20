from flask import Flask, render_template
from testdaten import produkte

app = Flask(__name__) # Erstellen der App
app.jinja_env.globals.update(len=len)
def umsatz():
    umsatz_wert = 0
    for p in produkte:
        if p["auf_lager"] == 0:
            umsatz_wert += p["preis"]
    return umsatz_wert

@app.route("/") #Hauptseite wird erstellt
def startseite():
    alle_produkte = produkte
    auflager_produkte = []
    ausverkauft_produkte = []
    for p in produkte:
        if p["auf_lager"] == 1:
            auflager_produkte.append(p)
        else:
            ausverkauft_produkte.append(p)

    gesamtumsatz = umsatz()
    return render_template("index.html", produkte=auflager_produkte, alle_produkte = produkte, ausverkauft_produkte = ausverkauft_produkte, gesamtumsatz = gesamtumsatz)

if __name__ == "__main__":
    app.run(debug=True)