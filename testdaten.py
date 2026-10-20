produkte = [{"name":"Austersauce", "preis": 3.50, "auf_lager": 1, "id": 1001}, {"name":"Fischsauce", "preis": 4.00, "auf_lager": 1, "id": 1002}, {"name":"Buldak Ramyeon", "preis": 2.50, "auf_lager": 0, "id": 1003}, {"name":"Glasnudeln", "preis": 1.99, "auf_lager": 0, "id":1004}, {"name":"Mama", "preis": 0.50, "auf_lager": 1, "id": 1005}]

def testdaten():
    for p in produkte:
        if p["auf_lager"] == 1:
            print(p["name"], p["preis"])




