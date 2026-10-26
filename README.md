# check123

Test pentru telefoane second-hand, rulat direct în browser pe telefonul care se vinde (nume de lucru: **Bifat**).

Vânzătorul deschide pagina pe telefon, trece prin testele ghidate și primește un raport cu cod unic, pe care îl trimite cumpărătorului (text copiat sau PDF).

## Ce testează

| Test | Android | iPhone |
|---|---|---|
| Ecran (culori pe tot ecranul) | da | da (în Safari rămân butoanele de jos; instalat pe ecranul principal e complet) |
| Atingere (grilă) | da | da |
| Camere față și spate (automat: pornește, imagine neagră, înghețată, focus) | da | da |
| Difuzor și microfon (detectare automată a tonurilor) | da | da |
| Senzori de mișcare | da | da, cu permisiune |
| Vibrație | da | nu se poate din browser |
| Deblocare biometrică | declarată de vânzător | declarată de vânzător |
| Baterie | nivel | doar din captură |
| IMEI, sănătatea bateriei, blocare cont, model | citite automat din capturi (OCR pe telefon) | citite automat din capturi (OCR pe telefon) |
| Model după IMEI (TAC) | da | da |

La final: raport cu cod unic, rezumat de copiat în chatul OLX și export PDF (raport + capturi).

## Cum îl rulezi

Camera, microfonul și senzorii merg doar pe **HTTPS** (sau `localhost`).

- **GitHub Pages:** Settings → Pages → Deploy from branch → `main` / root. Pagina va fi la `https://<user>.github.io/check123/`.
- **Local:** `npx serve .` și deschide adresa de pe telefon (aceeași rețea) sau folosește un tunel HTTPS (de ex. `npx localtunnel --port 3000`).

## Structură

- `index.html` – toată aplicația (HTML, CSS, JS într-un singur fișier).
  Folosește jsPDF și html2canvas de pe cdnjs pentru PDF și Tesseract.js de pe jsDelivr pentru citirea capturilor.
- `tac/` – codurile TAC (primele 8 cifre din IMEI) împărțite după primele 3 cifre, încărcate doar când e nevoie.
- `scripts/build_tac.py` – regenerează `tac/` din `tac_full.csv` al [MoazEb/tac-database](https://github.com/MoazEb/tac-database) (MIT):
  `python3 scripts/build_tac.py tac_full.csv tac`
- `manifest.webmanifest`, `icons/` – instalare pe ecranul principal, unde testul de ecran rulează fără barele browserului.

## Limitări cunoscute

- Modelul exact nu e transmis de browser (Safari nu îl dă deloc, Chrome îl ascunde parțial). Sursa sigură e captura „Despre telefon”.
- Sănătatea bateriei și IMEI-ul nu pot fi citite din browser, de aceea se cer capturi de ecran.
- Citirea capturilor rulează pe telefon, cu Tesseract.js; prima dată descarcă aproximativ 5 MB de date de limbă (română și engleză).
  Valorile citite pot avea greșeli, așa că rămân editabile.
- Baza TAC nu are proveniență documentată, deci modelul după IMEI e orientativ.
- Raportul rămâne pe telefonul pe care s-a făcut testul (nu există încă server).

## Următorii pași

- Backend pentru rapoarte cu link partajabil (`/r/<cod>`), deschis direct de cumpărător.
- Verificarea IMEI-ului în baze de telefoane furate.
- Verificare la predare: cumpărătorul compară codul și IMEI-ul pe loc.
