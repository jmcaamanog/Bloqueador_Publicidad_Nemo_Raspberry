# Pi-hole — Native Ads / Clickbait / Ad-Tech Blocklist (2026)

**Versión:** 2026-08-14  
**Objetivo:** reducir anuncios de contenido recomendado, clickbait, advertorials de salud/hogar, publicidad nativa, push ads, pop-under y parte del ecosistema ad-tech/trackers mediante DNS.

> **Importante:** Pi-hole filtra consultas DNS. No puede leer el texto o HTML del anuncio y, por tanto, no existe una regla DNS fiable que signifique «bloquea cualquier anuncio que diga salud, dolor, casa, etc.». La estrategia correcta es bloquear las redes/servidores que entregan esas creatividades.

## Qué contiene

- **01_NATIVE_CONTENT_RECOMMENDATION** — Taboola, Outbrain/Teads, MGID, RevContent, MediaGo, ZergNet y similares.
- **02_NATIVE_PROGRAMMATIC** — redes de publicidad nativa/programática.
- **03_AD_EXCHANGES_SSP_DSP** — exchanges y plataformas de puja publicitaria.
- **04_PUSH_POP_POPUNDER** — push ads, in-page push, pop-under y formatos agresivos.
- **05_DISPLAY_VIDEO_AD_SERVERS** — servidores de anuncios display/video.
- **06_TRACKING_AND_MEASUREMENT_ADTECH** — medición y tracking publicitario.
- **07_ADDITIONAL_CLICKBAIT_OR_AFFILIATE_NETWORKS** — afiliación, recomendadores y monetización contextual.
- **08_KNOWN_ADTECH_CDN_AND_SUBDOMAIN_FAMILIES** — endpoints concretos conocidos.
- **09_OPTIONAL_AGGRESSIVE** — bloqueos más agresivos que pueden afectar funcionalidad legítima.

## Importante sobre el nivel de bloqueo

Las secciones **01–04** son las más relacionadas con tu objetivo original y son las que recomiendo activar primero.

Las secciones **05–08** son más amplias: pueden eliminar mucha publicidad, pero también pueden romper vídeo, comentarios, login, medición o determinadas funciones de webs.

La sección **09** es deliberadamente agresiva. Úsala solo si quieres priorizar bloqueo sobre compatibilidad.

Pi-hole da prioridad a las reglas de allowlist sobre las de denylist, por lo que puedes crear excepciones para webs concretas que se rompan. citeturn398343search0

## Uso del archivo `.conf`

El archivo `.conf` adjunto contiene **una regex por línea**, con comentarios de sección. No es un fichero `dnsmasq.conf` genérico: está preparado como colección de reglas para Pi-hole.

Para cargarlo desde consola:

```bash
grep -vE '^\s*(#|$)' pihole_ads_clickbait_native_2026.conf | while IFS= read -r rule; do
  sudo pihole --regex "$rule"
done
```

Después:

```bash
sudo pihole reloadlists
```

Pi-hole documenta `pihole --regex` para añadir regex y `pihole reloadlists` para recargar las listas/regex. citeturn398343search0turn398343search3

## Alternativa recomendada: cargar por capas

### Capa 1 — objetivo principal

Activa:

- 01_NATIVE_CONTENT_RECOMMENDATION
- 04_PUSH_POP_POPUNDER

### Capa 2 — bloqueo publicitario amplio

Añade:

- 02_NATIVE_PROGRAMMATIC
- 03_AD_EXCHANGES_SSP_DSP
- 05_DISPLAY_VIDEO_AD_SERVERS

### Capa 3 — privacidad

Añade:

- 06_TRACKING_AND_MEASUREMENT_ADTECH

### Capa 4 — muy agresiva

Añade:

- 07_ADDITIONAL_CLICKBAIT_OR_AFFILIATE_NETWORKS
- 08_KNOWN_ADTECH_CDN_AND_SUBDOMAIN_FAMILIES
- 09_OPTIONAL_AGGRESSIVE

## Comprobación

Después de instalar, revisa:

```bash
pihole tail
```

y prueba una web donde normalmente aparezcan los widgets.

Para comprobar una regex concreta:

```bash
pihole --regex '^example\.com$'
```

También puedes revisar el Query Log de Pi-hole para identificar qué dominio real está sirviendo el contenido.

## Fuentes y criterio

La documentación oficial de Pi-hole explica que sus regex se aplican sobre el dominio consultado y recomienda anclar coincidencias con `^` y `$` para evitar coincidencias parciales no deseadas. citeturn398343search2

La documentación actual de Pi-hole también confirma que las regex se almacenan como denylist/allowlist y que la allowlist tiene prioridad. citeturn398343search0turn398343search13

Para el ecosistema de publicidad nativa, referencias recientes de 2026 identifican como actores principales a Taboola, Outbrain/Teads, MGID, RevContent y MediaGo, junto con Nativo, TripleLift y otras plataformas. citeturn398343search7turn398343search8turn398343search10

Las redes de push/pop incluidas se han elegido porque anuncian explícitamente formatos como push, in-page push y popunder; por ejemplo, PropellerAds describe esos formatos públicamente. citeturn398343search9

Como comprobación adicional de dominios, se han contrastado familias de Taboola, Outbrain, MGID, PubMatic, OpenX, Rubicon, Index Exchange, Sharethrough, Teads y otras con listados técnicos públicos. citeturn986911search0turn986911search1

## Advertencias

1. **No bloquees indiscriminadamente `ads.*`, `ad.*`, `cdn.*` o palabras como `content`**. Puedes romper sitios legítimos.
2. **Google/YouTube/Microsoft/Amazon** tienen ecosistemas publicitarios integrados con servicios legítimos. Por eso se han dejado en una sección opcional y no en el núcleo.
3. Las plataformas publicitarias cambian dominios, CDN y endpoints. Una lista estática nunca será perfecta.
4. Para conseguir el máximo resultado, combina esta colección con una buena gravity list generalista y revisa periódicamente el Query Log.
5. Si una web deja de funcionar, primero busca el dominio bloqueado en el Query Log y crea una excepción concreta en vez de desactivar todo el conjunto.

## Reglas incluidas

Total de regex únicas: **201**


### 01_NATIVE_CONTENT_RECOMMENDATION

- `(^|\.)taboola\.com$`
- `(^|\.)taboola\.net$`
- `(^|\.)taboolasyndication\.com$`
- `(^|\.)outbrain\.com$`
- `(^|\.)outbrainimg\.com$`
- `(^|\.)mgid\.com$`
- `(^|\.)revcontent\.com$`
- `(^|\.)zergnet\.com$`
- `(^|\.)mediago\.com$`
- `(^|\.)mediago\.io$`
- `(^|\.)content\.ad$`
- `(^|\.)content-ad\.net$`
- `(^|\.)contentad\.io$`
- `(^|\.)contentabc\.com$`
- `(^|\.)contentstream\.pl$`
- `(^|\.)zemanta\.com$`
- `(^|\.)nativo\.com$`
- `(^|\.)plista\.com$`
- `(^|\.)dianomi\.com$`
- `(^|\.)engageya\.com$`
- `(^|\.)connatix\.com$`
- `(^|\.)vidazoo\.com$`
- `(^|\.)adblade\.com$`
- `(^|\.)adblade\.org$`
- `(^|\.)adskeeper\.com$`
- `(^|\.)bidgear\.com$`
- `(^|\.)outbrainimg\.com$`

### 02_NATIVE_PROGRAMMATIC

- `(^|\.)teads\.tv$`
- `(^|\.)teadstv\.com$`
- `(^|\.)sharethrough\.com$`
- `(^|\.)triplelift\.com$`
- `(^|\.)3lift\.com$`
- `(^|\.)gumgum\.com$`
- `(^|\.)sovrn\.com$`
- `(^|\.)lijit\.com$`
- `(^|\.)sonobi\.com$`
- `(^|\.)33across\.com$`
- `(^|\.)yieldmo\.com$`
- `(^|\.)conversantmedia\.com$`
- `(^|\.)districtm\.io$`
- `(^|\.)smartadserver\.com$`
- `(^|\.)adform\.net$`
- `(^|\.)adkernel\.com$`
- `(^|\.)adition\.com$`
- `(^|\.)adscale\.de$`
- `(^|\.)gemius\.com$`
- `(^|\.)yieldlove\.com$`

### 03_AD_EXCHANGES_SSP_DSP

- `(^|\.)adnxs\.com$`
- `(^|\.)adsrvr\.org$`
- `(^|\.)openx\.net$`
- `(^|\.)pubmatic\.com$`
- `(^|\.)rubiconproject\.com$`
- `(^|\.)indexexchange\.com$`
- `(^|\.)contextweb\.com$`
- `(^|\.)media\.net$`
- `(^|\.)criteo\.com$`
- `(^|\.)criteo\.net$`
- `(^|\.)casalemedia\.com$`
- `(^|\.)33across\.com$`
- `(^|\.)spotxchange\.com$`
- `(^|\.)spotx\.tv$`
- `(^|\.)sonobi\.com$`
- `(^|\.)bidswitch\.net$`
- `(^|\.)bidtellect\.com$`
- `(^|\.)bidvertiser\.com$`
- `(^|\.)smartadserver\.com$`
- `(^|\.)adkernel\.com$`
- `(^|\.)adform\.net$`
- `(^|\.)appnexus\.com$`
- `(^|\.)smaato\.net$`
- `(^|\.)rhythmone\.com$`
- `(^|\.)undertone\.com$`
- `(^|\.)reklamstore\.com$`
- `(^|\.)admanmedia\.com$`
- `(^|\.)adunity\.com$`

### 04_PUSH_POP_POPUNDER

- `(^|\.)propellerads\.com$`
- `(^|\.)propellerads\.net$`
- `(^|\.)adsterra\.com$`
- `(^|\.)adsterra\.network$`
- `(^|\.)admaven\.com$`
- `(^|\.)richads\.com$`
- `(^|\.)evadav\.com$`
- `(^|\.)clickadu\.com$`
- `(^|\.)pushground\.com$`
- `(^|\.)hilltopads\.net$`
- `(^|\.)zeropark\.com$`
- `(^|\.)popads\.net$`
- `(^|\.)popcash\.net$`
- `(^|\.)trafficjunky\.net$`
- `(^|\.)exoclick\.com$`
- `(^|\.)exosrv\.com$`
- `(^|\.)adnium\.com$`
- `(^|\.)adcash\.com$`
- `(^|\.)trafficstars\.com$`
- `(^|\.)trafficfactory\.biz$`
- `(^|\.)clickcertain\.com$`
- `(^|\.)pushhouse\.org$`
- `(^|\.)izooto\.com$`
- `(^|\.)pushwoosh\.com$`
- `(^|\.)cleverpush\.com$`

### 05_DISPLAY_VIDEO_AD_SERVERS

- `(^|\.)doubleclick\.net$`
- `(^|\.)googlesyndication\.com$`
- `(^|\.)googleadservices\.com$`
- `(^|\.)adservice\.google\.com$`
- `(^|\.)2mdn\.net$`
- `(^|\.)adsensecamp\.com$`
- `(^|\.)adskeeper\.co$`
- `(^|\.)adroll\.com$`
- `(^|\.)advertising\.com$`
- `(^|\.)serving-sys\.com$`
- `(^|\.)adtech\.de$`
- `(^|\.)adtech\.com$`
- `(^|\.)adswizz\.com$`
- `(^|\.)smartadserver\.com$`
- `(^|\.)gumgum\.com$`
- `(^|\.)kargo\.com$`
- `(^|\.)undertone\.com$`
- `(^|\.)tremorhub\.com$`
- `(^|\.)rhythmone\.com$`
- `(^|\.)videoamp\.com$`
- `(^|\.)springserve\.com$`
- `(^|\.)jwplayer\.com$`
- `(^|\.)jwpsrv\.com$`
- `(^|\.)primis\.tech$`
- `(^|\.)vidoomy\.com$`
- `(^|\.)spotim\.io$`

### 06_TRACKING_AND_MEASUREMENT_ADTECH

- `(^|\.)doubleverify\.com$`
- `(^|\.)adsafeprotected\.com$`
- `(^|\.)insightexpressai\.com$`
- `(^|\.)moatads\.com$`
- `(^|\.)quantserve\.com$`
- `(^|\.)scorecardresearch\.com$`
- `(^|\.)imrworldwide\.com$`
- `(^|\.)bluekai\.com$`
- `(^|\.)rlcdn\.com$`
- `(^|\.)crwdcntrl\.net$`
- `(^|\.)demdex\.net$`
- `(^|\.)everesttech\.net$`
- `(^|\.)eyeota\.net$`
- `(^|\.)tapad\.com$`
- `(^|\.)liadm\.com$`
- `(^|\.)mookie1\.com$`
- `(^|\.)addthis\.com$`
- `(^|\.)sharethis\.com$`
- `(^|\.)clarity\.ms$`
- `(^|\.)omnitagjs\.com$`

### 07_ADDITIONAL_CLICKBAIT_OR_AFFILIATE_NETWORKS

- `(^|\.)revprotect\.com$`
- `(^|\.)reward-style\.com$`
- `(^|\.)skimresources\.com$`
- `(^|\.)skimlinks\.com$`
- `(^|\.)viglink\.com$`
- `(^|\.)sovrn\.com$`
- `(^|\.)infolinks\.com$`
- `(^|\.)kontera\.com$`
- `(^|\.)contextly\.com$`
- `(^|\.)adversal\.com$`
- `(^|\.)buysellads\.com$`
- `(^|\.)carbonads\.net$`
- `(^|\.)mediaforge\.com$`
- `(^|\.)bidfluence\.com$`
- `(^|\.)adpushup\.com$`
- `(^|\.)monetizemore\.com$`
- `(^|\.)freestar\.com$`
- `(^|\.)snigel\.com$`
- `(^|\.)playwire\.com$`
- `(^|\.)publift\.com$`

### 08_KNOWN_ADTECH_CDN_AND_SUBDOMAIN_FAMILIES

- `(^|\.)cdn\.taboola\.com$`
- `(^|\.)trc\.taboola\.com$`
- `(^|\.)images\.taboola\.com$`
- `(^|\.)nr\.taboola\.com$`
- `(^|\.)api\.taboola\.com$`
- `(^|\.)widgets\.outbrain\.com$`
- `(^|\.)log\.outbrain\.com$`
- `(^|\.)odb\.outbrain\.com$`
- `(^|\.)images\.outbrain\.com$`
- `(^|\.)cdn\.mgid\.com$`
- `(^|\.)servicer\.mgid\.com$`
- `(^|\.)counter\.mgid\.com$`
- `(^|\.)img\.mgid\.com$`
- `(^|\.)images\.revmcontent\.com$`
- `(^|\.)img\.revcontent\.com$`
- `(^|\.)a\.teads\.tv$`
- `(^|\.)cdn\.teads\.tv$`
- `(^|\.)rtb\.openx\.net$`
- `(^|\.)us-ads\.openx\.net$`
- `(^|\.)ads\.pubmatic\.com$`
- `(^|\.)hbopenbid\.pubmatic\.com$`
- `(^|\.)pixel\.rubiconproject\.com$`
- `(^|\.)fastlane\.rubiconproject\.com$`
- `(^|\.)cdn\.indexexchange\.com$`
- `(^|\.)eb2\.3lift\.com$`
- `(^|\.)tlx\.3lift\.com$`
- `(^|\.)apex\.go\.sonobi\.com$`
- `(^|\.)c\.gumgum\.com$`
- `(^|\.)cdn\.kargo\.com$`
- `(^|\.)sync\.kargo\.com$`
- `(^|\.)import\.adsrvr\.org$`

### 09_OPTIONAL_AGGRESSIVE

- `(^|\.)amazon-adsystem\.com$`
- `(^|\.)ads\.microsoft\.com$`
- `(^|\.)bat\.bing\.com$`
- `(^|\.)ads\.yahoo\.com$`
- `(^|\.)adfox\.yandex\.ru$`
- `(^|\.)metrika\.yandex\.ru$`
- `(^|\.)appmetrica\.yandex\.ru$`
- `(^|\.)unityads\.unity3d\.com$`
- `(^|\.)applovin\.com$`
- `(^|\.)vungle\.com$`
- `(^|\.)liftoff\.io$`
- `(^|\.)chartboost\.com$`
- `(^|\.)inmobi\.com$`
- `(^|\.)startappservice\.com$`
- `(^|\.)ironSource\.mobi$`
