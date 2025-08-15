from datetime import datetime, date

def formatta_data(row):
    '''
    Funzione che mi restituisce una data formattata in ISO carina a partire da una riga del file csv della banca
    '''
    data_schifosa = datetime.strptime(row["Data operazione"], "%d/%m/%Y")
    data_formattata = date.fromisoformat(data_schifosa.isoformat()[:10])
    return data_formattata

def scrivi_riga(data, importo, portafogli, descrizione, file):
    file.write(str(data) + " " + descrizione + "\n")
    file.write("    " + portafogli + "    " + importo + "€"+ "\n")
    file.write("\n")