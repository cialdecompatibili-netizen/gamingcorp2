import json, os, io
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# (id, it, en, slug_en, icona, desc_it, desc_en)
C = [
 ("azione","Azione & Arcade","Action & Arcade","action-arcade","\u2694\ufe0f","Picchiaduro, sparatutto a scorrimento e arcade open source da giocare subito.","Open source brawlers, shoot 'em ups and arcade games you can play right away."),
 ("sparatutto","Sparatutto FPS & TPS","Shooters FPS & TPS","shooters","\U0001F52B","Sparatutto in prima e terza persona, dai classici ai moderni.","First and third person shooters, from classics to modern ones."),
 ("platform","Platform","Platformers","platformers","\U0001F344","Giochi di salti e piattaforme, retro e moderni.","Retro and modern jump-and-run platform games."),
 ("avventura","Avventura & Punta e Clicca","Adventure & Point and Click","adventure","\U0001F5FA\ufe0f","Storie, enigmi ed esplorazione: avventure grafiche open source.","Stories, puzzles and exploration: open source adventure games."),
 ("gdr","GDR & Roguelike","RPG & Roguelike","rpg-roguelike","\U0001F409","Giochi di ruolo, dungeon crawler e roguelike con codice aperto.","Role-playing games, dungeon crawlers and open source roguelikes."),
 ("online","Mondi Online MMO","Online Worlds MMO","online-worlds","\U0001F310","Mondi multiplayer persistenti e MMORPG open source.","Persistent multiplayer worlds and open source MMORPGs."),
 ("strategia-tempo-reale","Strategia in Tempo Reale","Real-Time Strategy","real-time-strategy","\u26A1","Costruisci basi, comanda eserciti: RTS e rifacimenti dei grandi classici.","Build bases, command armies: RTS games and remakes of the great classics."),
 ("strategia-a-turni","Strategia a Turni","Turn-Based Strategy","turn-based-strategy","\u265F\ufe0f","Strategia a turni, 4X e wargame per pensare con calma.","Turn-based strategy, 4X and wargames for slow thinkers."),
 ("gestionali","Gestionali & Citta","Tycoon & City Building","tycoon-city-building","\U0001F3D9\ufe0f","Costruisci citta, aziende e imperi: tycoon e city builder open source.","Build cities, companies and empires: open source tycoon and city builders."),
 ("corse","Corse","Racing","racing","\U0001F3CE\ufe0f","Giochi di guida e corse, da arcade a simulazione.","Driving and racing games, from arcade to simulation."),
 ("puzzle","Puzzle & Giochi da Tavolo","Puzzle & Board Games","puzzle-board","\U0001F9E9","Rompicapo, carte e giochi da tavolo da giocare anche in browser.","Puzzles, card and board games you can also play in the browser."),
 ("sandbox","Sandbox & Costruzione","Sandbox & Building","sandbox-building","\u26CF\ufe0f","Mondi aperti da esplorare, scavare e costruire in libertà.","Open worlds to explore, dig and build freely."),
 ("sport","Sport","Sports","sports","\u26BD","Calcio, basket e altri sport in versione open source.","Football, basketball and other sports, open source style."),
 ("difesa","Tower Defense","Tower Defense","tower-defense","\U0001F3F0","Difendi la base con torri e strategia.","Defend your base with towers and strategy."),
 ("classici-rinati","Classici Rinati","Reborn Classics","reborn-classics","\U0001F579\ufe0f","Source port e rifacimenti di Doom, Quake, Diablo, Warcraft e altri miti.","Source ports and remakes of Doom, Quake, Diablo, Warcraft and other legends."),
 ("browser","Giochi nel Browser","Browser Games","browser-games","\U0001F30D","Si giocano subito dal browser, senza installare nulla.","Play instantly in your browser, nothing to install."),
 ("mobile","Giochi Mobile","Mobile Games","mobile-games","\U0001F4F1","Giochi open source per Android e iOS.","Open source games for Android and iOS."),
]
def w(p, s):
    p = os.path.join(R, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, "w", encoding="utf-8", newline="\n") as f: f.write(s)
cp = os.path.join(R, "_data", "catalogo.json")
d = json.load(io.open(cp, encoding="utf-8"))
d["categorie"] = [{"nome": it, "id": i, "icona": ic, "tr": {"en": {"nome": en}}} for i, it, en, sl, ic, di, de in C]
d["prodotti"] = []
io.open(cp, "w", encoding="utf-8", newline="\n").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
sp = os.path.join(R, "_data", "shop-categorie.json")
io.open(sp, "w", encoding="utf-8", newline="\n").write(json.dumps([{"nome": it, "slug": i} for i, it, *_ in C], ensure_ascii=False, indent=2) + "\n")
for f in ["_negozio/categoria-esempio.md", "_negozio/prodotto-esempio.md", "en/negozio/prodotto-esempio.md", "en/negozio/categoria/esempio.md"]:
    p = os.path.join(R, f)
    if os.path.exists(p): os.remove(p)
for i, it, en, sl, ic, di, de in C:
    w("_negozio/categoria-%s.md" % i, '---\nlayout: negozio-categoria\ntitle: "%s"\ncid: %s\npermalink: /negozio/categoria/%s/\ndescription: "%s"\nref: shop-cat-%s\n---\n' % (it, i, i, di, i))
    w("en/negozio/categoria/%s.md" % i, '---\nlayout: negozio-categoria\ntitle: "%s"\ncid: %s\npermalink: /en/shop/category/%s/\ndescription: "%s"\nlang: en\nlocale: en\nref: shop-cat-%s\ntr: tradotto\n---\n' % (en, i, sl, de, i))
print("categorie:", len(C))
