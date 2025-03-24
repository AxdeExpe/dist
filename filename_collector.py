import os

def liste_dateinamen(verzeichnis, ausgabedatei):
    """
    Listet alle Dateinamen in einem Verzeichnis auf und schreibt sie in eine Textdatei.

    Args:
        verzeichnis (str): Der Pfad zum Verzeichnis.
        ausgabedatei (str): Der Pfad zur Ausgabedatei.
    """

    try:
        with open(ausgabedatei, 'w') as f:
            for dateiname in os.listdir(verzeichnis):
                pfad = os.path.join(verzeichnis, dateiname)
                if os.path.isfile(pfad):  # Nur Dateien, keine Verzeichnisse
                    f.write(dateiname + '\n')
        print(f"Dateinamen wurden in '{ausgabedatei}' gespeichert.")

    except FileNotFoundError:
        print(f"Fehler: Verzeichnis '{verzeichnis}' nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Beispielaufruf
verzeichnis = "./flags"  # Ersetze dies durch den tatsächlichen Pfad
ausgabedatei = "dateinamen.txt"
liste_dateinamen(verzeichnis, ausgabedatei)