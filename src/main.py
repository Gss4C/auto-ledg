import csv
import funzioni_varie as fnx
#from datetime import date

que_banca = input("Quale banca si vuole scegliere? \n 1: Hype\n 2: Buddy \n")
csv_file = "./dati/" + input("Indica il nome (con estensione) del file che desideri: ")
#print('file selezionato: ' + csv_file)

match que_banca: #non mi va di inserire argparse, voglio na roba veloce
    case "1":
        print("Hai scelto Hype")
        portafogli = "Assets:Checking:Hype"
    case "2":
        print("Hai scelto Buddy")
        portafogli = "Assets:Checking:Buddy"


## Inizia la scrittura del file ##

with open("./Output_file_autoledger.txt", "w") as f:
    reader_csv_dict = csv.DictReader(open(csv_file))
    for row in reader_csv_dict:
        data    = fnx.formatta_data(row)
        importo = row["Importo ( € )"].replace(".", ",")

        fnx.scrivi_riga(data, importo, portafogli, row['Descrizione'], f) 