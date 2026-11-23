#  Giganci EasyLink
> **Jeden klik trenera – ta sama strona u wszystkich uczniów w sali.**  
> Narzędzie stworzone dla trenerów i placówek **Gigantów Programowania**, eliminujące chaos z dyktowaniem i wpisywaniem linków podczas zajęć.

---

##  Dlaczego powstał EasyLink? (Problem dydaktyczny)

Prowadząc zajęcia z dziećmi (zwłaszcza młodszymi grupami) stawałem przed następujacym problemem - dzieci nie potrafią dobrze używać przeglądarki. Problem występuje z wpisywaniem linków czy otwieraniem stron. Ponad to wrzucenie linku w pliku tekstowym na dysk nie wystarczy - dzieci nie potrafia go znaleźć, ponieważ często nie pamiętają gdzie on się znajduje. Powoduje to, że często muszę podchodzić i manualnie wpisywać link do przeglądarek uczniów. Ten proces można przyspieszyć.

**EasyLink rozwiązuje to w 1 sekundę:** Trener otwiera dowolną stronę (scratch, app inventor), klika **jeden guzik w Chrome**, a strona natychmiast pojawia się na ekranach wszystkich uczniów w pracowni.

---

## Jak to działa? 

1. **Uczeń**: Na stanowiskach dzieci w tle działa cichy, niewidoczny proces (`easylink_worker.exe`). Nie wymaga od dziecka żadnej interakcji ani wiedzy technicznej.
2. **Trener**: Posiada intuicyjne rozszerzenie w przeglądarce Chrome.
3. **Magia w tle (Zero Configuration)**: System automatycznie skanuje lokalną sieć (LAN) i sam wykrywa aktywne komputery w sali – bez wpisywania adresów IP, bez chmury, w 100% lokalnie i bezpiecznie.

---

## 🛠️ Architektura techniczna

Projekt składa się z trzech minimalistycznych, lekkich modułów:

1. **Frontend (`frontend/`)**:
   - Wtyczka **Chrome Extension** 
   - prosty guzik do otwierania stron na wszystkich komputerach

2. *** Serwer Trenera (`backend/`)**:
   - serwer **FastAPI**.
   - Moduł `NetworkService` skanujący maskę podsieci
   - Pamięć podręczna znalezionych komputerów w tymczasowym rejestrze.

3. **Klient Ucznia (`server/worker.py`)**:
   - skompilowany do pojedynczego pliku `.exe` (za pomocą PyInstaller).
   - Uruchamiany automatycznie z autostartem Windows lub wdrożony raz przez administratora pracowni.

---

## Jak uruchomić (Instrukcja wdrożenia)

### 1. Na komputerze ucznia (jednorazowo):
1. Zbuduj lub pobierz `easylink_worker.exe` (z folderu `server/` za pomocą `build.bat`).
2. Wrzuć plik do autostartu Windows (`shell:startup`). Gotowe!

### 2. Na komputerze trenera:
1. Uruchom serwer backendowy:
   ```bash
   cd backend
   uv run uvicorn src.main:app --port 8000
   ```
   TODO: aplikacja .exe ustawiona w autostarcie.
2. Załaduj rozszerzenie w przeglądarce Chrome:
   - Wejdź w `chrome://extensions/`.
   - Włącz **Tryb programisty** (Developer mode).
   - Kliknij **Załaduj rozpakowane** (Load unpacked) i wskaż folder `frontend`.

---

## 👥 Autor
Krzysztof Sokołowski, Radom 2026
