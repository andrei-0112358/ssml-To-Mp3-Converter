# SSML zu MP3 Konverter (Python / Google Cloud TTS)

## Beschreibung
Dieses Projekt implementiert ein einfaches Python-Skript, das SSML-Text in eine MP3-Datei umwandelt. Es verwendet die **Google Cloud Text-to-Speech API**, um synthetisierte Sprache aus formatiertem SSML zu erzeugen.

## Funktionsweise
1. Das Skript importiert die Google Cloud TTS-Bibliothek.
2. Eine Funktion `ssml_to_mp3(ssml_text, output_file)` nimmt SSML-Text als Eingabe und erzeugt eine MP3-Datei.
3. **Text-to-Speech Client**:
   * Sprache wird über `VoiceSelectionParams` festgelegt.
   * Audioformat ist MP3 (`AudioEncoding.MP3`).
4. SSML-Text kann mehrere Stimmen und `<break>` Pausen enthalten.
5. Das Ergebnis wird als MP3-Datei im angegebenen Pfad gespeichert.

## Ablauf / Beispiel
1. SSML-Text im Skript einfügen (Beispiel im Skript enthalten: verschiedene Formen von „Ich habe gesetzt / I put“ in Russisch und Englisch).
2. Funktionsaufruf:

   ```python
   ssml_to_mp3(ssml, "put.mp3")
   ```
3. Nach Ausführung erscheint die MP3-Datei `put.mp3` im Projektverzeichnis.


## Anpassungen
* SSML-Text kann beliebig geändert oder erweitert werden.
* Stimmen können angepasst werden (`ru-RU-Wavenet-A`, `en-US-Wavenet-D` etc.).
* Pausen `<break time="3s"/>` können beliebig gesetzt werden, um Sprachlern- oder Audio-Übungen zu strukturieren.

## Ausführen
1. Service Account Key als Umgebungsvariable setzen:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-key.json"
   ```
2. Skript starten:

   ```bash
   python ssml_to_mp3.py
   ```
3. MP3-Datei wird im aktuellen Verzeichnis erstellt.


## Voraussetzungen
* **Python 3.7+**
* **Google Cloud SDK** und authentifizierter Service Account mit Zugriff auf Text-to-Speech API
* Installation der Bibliothek:

  ```bash
  pip install google-cloud-texttospeech
  ```

