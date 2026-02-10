# Projekt 02 - Passwort-Hashing-Demo

## Ziel
Veranschaulichen, wie Passwörter gehasht werden, um sie nicht im Klartext zu speichern.
Dies verbessert die Sicherheit und schützt die Benutzerdaten.

## Hintergrund
Wenn Passwörter als Hashes gespeichert werden, sind sie selbst im Falle einer Kompromittierung der Datenbank nicht direkt einsehbar.
Hashing ist eine Einwegfunktion, die beliebige Eingaben in einen festen Zeichenstring umwandelt.

## Vorgehensweise 
- Der Benutzer gibt ein Passwort ein
- Mit dem Python-Modul 'hashlib' wird ein SHA-256-Hash erzeugt
- Das gehashte Passwort wird angezeigt

### Beispielausgabe
Gib ein Passwort ein, das gehasht werden soll: mypassword123
Gehashtes Passwort: 6e659deaa85842cdabb5c6305fcc40033ba43772ec00d45c2a3c921741a5e377

### Wichtige Erkenntnisse
- Hashing ist eine Einwegfunktion
- SHA-256 liefert für Passwörter einen sicheren Hash
- Passwörter sollen nie direkt gespeichert werden, sondern nur als Hash.
