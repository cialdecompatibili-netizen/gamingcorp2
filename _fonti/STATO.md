# STATO PROGETTO gamingcorp2 - appunti per domani (31/10/2026)

Smoke test PRIVATO: catalogo di giochi open source con nomi di fantasia. Repo clonata da `mistraltemplate1`.
- Repo: https://github.com/cialdecompatibili-netizen/gamingcorp2
- Sito: https://cialdecompatibili-netizen.github.io/gamingcorp2/ (shop: /negozio/, EN: /en/shop/)
- Cartella locale: C:\Users\mirco\Desktop\repository\gamingcorp2

## Fatto oggi
1. Creata la repo con `nuovo_sito.ps1 -Nome gamingcorp2 -Shop` (clone di mistraltemplate1, IT+EN, accento #6d28d9).
2. Salvate le due fonti in `_fonti/file.md` (commit d442a90):
   - bobeff/open-source-games (CC0, 17.3k stelle)
   - leereilly/games (ARCHIVIATA dal 14/09/2025, CC BY-NC-SA 4.0: vale per la lista, non per i giochi)
3. Create 17 categorie IT+EN (commit 6898a11), tolti categoria e prodotto di esempio. Script: `automation/crea_categorie_giochi.py`.
   Azione & Arcade, Sparatutto FPS & TPS, Platform, Avventura & Punta e Clicca, GDR & Roguelike, Mondi Online MMO,
   Strategia in Tempo Reale, Strategia a Turni, Gestionali & Citta, Corse, Puzzle & Giochi da Tavolo,
   Sandbox & Costruzione, Sport, Tower Defense, Classici Rinati, Giochi nel Browser, Giochi Mobile.
4. Aggiunti 41 giochi con nome di fantasia, screenshot e pagine IT+EN (commit a5fe84a). Prezzo 0, tipo digitale.
   Nella descrizione completa c'e il progetto originale con link GitHub. Esempio: SuperTuxKart = "Gran Premio dei Pinguini".
   Distribuzione: ogni categoria ne ha 1-3 (Tower Defense 1, Mobile 2).

## Screenshot
- 23 veri, presi dai README dei progetti. 18 generati con `gemini_auto\img.py` (hanno ombra e inquadratura "da prodotto").
- Lichess (era un diagramma) e Citybound (era nero) sono stati rigenerati.
- Loghi o banner al posto dello screenshot: Hypersomnia, Hextris, Rigs of Rods, Chase Whisply.
- File di lavoro in `C:\Users\mirco\Desktop\claudetemp\giochi\`:
  - `giochi2.py` = elenco dei 41 giochi (categoria, repo, nome originale, nome IT/EN, descrizioni) e download screenshot
  - `genera_mancanti.py` = genera gli screenshot mancanti
  - `costruisci_prodotti.py` = scrive catalogo.json e le pagine IT+EN
  - `giochi2.json` = dati finali, `screens2\` = immagini, `contact.jpg` = anteprima di tutte
- Per rifare tutto: `python costruisci_prodotti.py`, poi `python automation\allinea_hash.py en`, poi commit e push.

## Esclusi di proposito
Decompilazioni o sorgenti trapelati di giochi commerciali: Zelda Twilight Princess, Portal (portal64), Duke Nukem II, Diablo 2, Knight Online.
Scelti progetti aperti. Esclusi anche Frameworks/Engines, Chat bots e Maps/Hacks/Plugins di leereilly (non sono giochi).

## DA FARE (non fatto)
- [ ] Cercare altre repo gaming con molte stelle (`gh search repos --topic=game --sort=stars`) e aggiungerle con nomi diversi.
- [ ] Riempire le categorie povere (Tower Defense 1, Mobile 2).
- [ ] Foto per le 17 categorie (ora senza immagine).
- [ ] Guardare la resa grafica: nessuna pagina e stata vista a schermo, solo verificate online (HTTP 200).
- [ ] Sostituire gli screenshot generati con screenshot veri, dove possibile.
- [ ] Segnaposto del template: pulsante WhatsApp vuoto, email vuota in `_config.yml`, testi segnaposto in home, servizi, chi siamo (IT e EN). Se traduci a mano: `python automation\allinea_hash.py en`.
- [ ] Il connettore GitHub non compare in chat: si lavora con `gh` da Desktop Commander.

## Modifiche a mistraltemplate1 (il template, i cloni NON si aggiornano da soli)
- 60331fb Velocita: hero 331 KB -> 113 KB con preload (solo / e /en/), font in una richiesta non bloccante, CSS secondari async, logo-72.png (aggiunto a genera_logo.py), Alpine defer, skip link con id="main", contrasto footer.
  Punteggio mobile era 79 (desktop 98). I nuovi punteggi NON li so: PageSpeed ha risposto "troppe richieste". Da rilanciare su https://cialdecompatibili-netizen.github.io/mistraltemplate1/en/
- f36cd45 Footer: era bianco su bianco. Ora testo #4a4a4a, link oro scuro #8a6a00, hover #5c4500, credit webtomars.it con aura oro #ffc61a/#ffae00, occhio #b8860b.
- Per aggiornare un clone copiare: `_includes/head/custom.html`, `home-content.html`, `masthead.html`, la foto hero, `_includes/footer/custom.html` e le righe footer di `assets/css/main.scss`.
- gamingcorp2 e nato PRIMA di f36cd45 e potrebbe avere ancora il footer vecchio (bianco su bianco): da controllare e copiare.

## Note
- Memoria di Claude bloccata in questa chat perche si sono usati connettori: nulla salvato li. Questo file e il promemoria.
- Limite messaggi gratuiti Claude: ricaricati il 1 nov alle 01:50 (dal log della chat precedente).

## Aggiornamento sera (31/10/2026)
- Giochi da 41 a 71 (commit b9f200d): altre repo gaming con molte stelle, nomi di fantasia, screenshot veri dove possibile (script giochi3.py + costruisci_prodotti.py in claudetemp\giochi).
- Ora Tower Defense ha 2 giochi e Mobile 4. Restano da fare: foto categorie, controllo grafico, segnaposto, PageSpeed.
