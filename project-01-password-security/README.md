# Projekt 01 – Grundlagen der Passwortsicherheit

## Ziel
Die grundlegenden Prinzipien der Passwortsicherheit verstehen und häufige Schwachstellen kennenlernen.

## Hintergrund
Passwörter sind nach wie vor eine der gängigsten Methoden zur Authentifizierung. Schwache oder mehrfach verwendete Passwörter stellen ein großes Sicherheitsrisiko dar.

## Vorgehensweise
- Schwache und starke Passwörter vergleichen
- Analysieren, warum die Länge eines Passworts wichtig ist
- Grundlegende Angriffsarten (z. B. Brute-Force) auf konzeptioneller Ebene verstehen

## Wichtige Erkenntnisse
- Kurze Passwörter sind besonders anfällig
- Die Länge ist oft wichtiger als die Komplexität
- Mehrfach verwendete Passwörter erhöhen das Gesamtrisik0

## Password Comparison
| Passwortbeispiel | Länge  | Komplextität | Geschätzte Stärke  |
|------------------|--------|--------------|--------------------|
| 12345            | 5      | Niedrig      | Sehr schwach       |
| Pa55word         | 8      | Mittel       | Mittel             |
| My$ecur3P@ss2025!| 17     | Hoch         | Stark              |

### Beobachtung
Kurze Passwörter wie „12345“ sind extrem schwach und leicht durch Brute-Force-Angriffe zu knacken.
Längere, komplexe Passwörter sind deutlich sicherer und schwerer zu erraten.
Diese Übung verdeutlicht die Bedeutung von Passwortlänge und -komplexität.

## Python Exercise

Ein einfaches Python-Skript `password_check.py` demonstriert die Stärke von Passwörtern anhand ihrer Länge.

Das Skript geht eine Liste von Beispiel-Passwörtern durch, berechnet deren Länge und bewertet die Stärke als „Sehr schwach“, „Mittel“ oder „Stark“.

So wird deutlich, dass kurze Passwörter schwächer sind als längere und komplexere.

### Beispielausgabe

Password: 12345 | Länge: 5 | Geschätzte Stärke: Sehr schwach

Password: Pa55word | Länge: 8 | Geschätzte Stärke: Mittel

Password: My$ecur3P@ss2025! | Länge: 17 | Geschätzte Stärke: Stark
