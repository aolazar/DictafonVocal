# 🎤 Dictafon Vocal cu Integrare Xdotool

---

Un dictafon personalizat pentru sistemele Debian bazat pe Whisper, conceput pentru a transforma vorbirea în text în timp real (sau aproape real-time) și a o introduce direct în orice aplicație, folosind `xdotool`.

## ✨ Caracteristici

* **Recunoaștere Vocală Offline:** Utilizează motoare ASR (Automatic Speech Recognition) care funcționează complet offline, asigurând confidențialitatea și viteza.
* **Integrare cu Xdotool:** Textul recunoscut este tastat automat la poziția curentă a cursorului, în orice fereastră activă.
* **Compatibilitate Debian:** Optimizat pentru a rula pe sistemul de operare Debian 12 "Bookworm".

## 🚀 Cum Funcționează

1.  **Captură Audio:** Sistemul captează fluxul audio de la microfon la apasare unei combinatii de taste si termina de capturat cand eliberez tastele.
2.  **Procesare ASR:** Datele audio sunt trimise către motorul de recunoaștere vocală ales (Whisper).
3.  **Conversie Text:** Motorul ASR transformă vorbirea în text.
4.  **Introducere Text:** Textul rezultat este apoi simulat ca intrare de tastatură folosind `xdotool`, scriind în aplicația activă.

## 🛠️ Instalare și Configurare

### Pre-rechizite
Deja am instalat dependintele: python3 python3-pip venv xdotool ffmpeg portaudio19-dev.


### Pasul 1: Crearea unui repo in github
