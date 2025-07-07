# 🎤 Dictafon Vocal cu Integrare Xdotool

---

Un dictafon personalizat pentru sistemele Debian bazat pe Whisper, conceput pentru a transforma vorbirea în text în timp real (sau aproape real-time) și a o introduce direct în orice aplicație, folosind `xdotool`.

## ✨ Caracteristici

*   **Recunoaștere Vocală Offline:** Utilizează motoare ASR (Automatic Speech Recognition) care funcționează complet offline, asigurând confidențialitatea și viteza.
*   **Integrare cu Xdotool:** Textul recunoscut este tastat automat la poziția curentă a cursorului, în orice fereastră activă.
*   **Comutare Înregistrare (Push-to-Talk):** Înregistrarea audio este controlată prin apăsarea tastei `F12` (toggle). O apăsare începe înregistrarea, iar o a doua apăsare o oprește și declanșează transcrierea.
*   **Selectare Model Whisper:** Permite utilizatorului să specifice modelul Whisper (`tiny`, `base`, `small`, `medium`, `large`) la pornirea scriptului, oferind flexibilitate între acuratețe și performanță.
*   **Compatibilitate Debian:** Optimizat pentru a rula pe sistemul de operare Debian 12 "Bookworm".

## 🚀 Cum Funcționează

1.  **Captură Audio:** Sistemul captează fluxul audio de la microfon la apăsarea tastei `F12` și continuă să înregistreze până la o nouă apăsare a aceleiași taste.
2.  **Procesare ASR:** Datele audio înregistrate sunt trimise către motorul de recunoaștere vocală Whisper.
3.  **Conversie Text:** Motorul Whisper transformă vorbirea în text, cu o acuratețe îmbunătățită prin specificarea explicită a limbii române.
4.  **Introducere Text:** Textul rezultat este apoi simulat ca intrare de tastatură folosind `xdotool`, scriind în aplicația activă.

## 🛠️ Instalare și Configurare

### Pre-rechizite
Deja am instalat dependintele: python3 python3-pip venv xdotool ffmpeg portaudio19-dev.

### Pasul 1: Crearea unui repo in github

### Pasul 2: Instalarea dependințelor Python

Instalați pachetele necesare în mediul virtual:

```bash
source venv/bin/activate
pip install openai-whisper sounddevice pynput scipy
```

### Pasul 3: Rularea aplicației

Pentru a rula aplicația, navigați în directorul proiectului și activați mediul virtual, apoi executați scriptul `dictafon.py` specificând modelul Whisper dorit (ex: `small`, `base`, `medium`).

```bash
source venv/bin/activate
python3 dictafon.py [model_name]
```

Dacă nu specificați un `model_name`, scriptul va afișa o listă cu modelele disponibile.

**Exemple:**

*   `python3 dictafon.py small`
*   `python3 dictafon.py base`
*   `python3 dictafon.py medium`

După pornirea scriptului, apăsați `F12` pentru a începe înregistrarea și `F12` din nou pentru a o opri și a transcrie. Textul transcris va fi tastat automat în aplicația activă.

### Pasul 4: Integrarea in OS cu ajutorul xdotool
In faza acuala dictarea apare in terminal, doresc ca aceasta sa fie "scris" unde am cursorul, de exmplu in chatbox-ul din programul 'gemini cli'