# check123

Test pentru telefoane second-hand, rulat direct în browser pe telefonul care se vinde (nume de lucru: **Bifat**).

Vânzătorul deschide pagina pe telefon, trece prin testele ghidate și primește un raport cu cod unic, pe care îl trimite cumpărătorului (text copiat sau PDF).

## Ce testează

| Test | Android | iPhone |
|---|---|---|
| Ecran (culori pe tot ecranul) | da | da (fără fullscreen în Safari) |
| Atingere (grilă) | da | da |
| Camere față și spate | da | da |
| Difuzor și microfon (detectare automată a tonurilor) | da | da |
| Senzori de mișcare | da | da, cu permisiune |
| Vibrație | da | nu se poate din browser |
| Deblocare biometrică | declarată de vânzător | declarată de vânzător |
| Baterie | nivel | doar din captură |
| IMEI, sănătatea bateriei, blocare cont, model | din capturi de ecran | din capturi de ecran |

La final: raport cu cod unic, rezumat de copiat în chatul OLX și export PDF (raport + capturi).

## Cum îl rulezi

Camera, microfonul și senzorii merg doar pe **HTTPS** (sau `localhost`).

- **GitHub Pages:** Settings → Pages → Deploy from branch → `main` / root. Pagina va fi la `https://<user>.github.io/check123/`.
- **Local:** `npx serve .` și deschide adresa de pe telefon (aceeași rețea) sau folosește un tunel HTTPS (de ex. `npx localtunnel --port 3000`).

## Structură

- `index.html` – toată aplicația (HTML, CSS, JS într-un singur fișier). Folosește jsPDF și html2canvas de pe cdnjs pentru PDF.

## Limitări cunoscute

- Modelul exact nu e transmis de browser (Safari nu îl dă deloc, Chrome îl ascunde parțial). Sursa sigură e captura „Despre telefon”.
- Sănătatea bateriei și IMEI-ul nu pot fi citite din browser, de aceea se cer capturi de ecran.
- În afara claude.ai nu există citire automată a capturilor; câmpurile se completează manual.
- Raportul rămâne pe telefonul pe care s-a făcut testul (nu există încă server).

## Următorii pași

- Backend pentru rapoarte cu link partajabil (`/r/<cod>`), deschis direct de cumpărător.
- OCR pe server pentru IMEI, model și baterie din capturi.
- Identificarea modelului din IMEI (TAC) și verificare în baze de telefoane furate.
- Verificare la predare: cumpărătorul compară codul și IMEI-ul pe loc.
