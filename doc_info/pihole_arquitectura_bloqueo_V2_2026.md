# Pi-hole — Arquitectura de bloqueo avanzada V2 (2026)

**Fecha:** 14/08/2026  
**Objetivo:** diseñar una instalación de Pi-hole orientada a bloquear publicidad, publicidad nativa/clickbait, trackers, malvertising, popups/popunders, redirects y bypass de DNS, sin caer en una colección inmanejable de listas duplicadas o falsos positivos.

---

## 1. Idea fundamental

Pi-hole es un **filtro DNS**.

Puede impedir que un dispositivo resuelva:

- `taboola.com`
- `outbrain.com`
- `mgid.com`
- `doubleclick.net`
- dominios de tracking
- dominios de malware
- dominios de phishing
- infraestructura de popups/popunders

Pero no puede, por sí solo, hacer todo lo que hace un bloqueador dentro del navegador.

### Pi-hole no puede sustituir completamente a uBlock Origin

Hay problemas que requieren actuar sobre la página:

- ocultar un `div`
- eliminar un banner HTML
- bloquear un script concreto mientras se permite el resto del dominio
- aplicar filtros cosméticos
- modificar el DOM
- bloquear algunos anuncios servidos desde el mismo dominio que la web
- determinados mecanismos anti-adblock
- algunos anuncios de vídeo que utilizan la infraestructura del propio proveedor

Por eso la arquitectura recomendada es:

```text
Internet
   │
   ▼
Router / Firewall
   │
   ├── Fuerza DNS hacia Pi-hole
   ├── Evita DNS externo
   ├── Controla IPv4
   └── Controla IPv6
   │
   ▼
Pi-hole
   │
   ├── Gravity lists
   ├── Regex
   ├── CNAME inspection
   ├── Malware / phishing
   ├── Ad-tech / tracking
   └── Protección contra DNS bypass
   │
   ▼
Navegador
   │
   └── uBlock Origin / EasyList / EasyPrivacy
```

---

# 2. Arquitectura recomendada

## Capa A — Pi-hole como primera línea

Debe encargarse de:

- publicidad DNS
- trackers
- ad-tech
- publicidad nativa
- clickbait
- malvertising
- malware
- phishing
- scams
- redirects
- popups
- popunders
- push advertising
- dominios de fingerprinting
- infraestructura de medición publicitaria
- dominios de afiliación
- parte del ecosistema de CNAME cloaking

## Capa B — Router / Firewall

Debe encargarse de:

- forzar DNS
- bloquear DNS externo
- controlar IPv4
- controlar IPv6
- bloquear DoT cuando sea necesario
- controlar DNS over QUIC
- reducir bypass por DNS alternativo

## Capa C — Navegador

Debe encargarse de:

- filtros cosméticos
- DOM
- scripts
- elementos HTML
- anuncios first-party
- video ads
- anti-adblock
- filtros de URL
- elementos in-page
- contenido patrocinado que comparte dominio con la web

---

# 3. Publicidad nativa / Content Discovery

Esta es la categoría principal para el objetivo original.

## Plataformas y familias

### Taboola

- `taboola.com`
- `taboola.net`
- `taboolasyndication.com`

### Outbrain

- `outbrain.com`
- `outbrainimg.com`
- `widgets.outbrain.com`

### Teads

- `teads.tv`
- `teadstv.com`

Outbrain y Teads deben contemplarse juntos en una arquitectura moderna de publicidad nativa, porque la actividad y oferta comercial de ambas plataformas está relacionada actualmente.

### MGID

- `mgid.com`

### MediaGo

- `mediago.com`
- `mediago.io`

### RevContent

- `revcontent.com`

### ZergNet

- `zergnet.com`

### Nativo

- `nativo.com`

### Dianomi

- `dianomi.com`

### ConnatiX

- `connatix.com`

### Vidazoo

- `vidazoo.com`

### Plista

- `plista.com`

### Zemanta

- `zemanta.com`

### EngageYa

- `engageya.com`

### Content.ad

- `content.ad`
- `content-ad.net`
- `contentad.io`

### Adblade

- `adblade.com`
- `adblade.org`

### AdsKeeper

- `adskeeper.com`

### Bidegar / Bidgear

- `bidgear.com`

---

# 4. Formatos de publicidad nativa que deben contemplarse

No hay una palabra DNS que bloquee estos formatos. Hay que bloquear la infraestructura que los entrega.

## Formatos

- Recommended for you
- Recommended stories
- Sponsored content
- Sponsored stories
- You may also like
- More from around the web
- From around the web
- Promoted content
- Native ads
- In-feed ads
- Article recommendation
- Content recommendation
- Commerce recommendation
- Related content
- Recommended videos
- Sponsored links
- Advertorial
- Branded content
- Discovery ads
- Content discovery

Ejemplos típicos de contenido:

- pérdida de peso milagrosa
- suplementos
- dolor de espalda
- dolor de rodilla
- "médicos no quieren que conozcas..."
- "el truco que..."
- "lo que ocurre si..."
- bricolaje milagroso
- productos domésticos
- ofertas falsas
- advertorials de salud
- productos financieros engañosos
- falsos tests
- páginas de "listas" clickbait

Pi-hole no debe bloquear palabras como `health`, `home`, `pain` o `weight`.

La estrategia correcta es bloquear el **proveedor o dominio de entrega**.

---

# 5. Ad Exchanges / SSP / DSP

## Ad exchanges

- AppNexus / Xandr
- PubMatic
- OpenX
- Rubicon Project / Magnite
- Index Exchange
- OpenWeb / context-ad systems
- Smaato
- BidSwitch
- Bidtellect
- Sonobi
- Smart AdServer
- TripleLift
- Sharethrough

### Ejemplos

```text
adnxs.com
appnexus.com
pubmatic.com
openx.net
rubiconproject.com
indexexchange.com
bidswitch.net
bidtellect.com
sonobi.com
smartadserver.com
3lift.com
sharethrough.com
```

## DSP / programática

También merece la pena cubrir plataformas que participan en compra automatizada:

- The Trade Desk
- MediaMath / infraestructura sucesora
- Criteo
- Amazon Ads
- Adobe Advertising
- LiveRamp
- Yahoo DSP
- Microsoft Advertising
- Xandr
- MediaGo

No siempre deben ir en la lista más agresiva, porque algunas tienen componentes legítimos que pueden afectar funcionalidades.

---

# 6. Display y vídeo

## Categorías

- display ads
- banner ads
- video ads
- pre-roll
- mid-roll
- post-roll
- outstream
- in-stream
- overlays
- interstitials
- video recommendation

## Familias

- Google Ads / DoubleClick
- Google Syndication
- Criteo
- Advertising.com
- AdRoll
- Teads
- SpotX / Magnite
- SpringServe
- Primis
- JW Player advertising infrastructure
- GumGum
- Kargo
- Undertone
- RhythmOne

### Ejemplos

```text
doubleclick.net
googlesyndication.com
googleadservices.com
advertising.com
adroll.com
spotx.tv
tremorhub.com
springserve.com
primis.tech
jwpsrv.com
gumgum.com
kargo.com
undertone.com
```

---

# 7. Push Ads / In-page Push / Popup / Popunder

## Formatos

- web push
- in-page push
- push ads
- pop-up
- pop-under
- tab-under
- new-tab advertising
- redirect
- interstitial
- notification ads

## Redes interesantes

- PropellerAds
- Adsterra
- AdMaven
- RichAds
- Evadav
- Clickadu
- PushGround
- HilltopAds
- Zeropark
- PopAds
- PopCash
- ExoClick
- TrafficJunky
- TrafficStars
- AdCash
- Adnium
- PushHouse
- iZooto
- Pushwoosh
- CleverPush

---

# 8. Clickbait

Clickbait no es un protocolo DNS. Es un tipo de contenido.

Debe tratarse mediante:

1. bloquear redes de recomendación;
2. bloquear redirects;
3. bloquear afiliación sospechosa;
4. bloquear malvertising;
5. utilizar uBlock/EasyList para el propio contenido HTML.

## Señales típicas

- "No te creerás..."
- "Los médicos están sorprendidos..."
- "Haz esto antes de dormir..."
- "Una cucharada..."
- "El secreto..."
- "Lo que nunca te contaron..."
- falsos premios
- falsos avisos de seguridad
- productos milagro
- testimonios falsos

No tiene sentido crear una regex DNS sobre el texto.

---

# 9. Trackers y Ad-Tech

## Categorías

- analytics
- telemetry
- tracking
- audience measurement
- attribution
- conversion tracking
- remarketing
- retargeting
- fingerprinting
- cross-site tracking
- ad verification
- viewability
- fraud detection

## Redes y servicios importantes

- DoubleVerify
- IAS / Integral Ad Science
- Moat
- Quantcast
- Nielsen
- Comscore
- Oracle Advertising
- Adobe Advertising
- Criteo
- LiveRamp
- TapAd
- Lotame
- BlueKai
- Eyeota
- Neustar
- Acxiom
- The Trade Desk
- ScorecardResearch
- Quantserve

Ejemplos conocidos:

```text
doubleverify.com
adsafeprotected.com
moatads.com
quantserve.com
scorecardresearch.com
imrworldwide.com
bluekai.com
rlcdn.com
crwdcntrl.net
demdex.net
everesttech.net
eyeota.net
tapad.com
```

---

# 10. CNAME Cloaking

## Problema

Una página puede utilizar un dominio aparentemente propio:

```text
metrics.example.com
```

y utilizar DNS para hacer que dicho nombre sea un alias CNAME hacia infraestructura de tracking.

Por tanto:

```text
example.com
   │
   └── metrics.example.com
          │
          └── CNAME → proveedor de tracking
```

puede ser más difícil de detectar mediante simples listas de dominios.

## Mitigación

Pi-hole debe configurarse con:

- CNAME inspection
- listas que contemplen tracking first-party
- análisis del Query Log
- allowlist selectiva

Esto es particularmente importante para redes que ocultan parte del tracking como subdominios first-party.

---

# 11. First-Party Tracking

Una parte de la publicidad y tracking moderno intenta parecer parte de la web que visitas.

Ejemplo:

```text
www.example.com
analytics.example.com
metrics.example.com
stats.example.com
cdn.example.com
```

No todos son malos.

No conviene bloquear por nombre.

Hay que identificar los endpoints reales y actuar con:

- CNAME inspection
- reglas específicas
- uBlock
- listas de privacidad

---

# 12. Malware / Phishing / Scam

Una instalación potente de Pi-hole no debería limitarse a anuncios.

## Categorías

- malware
- phishing
- ransomware
- scam
- fraude
- fake shops
- fake antivirus
- scareware
- cryptojacking
- malicious redirects
- malicious downloads
- command and control

## Fuentes

Una buena arquitectura puede utilizar listas mantenidas para:

- malware
- phishing
- scam
- ransomware
- cryptojacking
- fraud

Blocklist Project y HaGeZi mantienen categorías específicas para estas amenazas.

---

# 13. Redirects

Añadir una categoría dedicada:

```text
REDIRECT
CLICK_TRACKING
TRAFFIC_REDIRECT
AFFILIATE_REDIRECT
```

Flujo habitual:

```text
web
 │
 ▼
redirect
 │
 ▼
tracking
 │
 ▼
ad network
 │
 ▼
landing page
```

Bloquear solamente la landing final no siempre sirve.

---

# 14. Affiliate / Commerce Tracking

Categorías:

- affiliate tracking
- commerce recommendations
- shopping tracking
- coupon redirects
- referral links

Familias que pueden aparecer:

- Skimlinks
- Sovrn
- VigLink
- RewardStyle / LTK
- Infolinks
- Kontera
- BuySellAds
- Carbon Ads
- Freestar
- Snigel
- Playwire
- Publift
- MonetizeMore

Importante: algunos son principalmente monetización legítima.

Este bloque debe ser **opcional**.

---

# 15. Dynamic DNS abusivo

No bloquear todos los proveedores de DDNS.

Crear una categoría:

```text
MALICIOUS_DYNAMIC_DNS
ABUSED_DDNS
```

porque DDNS también se usa legítimamente para:

- servidores domésticos
- NAS
- cámaras
- Home Assistant
- VPN
- servicios remotos

---

# 16. URL Shorteners

Ejemplos:

- bit.ly
- tinyurl
- otros acortadores

Son ambiguos.

Pueden servir para:

- enlaces legítimos
- marketing
- tracking
- phishing
- redirects

No deben bloquearse por defecto en una red doméstica.

Crear:

```text
OPTIONAL_URL_SHORTENERS
```

---

# 17. DNS Bypass

Este apartado es crítico.

Puedes tener un Pi-hole perfecto y que un dispositivo ignore completamente tu DNS.

## Vectores

- DNS externo
- Google DNS
- Cloudflare DNS
- Quad9
- DNS ISP
- DNS over HTTPS
- DNS over TLS
- DNS over QUIC
- VPN
- proxy
- Tor
- aplicaciones con resolvers propios

## Ejemplos de DNS públicos

```text
8.8.8.8
8.8.4.4

1.1.1.1
1.0.0.1

9.9.9.9

208.67.222.222
208.67.220.220
```

No se resuelve solamente con Pi-hole.

Debe solucionarse principalmente en router/firewall.

---

# 18. DNS Over HTTPS

DoH utiliza HTTPS y suele viajar por:

```text
TCP/443
```

por lo que bloquear "todos los DNS por 443" rompería Internet.

La estrategia es:

- políticas específicas del router;
- bloqueo de resolvers DoH conocidos;
- navegador administrado cuando sea necesario;
- listas de proveedores DoH;
- control mediante firewall;
- permitir únicamente el resolver deseado.

---

# 19. DNS Over TLS

Habitualmente:

```text
TCP/853
UDP/853
```

Si la red debe obligar a utilizar Pi-hole:

```text
bloquear cliente → Internet:853
permitir cliente → Pi-hole:53
```

---

# 20. DNS over QUIC

DNS over QUIC puede utilizar:

```text
UDP/443
```

Este punto debe contemplarse especialmente en redes modernas.

Bloquear indiscriminadamente UDP/443 puede romper aplicaciones legítimas.

Lo correcto es:

- identificar resolvers;
- aplicar reglas específicas;
- controlar clientes si es una red administrada.

---

# 21. IPv4 + IPv6

No basta con configurar IPv4.

Comprobar:

```text
DHCPv4 → Pi-hole
DNSv4 → Pi-hole

DHCPv6 → Pi-hole
RA → Pi-hole
DNSv6 → Pi-hole
```

y revisar que el router no anuncie DNS alternativos mediante IPv6.

---

# 22. Firewall recomendado

Modelo conceptual:

```text
LAN clients
   │
   ├── TCP/UDP 53 → Pi-hole       ALLOW
   │
   ├── Internet:53               DENY
   ├── Internet:853              DENY
   │
   └── DNS/DoH/DoQ alternativos  CONTROLAR
```

El Pi-hole es el DNS autorizado.

El router/firewall es quien impide que el cliente lo salte.

---

# 23. Gravity Lists

No conviene cargar 10 listas gigantes sin estudiar solapamientos.

Más listas no implica automáticamente más protección.

Puede aumentar:

- duplicación
- falsos positivos
- consumo
- dificultad de diagnóstico
- conflictos

## Fuentes importantes

### HaGeZi

Mantiene múltiples categorías, entre ellas:

- Multi
- Pro
- Pop-Up Ads
- TIF
- Threat Intelligence
- URL Shorteners
- Dynamic DNS
- categorías específicas de privacidad y bypass

### Blocklist Project

Mantiene listas de:

- Ads
- Tracking
- Malware
- Phishing
- Fraud
- Scam
- Ransomware
- Redirect
- Cryptojacking

### StevenBlack

Lista unificada histórica y muy utilizada, con diferentes variantes.

### 1Hosts

Dispone de variantes con distinta agresividad.

---

# 24. Estrategia de listas recomendada

## Perfil doméstico equilibrado

```text
1 lista principal de ads/tracking
1 lista de amenazas
1 lista de popup
regex personalizadas
```

## Perfil avanzado

```text
HaGeZi principal
+
HaGeZi TIF
+
HaGeZi Pop-Up Ads
+
regex propias
+
allowlist controlada
```

## Perfil muy agresivo

```text
HaGeZi PRO/ULTIMATE según necesidades
+
Threat Intelligence
+
Popups
+
reglas propias
+
bloqueo de bypass DNS
+
uBlock Origin
```

No mezclar indiscriminadamente varias listas enormes si no se ha comprobado su solapamiento.

---

# 25. Pi-hole + uBlock Origin

Esta es probablemente la combinación más potente para un usuario doméstico.

## Pi-hole

Bloquea por DNS:

- dominios
- infraestructura
- tracking
- ads
- malware
- phishing
- ad-tech
- popups
- redirects

## uBlock Origin

Bloquea:

- URL concretas
- scripts
- DOM
- CSS
- elementos
- anuncios first-party
- elementos patrocinados
- anti-adblock
- vídeo
- contenido HTML

---

# 26. EasyList / EasyPrivacy

EasyList es especialmente útil para el filtrado en navegador.

Incluye reglas destinadas a:

- publicidad
- popups
- popunders
- vídeo
- scripts publicitarios
- elementos de página
- filtros cosméticos

EasyPrivacy está orientada al tracking y privacidad.

Esto complementa a Pi-hole en lugar de competir con él.

---

# 27. Limite importante: anuncios servidos desde el mismo dominio

Ejemplo:

```text
example.com
```

sirve:

```text
example.com/content
example.com/ad
example.com/script
example.com/image
```

Pi-hole no puede decir:

```text
bloquea /ad
```

porque DNS no trabaja con rutas URL.

Por tanto:

```text
Pi-hole ≠ bloqueador HTTP
```

La capa de navegador es imprescindible para casos así.

---

# 28. Video ads

Categoría propia:

- pre-roll
- mid-roll
- post-roll
- outstream
- overlays
- video recommendation

El filtrado completo de vídeo requiere reglas específicas de navegador.

---

# 29. Anti-Adblock

Un sitio puede detectar que existe un bloqueador.

Las estrategias pueden incluir:

- scripts anti-adblock
- detección de elementos publicitarios
- comprobación de endpoints
- bloqueos condicionales
- páginas de recuperación

Pi-hole puede bloquear algunos dominios asociados, pero no resolver todos los mecanismos.

uBlock es mucho más apropiado para esta capa.

---

# 30. Allowlist

Hay que preparar desde el principio una allowlist.

Categorías:

```text
CRITICAL_SERVICES
BANKING
AUTHENTICATION
MICROSOFT
GOOGLE
APPLE
AMAZON
CLOUD_SERVICES
STREAMING
SMART_HOME
HOME_ASSISTANT
NAS
WORK
```

La allowlist debe ser pequeña y justificada.

No conviene crear:

```text
*.google.com
*.microsoft.com
*.amazon.com
```

a ciegas.

---

# 31. Control de falsos positivos

Cuando una web deja de funcionar:

1. Abrir Query Log.
2. Identificar el dominio bloqueado.
3. Ver qué lista o regex lo ha bloqueado.
4. Confirmar que realmente es necesario.
5. Crear una excepción específica.

No desactivar todas las listas.

---

# 32. Observabilidad

Una instalación potente necesita poder diagnosticarse.

Comprobar periódicamente:

```text
Query Log
Top Blocked Domains
Clients
Lists
Regex Hits
CNAME-related blocks
```

La mejor fuente para descubrir huecos nuevos es observar qué aparece en el Query Log cuando navegas por webs problemáticas.

---

# 33. Pruebas que conviene realizar

## Publicidad nativa

Buscar páginas con:

- Taboola
- Outbrain
- MGID
- RevContent
- ZergNet

## Clickbait

Probar:

- prensa online
- revistas
- portales de salud
- entretenimiento
- páginas de bricolaje
- webs de recetas

## Popups

Probar sitios conocidos por:

- popups
- redirects
- nuevas pestañas

## Malvertising

No buscar malware real deliberadamente.

Utilizar:

- páginas de prueba
- dominios documentados
- herramientas de verificación

## DNS bypass

Comprobar desde clientes si pueden resolver directamente contra:

- 8.8.8.8
- 1.1.1.1
- 9.9.9.9

El objetivo es verificar que el firewall realmente fuerza Pi-hole.

---

# 34. Estructura recomendada para una V2 definitiva

La colección propia debería organizarse así:

```text
00_CORE
01_NATIVE_ADS
02_CONTENT_DISCOVERY
03_CLICKBAIT
04_AD_EXCHANGES
05_SSP
06_DSP
07_DISPLAY
08_VIDEO
09_TRACKING
10_ANALYTICS
11_FINGERPRINTING
12_AFFILIATE
13_PUSH
14_POPUP
15_POPUNDER
16_INTERSTITIAL
17_REDIRECT
18_MALVERTISING
19_MALWARE
20_PHISHING
21_SCAM
22_CRYPTOJACKING
23_CNAME
24_FIRST_PARTY_TRACKING
25_DYNAMIC_DNS
26_URL_SHORTENERS
27_DNS_BYPASS
28_OPTIONAL_AGGRESSIVE
```

---

# 35. Formatos que deben mantenerse separados

No mezclar en el mismo fichero:

```text
Pi-hole regex
hosts
domain lists
AdGuard syntax
uBlock syntax
dnsmasq rules
```

## Recomendación

```text
pihole_ads_native_v2.conf
pihole_threats_v2.conf
pihole_privacy_v2.conf
pihole_optional_v2.conf
allowlist_v2.conf
```

y, para navegador:

```text
ublock_rules.txt
easylist-compatible.txt
```

---

# 36. Qué NO hacer

## No utilizar regex genéricas

```regex
.*ad.*
.*ads.*
.*advert.*
.*content.*
.*click.*
.*cdn.*
```

Son demasiado peligrosas.

## No bloquear palabras

```regex
.*health.*
.*home.*
.*pain.*
.*weight.*
.*money.*
```

DNS no entiende el contexto.

## No bloquear todo un proveedor legítimo sin necesidad

Por ejemplo:

```text
amazon
google
microsoft
apple
cloudflare
```

pueden desempeñar muchas funciones diferentes.

## No meter todas las listas disponibles

Más tamaño no implica mejor resultado.

---

# 37. Prioridad recomendada

## Prioridad 1

- Taboola
- Outbrain
- Teads
- MGID
- MediaGo
- RevContent
- ZergNet
- Nativo
- Dianomi
- publicidad nativa relacionada

## Prioridad 2

- popups
- popunders
- push ads
- redirects
- malvertising

## Prioridad 3

- trackers
- analytics
- attribution
- fingerprinting

## Prioridad 4

- malware
- phishing
- scam
- ransomware
- cryptojacking

## Prioridad 5

- DNS bypass
- DoH
- DoT
- DoQ
- IPv6 bypass

## Prioridad 6

- filtros cosméticos y de navegador mediante uBlock

---

# 38. Arquitectura final recomendada para una red doméstica avanzada

```text
                         INTERNET
                             │
                             ▼
                    ┌─────────────────┐
                    │ Router / Firewall│
                    └────────┬────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
       Fuerza DNS                    Bloquea bypass
              │                     53 / 853 / etc.
              │
              ▼
        ┌────────────┐
        │   Pi-hole  │
        └──────┬─────┘
               │
      ┌────────┼─────────────┐
      │        │             │
   Gravity   Regex         CNAME
      │        │          inspection
      │        │             │
      └────────┼─────────────┘
               │
               ▼
             LAN
               │
       ┌───────┴─────────┐
       │                 │
       ▼                 ▼
    Navegador       IoT / Smart TV
       │
       ▼
 uBlock Origin
 EasyList
 EasyPrivacy
```

---

# 39. Configuración objetivo

Una instalación "a tope" pero razonable debería buscar:

### Publicidad

- [x] native ads
- [x] content discovery
- [x] clickbait networks
- [x] display
- [x] video
- [x] push
- [x] popup
- [x] popunder
- [x] interstitial
- [x] redirect

### Privacidad

- [x] tracking
- [x] analytics
- [x] attribution
- [x] fingerprinting
- [x] CNAME tracking
- [x] first-party tracking cuando sea identificable

### Seguridad

- [x] malware
- [x] phishing
- [x] scam
- [x] ransomware
- [x] cryptojacking
- [x] malicious redirects

### Infraestructura

- [x] IPv4
- [x] IPv6
- [x] CNAME inspection
- [x] DNS bypass
- [x] DoH/DoT/DoQ control
- [x] router/firewall enforcement

### Navegador

- [x] uBlock Origin
- [x] EasyList
- [x] EasyPrivacy
- [x] filtros cosméticos
- [x] anti-adblock

---

# 40. Fuentes recomendadas

## Pi-hole

Documentación oficial:

- https://docs.pi-hole.net/
- https://docs.pi-hole.net/regex/
- https://docs.pi-hole.net/regex/tutorial/
- https://docs.pi-hole.net/database/query-database/
- https://docs.pi-hole.net/ftldns/blockingmode/

## HaGeZi

- https://github.com/hagezi/dns-blocklists

Especialmente interesantes:

- Multi
- Pro
- TIF
- Pop-Up Ads
- Threat Intelligence
- URL Shorteners
- Dynamic DNS

## Blocklist Project

- https://github.com/blocklistproject/Lists

Categorías relevantes:

- Ads
- Tracking
- Malware
- Phishing
- Scam
- Fraud
- Redirect
- Ransomware
- Cryptojacking

## StevenBlack

- https://github.com/StevenBlack/hosts

## 1Hosts

- https://github.com/badmojr/addons_1Hosts

## EasyList

- https://github.com/easylist/easylist

## EasyPrivacy

- https://github.com/easylist/easyprivacy

---

# 41. Conclusión

La mejor instalación de Pi-hole no es la que tiene más regex.

Es la que combina:

```text
Pi-hole
+
gravity lists buenas
+
regex propias
+
CNAME inspection
+
DNS enforcement
+
IPv6 control
+
protección frente a bypass
+
uBlock Origin
+
EasyList
+
EasyPrivacy
```

El objetivo real debe ser una defensa por capas:

```text
DNS
↓
Firewall
↓
Pi-hole
↓
CNAME
↓
Browser filtering
↓
Cosmetic filtering
```

Para el objetivo concreto de eliminar **Taboola / Outbrain / MediaGo / MGID / clickbait de salud y hogar / widgets de contenido recomendado**, las categorías `01_NATIVE_ADS`, `02_CONTENT_DISCOVERY`, `03_CLICKBAIT`, `13_PUSH`, `14_POPUP`, `15_POPUNDER` y `17_REDIRECT` son especialmente importantes.

La segunda gran prioridad es impedir que los dispositivos **salten el Pi-hole**, porque un DNS perfecto pierde utilidad si el cliente puede consultar libremente otro resolver.

La tercera es aceptar la limitación del DNS: para eliminar completamente anuncios embebidos, vídeo, elementos HTML, CSS, scripts y ciertos mecanismos first-party, hace falta una capa de navegador como uBlock Origin.
