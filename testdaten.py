produkte = [{"name":"Austersauce", "preis": 3.50, "auf_lager": 1}, {"name":"Fischsauce", "preis": 4.00, "auf_lager": 1}, {"name":"Buldak Ramyeon", "preis": 2.50, "auf_lager": 0}, {"name":"Glasnudeln", "preis": 1.99, "auf_lager": 0}, {"name":"Mama", "preis": 0.50, "auf_lager": 1}]

def testdaten():
    for p in produkte:
        if p["auf_lager"] == 1:
            print(p["name"], p["preis"])




