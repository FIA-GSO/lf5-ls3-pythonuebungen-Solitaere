class kunde:
    def __init__(self,vorname: str,nachname: str, konten: str):
        self.vorname = vorname
        self.nachname = nachname
        self.konten = konten
        
class konto:
    def __init__(self,iban: str,saldo: float, zugangsdaten: str, vorname: str, nachname: str):
        self.iban = iban 
        self.saldo = saldo 
        self.zugangsdaten = zugangsdaten
        self.kunde = kunde(vorname, nachname)