# pwmint – Pseudoword Generator Implementation Plan

## Ziel

Die bisher verwendete statische Datei `src/pwmint/wordlist.txt` soll vollständig entfernt werden.

Statt einer persistenten Wortliste soll `pwmint` Pseudowörter bei Bedarf dynamisch im Arbeitsspeicher erzeugen.

Der neue Pseudowort-Generator soll:

- ausschließlich die Python-Standardbibliothek verwenden
- `secrets` als kryptografisch geeignete Zufallsquelle verwenden
- Pseudowörter mit 6–12 Zeichen erzeugen
- ausschließlich Kleinbuchstaben `a-z` verwenden
- durch eine einfache C/V-Regel relativ lesbare Pseudowörter erzeugen
- keine Wörter dauerhaft speichern
- keine externe Wordlist benötigen
- einfachen und gut verständlichen Python-Code verwenden
- leicht durch Unit Tests überprüfbar sein

Der Generator ist ausschließlich für die Passphrase-Erzeugung vorgesehen.

Der bestehende Passwortgenerator `password.py` darf nicht verändert werden.

---

# 1. Aktuelle Architektur

Die aktuelle Struktur ist:

```text
pwmint/
├── .github/
│   ├── instructions/
│   │   ├── copilot-instructions.md
│   │   ├── project-structure.md
│   │   └── requirements.md
│   └── planning/
│       └── plan-pwmint-implementation.prompt.md
├── build/
├── cli/
│   └── pwmint.py
├── gui/
├── security-review/
├── src/
│   └── pwmint/
│       ├── passphrase.py
│       ├── password.py
│       └── wordlist.txt
├── tests/
│   ├── test_passphrase.py
│   └── test_password.py
├── .envrc
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

Nach der Implementierung soll die Struktur unter `src/pwmint/` ungefähr so aussehen:

```text
src/
└── pwmint/
    ├── passphrase.py
    ├── password.py
    └── pseudoword.py
```

`wordlist.txt` soll nicht mehr benötigt werden und anschließend gelöscht werden.

---

# 2. Neue Datei `pseudoword.py`

Erstelle:

```text
src/pwmint/pseudoword.py
```

Diese Datei enthält ausschließlich die Logik zur Erzeugung einzelner Pseudowörter.

Die Funktion soll eine klare, kleine Verantwortung haben:

> Erzeuge ein zufälliges Pseudowort mit einer Länge zwischen 6 und 12 Zeichen.

Bevorzugt soll eine einfache Funktion verwendet werden:

```python
generate_pseudoword()
```

Eine Klasse ist nicht erforderlich.

Keine unnötigen Abstraktionen oder Design Patterns einführen.

---

# 3. Wortlänge

Definiere Konstanten für die erlaubte Wortlänge:

```python
MIN_WORD_LENGTH = 6
MAX_WORD_LENGTH = 12
```

Die Länge jedes Pseudowortes soll unabhängig und zufällig zwischen 6 und 12 Zeichen gewählt werden.

Wichtig:

Es darf keine getrennte Wortliste oder ein separater Pool für unterschiedliche Wortlängen existieren.

Nicht:

```text
6 Zeichen → eigener Pool
7 Zeichen → eigener Pool
8 Zeichen → eigener Pool
...
```

Stattdessen wird für jedes einzelne Wort die Länge neu bestimmt.

Beispiel:

```text
7 - 12 - 10 - 8 - 8 - 6
```

ist eine gültige Folge von Wortlängen innerhalb einer sechs Wörter langen Passphrase.

---

# 4. Alphabet

Verwende ausschließlich Kleinbuchstaben.

```python
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
```

Damit stehen zur Verfügung:

- 5 Vokale
- 21 Konsonanten

Das `y` wird als Konsonant behandelt.

Keine Zahlen.

Keine Sonderzeichen.

Keine Großbuchstaben.

Keine Umlaute.

Keine Unicode-Zeichen.

---

# 5. C/V-Regel

Die Pseudowörter sollen durch eine einfache Konsonant-/Vokal-Struktur lesbarer werden.

Dabei gilt:

```text
C = Konsonant
V = Vokal
```

Das Pseudowort verwendet abwechselnd:

```text
C V C V C V ...
```

oder:

```text
V C V C V C ...
```

Die Startposition soll zufällig gewählt werden.

Dadurch können beispielsweise Pseudowörter entstehen wie:

```text
velanor
kamiro
tavelo
orimaku
sudekano
```

Die erzeugten Wörter müssen keine echten Wörter sein und müssen nicht perfekt aussprechbar sein.

Die Lesbarkeit ist ein Komfortmerkmal.

Die kryptografisch geeignete Zufallsauswahl hat Vorrang.

---

# 6. Zufallsquelle

Verwende ausschließlich:

```python
import secrets
```

Für die zufällige Auswahl von:

- Wortlänge
- Startposition
- Konsonanten
- Vokalen

soll `secrets` verwendet werden.

Bevorzugt sollen einfache Funktionen wie:

```python
secrets.choice()
```

und bei Bedarf:

```python
secrets.randbelow()
```

verwendet werden.

Nicht verwenden:

```python
random
```

Keine eigene Zufallslogik implementieren.

Keine Hash-Funktionen als Ersatz für einen Zufallszahlengenerator verwenden.

Keine externen Zufallsquellen verwenden.

---

# 7. Entropie und Zufallsraum

Der Pseudowort-Generator soll keinen eigenen kryptografischen Zufallsalgorithmus implementieren.

Der Zufallsraum wird durch die erlaubten Kombinationen aus:

- Wortlänge
- Startposition
- Vokalen
- Konsonanten
- mehreren unabhängigen Pseudowörtern

definiert.

Die tatsächliche Sicherheit soll aus der Verwendung von `secrets` und der Kombination mehrerer unabhängig erzeugter Pseudowörter entstehen.

Wichtig:

Die Implementierung darf keine unbegründeten Entropiewerte als Sicherheitsversprechen ausgeben.

Insbesondere soll nicht behauptet werden, dass ein einzelnes Pseudowort eine bestimmte Anzahl Bits Entropie besitzt, ohne den tatsächlichen Zufallsraum exakt zu berechnen.

Die C/V-Regel dient hauptsächlich der besseren Lesbarkeit.

---

# 8. Keine persistente Speicherung

Der Pseudowort-Generator darf keine Dateien erzeugen.

Insbesondere darf keine Datei unter:

```text
~/.cache/pwmint/
```

angelegt werden.

Es soll keine Cache-Datei geben.

Es soll keine temporäre Wordlist geben.

Es soll keine Datenbank geben.

Die Pseudowörter werden nur während der aktuellen Programmausführung im Arbeitsspeicher erzeugt.

Nach Beendigung der Verarbeitung sollen sie nicht persistent gespeichert werden.

---

# 9. Integration in `passphrase.py`

Die bestehende Passphrase-Funktion soll weiterhin folgende Anforderungen erfüllen:

- Standardmäßig 4 Wörter
- mindestens 4 Wörter
- maximal 10 Wörter
- maximal 128 Zeichen für die gesamte Passphrase
- Standardseparator `-`
- frei wählbarer Separator
- keine Wiederholung eines Wortes innerhalb einer einzelnen Passphrase
- `secrets` als Zufallsquelle
- keine Speicherung vergangener Passphrasen

Die bisherige Funktion `_load_word_list()` soll entfernt werden.

Stattdessen soll `passphrase.py` den neuen Generator aus `pseudoword.py` verwenden.

Die Abhängigkeit soll ungefähr so aussehen:

```text
passphrase.py
      │
      ▼
pseudoword.py
      │
      ▼
    secrets
```

`passphrase.py` soll weiterhin für die Erstellung der kompletten Passphrase verantwortlich sein.

`pseudoword.py` soll nur einzelne Pseudowörter erzeugen.

Keine Passphrase-Logik in `pseudoword.py` verschieben.

---

# 10. Keine Wiederholung innerhalb einer Passphrase

Die bisherige Anforderung bleibt bestehen:

Innerhalb einer einzelnen Passphrase darf dasselbe Pseudowort nicht zweimal vorkommen.

Beispiel gültig:

```text
velanor-kamiro-dorena-suranomi-melvikon-tavelo
```

Beispiel ungültig:

```text
velanor-kamiro-velanor-suranomi-melvikon-tavelo
```

Zwischen unterschiedlichen Passphrasen ist eine Wiederholung dagegen erlaubt.

Beispiel:

```text
Passphrase 1:
velanor-kamiro-dorena-suranomi

Passphrase 2:
tavelo-dorena-melvikon-umekari
```

Das Wort `dorena` darf in beiden Passphrasen vorkommen.

---

# 11. Verhalten bei `--count`

Bei:

```bash
python -m cli.pwmint --passphrase --words 6 --count 10
```

sollen zehn Passphrasen erzeugt werden.

Jede Passphrase besteht aus sechs unabhängig erzeugten Pseudowörtern.

Die Pseudowörter werden nur für die aktuelle Verarbeitung erzeugt.

Es gibt keinen gemeinsamen persistenten Wortpool.

Die gleiche Pseudowort-Zeichenfolge darf zufällig in verschiedenen Passphrasen wieder auftreten.

---

# 12. Tests

Erstelle:

```text
tests/test_pseudoword.py
```

Die Tests sollen mindestens prüfen:

### Länge

Jedes erzeugte Wort muss zwischen 6 und 12 Zeichen lang sein.

### Alphabet

Jedes erzeugte Wort darf ausschließlich aus:

```text
a-z
```

bestehen.

### Vokale

Jedes erzeugte Wort muss mindestens einen Vokal enthalten.

### Konsonanten

Jedes erzeugte Wort muss mindestens einen Konsonanten enthalten.

### C/V-Struktur

Die erzeugten Wörter müssen der definierten alternierenden C/V-Struktur entsprechen.

Dabei müssen sowohl Wörter mit:

```text
C V C V ...
```

als auch:

```text
V C V C ...
```

grundsätzlich möglich sein.

Da die Startposition zufällig ist, soll der Test nicht davon ausgehen, dass jedes Wort mit einem Konsonanten beginnt.

### Mehrere Wörter

Mehrere Pseudowörter erzeugen und prüfen, dass sie gültige Ergebnisse liefern.

### Unterschiedliche Wortlängen

Der Test darf nicht davon ausgehen, dass alle Wörter dieselbe Länge besitzen.

Die Implementierung soll die Länge für jedes Wort unabhängig bestimmen.

Da Zufallstests grundsätzlich probabilistisch sind, soll ein Test nicht unnötig fehlschlagen, nur weil in einer kleinen Stichprobe zufällig nicht jede mögliche Länge vorkommt.

---

# 13. Bestehende Tests

Die vorhandenen Tests dürfen nicht unnötig verändert werden.

Insbesondere:

```text
tests/test_password.py
```

darf nicht verändert werden, sofern dies für die neue Funktion nicht zwingend notwendig ist.

Die bestehenden Passphrase-Tests sollen an die neue Implementierung angepasst werden, falls sie bisher direkt oder indirekt von der statischen `wordlist.txt` abhängig sind.

Alle bisherigen funktionalen Anforderungen der Passphrase sollen erhalten bleiben.

---

# 14. CLI

Die CLI soll in diesem Schritt grundsätzlich unverändert bleiben.

Nicht ändern:

```text
cli/pwmint.py
```

außer eine Änderung ist zwingend notwendig, damit die neue Pseudowort-Implementierung funktioniert.

Die bestehende CLI-Validierung soll erhalten bleiben:

```text
--length      nur für Passwörter
--words       nur mit --passphrase
--separator   nur mit --passphrase
--count       für Passwort und Passphrase
```

Keine neue CLI-Funktionalität hinzufügen.

---

# 15. Passwortgenerator

Die Datei:

```text
src/pwmint/password.py
```

darf nicht verändert werden.

Der Passwortgenerator ist von dieser Änderung nicht betroffen.

---

# 16. Dateien, die geändert oder erstellt werden dürfen

Für diese Aufgabe dürfen ausschließlich folgende Dateien erstellt oder geändert werden:

```text
src/pwmint/pseudoword.py
src/pwmint/passphrase.py
tests/test_pseudoword.py
tests/test_passphrase.py
```

Zusätzlich soll anschließend diese Datei gelöscht werden:

```text
src/pwmint/wordlist.txt
```

Keine weiteren Dateien anlegen.

Insbesondere nicht:

- keine neuen Konfigurationsdateien
- keine zusätzlichen Python-Pakete
- keine neuen Abstraktionsschichten
- keine neuen Klassen
- keine Datenbank
- keine Cache-Dateien
- keine Dateien unter `~/.cache/pwmint/`

---

# 17. Code-Stil

Der Code soll dem bestehenden Projektstil entsprechen.

Bevorzugt:

- einfache Funktionen
- verständliche Variablennamen
- einfache `for`-Schleifen
- einfache `if`-Anweisungen
- einfache Typ-Hinweise, wo sinnvoll
- kurze Docstrings
- Kommentare nur dort, wo sie das "Warum" erklären

Vermeiden:

- unnötige Klassen
- Design Patterns
- komplizierte Comprehensions
- Generator Expressions
- unnötige Decorators
- Metaclasses
- unnötige Abstraktionen
- unnötige externe Libraries
- übermäßig cleveren Code
- schwer verständliche Einzeiler

Der Code soll auch für einen fortgeschrittenen Python-Anfänger gut nachvollziehbar sein.

---

# 18. Dokumentation im Code

`pseudoword.py` soll einen kurzen Modul-Docstring besitzen.

Die öffentliche Funktion `generate_pseudoword()` soll einen kurzen Docstring besitzen, der erklärt:

- was erzeugt wird
- welche Länge möglich ist
- dass `secrets` für die Zufallsauswahl verwendet wird

Nicht die komplette technische Spezifikation in den Docstring kopieren.

---

# 19. Sicherheitsanforderungen

Keine geheimen Werte loggen.

Keine Pseudowörter oder Passphrasen in Dateien schreiben.

Keine Debug-Ausgaben in den Generator einbauen.

Kein `random` verwenden.

Keine eigenen kryptografischen Algorithmen implementieren.

Keine externe Netzwerkverbindung verwenden.

Der Generator muss vollständig offline funktionieren.

---

# 20. Abschlussprüfung

Nach der Implementierung müssen mindestens folgende Befehle erfolgreich sein:

```bash
pytest
```

und:

```bash
python -m cli.pwmint
```

sowie:

```bash
python -m cli.pwmint --passphrase
```

und:

```bash
python -m cli.pwmint --passphrase --words 6 --count 5
```

Dabei sollen gültige Pseudopassphrasen erzeugt werden.

Zusätzlich prüfen:

```bash
python -m cli.pwmint --passphrase --words 10
```

und:

```bash
python -m cli.pwmint --passphrase --words 11
```

Der zweite Aufruf muss weiterhin sauber mit einem Fehler abgelehnt werden.

---

# 21. Erwartetes Ergebnis

Nach Abschluss soll `pwmint` keine statische Wordlist mehr benötigen.

Beispiel:

```bash
python -m cli.pwmint --passphrase --words 6 --count 3
```

könnte beispielsweise erzeugen:

```text
velanor-kamirobenito-tavelipo-suranomi-melvikon-dorena
umekari-tavelo-sudekano-orimaku-velanor-pimeta
kamiro-suvane-doremi-taveloku-neravi-umeko
```

Die konkreten Wörter und deren Reihenfolge müssen bei jedem Aufruf zufällig sein.

Die Wörter müssen keine echten Wörter sein.

Die Wortlängen dürfen sich innerhalb einer Passphrase unterscheiden.

Es darf keine persistente Wordlist mehr vorhanden sein.

---

# 22. Wichtige Einschränkung

Nicht über den beschriebenen Umfang hinausgehen.

Diese Aufgabe betrifft ausschließlich:

```text
Pseudowort-Generator
        +
Passphrase-Integration
        +
Tests
        +
Entfernen der Wordlist
```

Nicht in dieser Aufgabe enthalten:

- GUI
- PyInstaller
- Packaging
- neue CLI-Funktionen
- Passwortgenerator
- Security-Review-Dokumentation
- README-Überarbeitung
- Datenbank
- Cache
- Konfigurationsdateien

Nach Abschluss bitte zuerst die geänderten Dateien und eine kurze Zusammenfassung der Änderungen anzeigen.

Danach:

```bash
pytest
```

ausführen und das Testergebnis melden.
