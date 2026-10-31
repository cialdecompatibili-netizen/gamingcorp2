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

## Mappa giochi -> repo originale (per fork futuri)

Ogni gioco del negozio ha nome di fantasia; qui il progetto vero. Fork eventuale: `gh repo fork OWNER/REPO --clone=false` (oppure `gh repo fork OWNER/REPO --org NOMEORG`). Controlla la licenza prima di pubblicare un fork modificato: la lista e' CC0/CC BY-NC-SA, i giochi hanno licenze loro.

| # | Nome fantasia (IT) | Nome originale | Repo originale | Categoria | Link |
|---|---|---|---|---|---|
| 1 | Ipersonno Armato | Hypersomnia | `TeamHypersomnia/Hypersomnia` | azione | https://github.com/TeamHypersomnia/Hypersomnia |
| 2 | Cubo d'Assalto | AssaultCube | `assaultcube/AC` | sparatutto | https://github.com/assaultcube/AC |
| 3 | Pesce Saltatore | Jumpy | `fishfolk/jumpy` | platform | https://github.com/fishfolk/jumpy |
| 4 | Pinguino Supremo | SuperTux | `SuperTux/supertux` | platform | https://github.com/SuperTux/supertux |
| 5 | Il Re delle Potenze | 2048 | `gabrielecirulli/2048` | puzzle | https://github.com/gabrielecirulli/2048 |
| 6 | Scacchiera Eterna | Lichess | `ornicar/lila` | puzzle | https://github.com/ornicar/lila |
| 7 | Mahjong Infinito | Whatajong | `masylum/whatajong` | puzzle | https://github.com/masylum/whatajong |
| 8 | Esagono Cosmico | Hextris | `Hextris/hextris` | browser | https://github.com/Hextris/hextris |
| 9 | Fortezza dei Server | Server Survival | `pshenok/server-survival` | browser | https://github.com/pshenok/server-survival |
| 10 | Ascesa dei Morti | Dead Ascend | `larpon/DeadAscend` | avventura | https://github.com/larpon/DeadAscend |
| 11 | Cataclisma Oscuro | Cataclysm: Dark Days Ahead | `CleverRaven/Cataclysm-DDA` | gdr | https://github.com/CleverRaven/Cataclysm-DDA |
| 12 | Terre di Veloria | Veloren | `veloren/veloren` | gdr | https://github.com/veloren/veloren |
| 13 | Metropoli Futura | Citybound | `citybound/citybound` | gestionali | https://github.com/citybound/citybound |
| 14 | Asfalto in Derapata | VDrift | `VDrift/vdrift` | corse | https://github.com/VDrift/vdrift |
| 15 | Fisica d'Acciaio | Rigs of Rods | `RigsOfRods/rigs-of-rods` | corse | https://github.com/RigsOfRods/rigs-of-rods |
| 16 | Cubi Classici | ClassiCube | `ClassiCube/ClassiCube` | sandbox | https://github.com/ClassiCube/ClassiCube |
| 17 | Green dei Campioni | Open Golf | `mgerdes/Open-Golf` | sport | https://github.com/mgerdes/Open-Golf |
| 18 | Maestro del Biliardo | Pooltool | `ekiefl/pooltool` | sport | https://github.com/ekiefl/pooltool |
| 19 | Imperi Lontani | Widelands | `widelands/widelands` | strategia-tempo-reale | https://github.com/widelands/widelands |
| 20 | Impero Eterno | Unciv | `yairm210/Unciv` | strategia-a-turni | https://github.com/yairm210/Unciv |
| 21 | Abisso Redento | DevilutionX | `diasurgical/devilutionX` | classici-rinati | https://github.com/diasurgical/devilutionX |
| 22 | Memoria Arcana | Memory Game | `sromku/memory-game` | mobile | https://github.com/sromku/memory-game |
| 23 | Caccia agli Spettri | Chase Whisply | `tvbarthel/ChaseWhisplyProject` | mobile | https://github.com/tvbarthel/ChaseWhisplyProject |
| 24 | Guerrieri Pixel | Teeworlds | `teeworlds/teeworlds` | azione | https://github.com/teeworlds/teeworlds |
| 25 | Gli Invitti | Unvanquished | `Unvanquished/Unvanquished` | sparatutto | https://github.com/Unvanquished/Unvanquished |
| 26 | Cercatore del Reame | BrowserQuest | `mozilla/BrowserQuest` | browser | https://github.com/mozilla/BrowserQuest |
| 27 | Custode delle Vecchie Avventure | ScummVM | `scummvm/scummvm` | avventura | https://github.com/scummvm/scummvm |
| 28 | Abissi di Pietra | Dungeon Crawl Stone Soup | `crawl/crawl` | gdr | https://github.com/crawl/crawl |
| 29 | Imperatore dei Trasporti | OpenTTD | `OpenTTD/OpenTTD` | gestionali | https://github.com/OpenTTD/OpenTTD |
| 30 | Gran Premio dei Pinguini | SuperTuxKart | `supertuxkart/stk-code` | corse | https://github.com/supertuxkart/stk-code |
| 31 | Terre Cubiche | Luanti (Minetest) | `luanti-org/luanti` | sandbox | https://github.com/luanti-org/luanti |
| 32 | Mondo dei Blocchi Vivi | Terasology | `MovingBlocks/Terasology` | sandbox | https://github.com/MovingBlocks/Terasology |
| 33 | Fabbrica Fortezza | Mindustry | `Anuken/Mindustry` | difesa | https://github.com/Anuken/Mindustry |
| 34 | Fronte di Ferro | OpenRA | `OpenRA/OpenRA` | strategia-tempo-reale | https://github.com/OpenRA/OpenRA |
| 35 | Campo di Battaglia 2100 | Warzone 2100 | `Warzone2100/warzone2100` | strategia-tempo-reale | https://github.com/Warzone2100/warzone2100 |
| 36 | Battaglia per Eldoria | Battle for Wesnoth | `wesnoth/wesnoth` | strategia-a-turni | https://github.com/wesnoth/wesnoth |
| 37 | Mondi in Evoluzione | Freeciv | `freeciv/freeciv` | strategia-a-turni | https://github.com/freeciv/freeciv |
| 38 | Leggenda dei Cantastorie | Stendhal | `arianne/stendhal` | online | https://github.com/arianne/stendhal |
| 39 | Meridiano Antico | Meridian 59 | `Meridian59/Meridian59` | online | https://github.com/Meridian59/Meridian59 |
| 40 | Inferno Classico | Chocolate Doom | `chocolate-doom/chocolate-doom` | classici-rinati | https://github.com/chocolate-doom/chocolate-doom |
| 41 | Cronache Riaperte | OpenMW | `OpenMW/openmw` | classici-rinati | https://github.com/OpenMW/openmw |
| 42 | Ritmo Infinito | osu! | `ppy/osu` | azione | https://github.com/ppy/osu |
| 43 | Serpente degli Eroi | SNKRX | `a327ex/SNKRX` | azione | https://github.com/a327ex/SNKRX |
| 44 | Rotta tra le Stelle | Endless Sky | `endless-sky/endless-sky` | avventura | https://github.com/endless-sky/endless-sky |
| 45 | Artigiano di Cubi | Craft | `fogleman/Craft` | sandbox | https://github.com/fogleman/Craft |
| 46 | Cubi Senza Confini | Cubyz | `PixelGuys/Cubyz` | sandbox | https://github.com/PixelGuys/Cubyz |
| 47 | Cripta Eterna | NetHack | `NetHack/NetHack` | gdr | https://github.com/NetHack/NetHack |
| 48 | Discesa Minimalista | Brogue CE | `tmewett/BrogueCE` | gdr | https://github.com/tmewett/BrogueCE |
| 49 | Tana dei Draghi | Angband | `angband/angband` | gdr | https://github.com/angband/angband |
| 50 | Ballata dei Cavalieri | Godot Open RPG | `gdquest-demos/godot-open-rpg` | gdr | https://github.com/gdquest-demos/godot-open-rpg |
| 51 | Skyline Isometrico | IsoCity | `victorqribeiro/isocity` | gestionali | https://github.com/victorqribeiro/isocity |
| 52 | Fondatori di Citta | Cytopia | `CytopiaTeam/Cytopia` | gestionali | https://github.com/CytopiaTeam/Cytopia |
| 53 | Metropoli Senza Griglia | Egregoria | `Uriopass/Egregoria` | gestionali | https://github.com/Uriopass/Egregoria |
| 54 | Corsa Sfrenata | Racing Game | `pmndrs/racing-game` | corse | https://github.com/pmndrs/racing-game |
| 55 | Corsa Antigravita | HexGL | `BKcore/HexGL` | corse | https://github.com/BKcore/HexGL |
| 56 | Arena delle Bestie | Ancient Beast | `FreezingMoon/AncientBeast` | strategia-a-turni | https://github.com/FreezingMoon/AncientBeast |
| 57 | Guerra dei Continenti | TripleA | `triplea-game/triplea` | strategia-a-turni | https://github.com/triplea-game/triplea |
| 58 | Conquista Globale | OpenFront | `openfrontio/OpenFrontIO` | strategia-tempo-reale | https://github.com/openfrontio/OpenFrontIO |
| 59 | Comandante Libero | Godot Open RTS | `lampe-games/godot-open-rts` | strategia-tempo-reale | https://github.com/lampe-games/godot-open-rts |
| 60 | Alchimista dei Cubi | Cube Composer | `sharkdp/cube-composer` | puzzle | https://github.com/sharkdp/cube-composer |
| 61 | Guerriero del Codice | WarriorJS | `olistic/warriorjs` | puzzle | https://github.com/olistic/warriorjs |
| 62 | Torre di Blocchi | React Tetris | `chvin/react-tetris` | puzzle | https://github.com/chvin/react-tetris |
| 63 | Blocchi in Duello | Flatris | `ovidiuch/flatris` | puzzle | https://github.com/ovidiuch/flatris |
| 64 | Mazzo dei Solitari | PySolFC | `shlomif/PySolFC` | puzzle | https://github.com/shlomif/PySolFC |
| 65 | Labirinto Famelico | Pacman HTML5 | `mumuy/pacman` | browser | https://github.com/mumuy/pacman |
| 66 | Mondi Biomi | Biomes | `ill-inc/biomes-game` | online | https://github.com/ill-inc/biomes-game |
| 67 | Saga del Regno Pixel | Kaetram | `Kaetram/Kaetram-Open` | online | https://github.com/Kaetram/Kaetram-Open |
| 68 | Cercatore di Mine | Antimine | `lucasnlm/antimine-android` | mobile | https://github.com/lucasnlm/antimine-android |
| 69 | Mattoni Sospesi | Compose Tetris | `vitaviva/compose-tetris` | mobile | https://github.com/vitaviva/compose-tetris |
| 70 | Grotta dei Ricordi | doukutsu-rs | `doukutsu-rs/doukutsu-rs` | classici-rinati | https://github.com/doukutsu-rs/doukutsu-rs |
| 71 | Baluardo dell'Impero | TowerDefense GameFramework Demo | `DrFlower/TowerDefense-GameFramework-Demo` | difesa | https://github.com/DrFlower/TowerDefense-GameFramework-Demo |

Fonti per cercarne altri: `_fonti/file.md` (bobeff/open-source-games, leereilly/games). Script: `claudetemp\giochi\giochi3.py` (lista G3) + `costruisci_prodotti.py`.

### Aggiunta 31/10 sera: giochi 72-95 (script giochi4.py)

| # | Nome fantasia (IT) | Nome originale | Repo originale | Categoria | Link |
|---|---|---|---|---|---|
| 72 | Sotterranei di Pixel | Pixel Dungeon | `watabou/pixel-dungeon` | gdr | https://github.com/watabou/pixel-dungeon |
| 73 | Duello degli Arconti | Duelyst | `open-duelyst/duelyst` | online | https://github.com/open-duelyst/duelyst |
| 74 | Parole Isometriche | isowords | `pointfreeco/isowords` | mobile | https://github.com/pointfreeco/isowords |
| 75 | Maestro dei Mazzi | Forge | `Card-Forge/forge` | strategia-a-turni | https://github.com/Card-Forge/forge |
| 76 | Civilta nel Browser | Freeciv-web | `freeciv/freeciv-web` | strategia-a-turni | https://github.com/freeciv/freeciv-web |
| 77 | Crisi di Atena | Athena Crisis | `nkzw-tech/athena-crisis` | strategia-a-turni | https://github.com/nkzw-tech/athena-crisis |
| 78 | Colonie Libere | FreeCol | `FreeCol/freecol` | strategia-a-turni | https://github.com/FreeCol/freecol |
| 79 | Signore delle Stelle | Star Ruler 2 | `BlindMindStudios/StarRuler2-Source` | strategia-tempo-reale | https://github.com/BlindMindStudios/StarRuler2-Source |
| 80 | Fronte Aperto | OpenRTS | `methusalah/OpenRTS` | strategia-tempo-reale | https://github.com/methusalah/OpenRTS |
| 81 | Colonie di Ferro | OpenHV | `OpenHV/OpenHV` | strategia-tempo-reale | https://github.com/OpenHV/OpenHV |
| 82 | Una Vita Sola | One Hour One Life | `jasonrohrer/OneLife` | online | https://github.com/jasonrohrer/OneLife |
| 83 | Rettilineo Retro | JavaScript Racer | `jakesgordon/javascript-racer` | corse | https://github.com/jakesgordon/javascript-racer |
| 84 | Corridore Rosso | Red Runner | `BayatGames/RedRunner` | platform | https://github.com/BayatGames/RedRunner |
| 85 | Squadra in Corsa | DDraceNetwork | `ddnet/ddnet` | platform | https://github.com/ddnet/ddnet |
| 86 | Officina degli Enigmi | PuzzleScript | `increpare/PuzzleScript` | puzzle | https://github.com/increpare/PuzzleScript |
| 87 | Regno di Reia | Reia | `Quaint-Studios/Reia` | gdr | https://github.com/Quaint-Studios/Reia |
| 88 | Domani Maledetto | Cursed Tomorrow | `AhmadHassan-BTed/CursedTomorrow` | avventura | https://github.com/AhmadHassan-BTed/CursedTomorrow |
| 89 | Sentiero dei Byte | BYTEPATH | `a327ex/BYTEPATH` | azione | https://github.com/a327ex/BYTEPATH |
| 90 | Scacchi in Tasca | Lichess Mobile | `lichess-org/mobile` | mobile | https://github.com/lichess-org/mobile |
| 91 | Potenze di Due | 2048 Android | `uberspot/2048-android` | mobile | https://github.com/uberspot/2048-android |
| 92 | Blocchi Dispettosi | Hatetris | `qntm/hatetris` | puzzle | https://github.com/qntm/hatetris |
| 93 | Mattoncini Vue | Vue Tetris | `Binaryify/vue-tetris` | browser | https://github.com/Binaryify/vue-tetris |
| 94 | Sala Giochi da Console | dotnet console games | `dotnet/dotnet-console-games` | sport | https://github.com/dotnet/dotnet-console-games |
| 95 | Laboratorio dei Giochi | microStudio | `pmgl/microstudio` | sandbox | https://github.com/pmgl/microstudio |

Esclusi: motori/strumenti (pixijs, GDevelop, libgdx), riscritture di giochi commerciali che richiedono asset originali (OpenRCT2, openage, fheroes2, CorsixTH, OpenJK), Barotrauma (senza licenza chiara), cloni con marchi altrui (Pokemon Auto Chess). Totale ora: 95 giochi.
