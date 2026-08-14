import paramiko
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

PI_IP = os.getenv("PI_IP", "192.168.0.23")
PI_USER = os.getenv("PI_USER", "jose")
PI_PASS = os.getenv("PI_PASS", "josejosejose1")

conf_path = os.path.join(os.path.dirname(__file__), "..", "doc_info", "pihole_ads_clickbait_native_2026.conf")
regex_list = []
if os.path.exists(conf_path):
    with open(conf_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                regex_list.append(line)

print(f"Total reglas Regex cargadas: {len(regex_list)}")

adlists = [
    'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
    'https://v.firebog.net/hosts/AdguardDNS.txt',
    'https://v.firebog.net/hosts/Admiral.txt',
    'https://v.firebog.net/hosts/Easylist.txt',
    'https://v.firebog.net/hosts/Easyprivacy.txt',
    'https://v.firebog.net/hosts/Prigent-Ads.txt',
    'https://v.firebog.net/hosts/static/w3kbl.txt',
    'https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt',
    'https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt',
    'https://v.firebog.net/hosts/Prigent-Crypto.txt',
    'https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts',
    'https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abb8648620e4b6/bad_lists/Mandiant_APT1_Report_Appendix_D.txt',
    'https://phishing.army/download/phishing_army_blocklist_extended.txt',
    'https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt',
    'https://v.firebog.net/hosts/RPiList-Malware.txt',
    'https://v.firebog.net/hosts/RPiList-Phishing.txt',
    'https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt',
    'https://raw.githubusercontent.com/AssoEchap/stalkerware-indicators/master/generated/hosts',
    'https://urlhaus.abuse.ch/downloads/hostfile/',
    'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/multi.txt',
    'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/popupads.txt',
    'https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/tif.txt',
    'https://blocklistproject.github.io/Lists/alt-version/malware-nl.txt',
    'https://blocklistproject.github.io/Lists/alt-version/phishing-nl.txt',
    'https://blocklistproject.github.io/Lists/alt-version/scam-nl.txt',
    'https://blocklistproject.github.io/Lists/alt-version/redirect-nl.txt'
]

py_script = f"""
import sqlite3

conn = sqlite3.connect('/etc/pihole/gravity.db')
c = conn.cursor()

c.execute("DELETE FROM domainlist WHERE domain LIKE '%googlesyndication%' AND type IN (1, 3);")
c.execute("DELETE FROM domainlist WHERE domain LIKE '%mediago%' AND type IN (1, 3);")

adlists = {adlists!r}
regex_rules = {regex_list!r}

for url in adlists:
    c.execute("INSERT OR IGNORE INTO adlist (address, enabled, comment) VALUES (?, 1, 'Master V2 Pack');", (url,))
    c.execute("SELECT id FROM adlist WHERE address = ?;", (url,))
    row = c.fetchone()
    if row:
        c.execute("INSERT OR IGNORE INTO adlist_by_group (adlist_id, group_id) VALUES (?, 0);", (row[0],))

for reg in regex_rules:
    c.execute("INSERT OR IGNORE INTO domainlist (domain, type, enabled, comment) VALUES (?, 2, 1, 'Master Regex V2');", (reg,))
    c.execute("SELECT id FROM domainlist WHERE domain = ? AND type = 2;", (reg,))
    row = c.fetchone()
    if row:
        c.execute("INSERT OR IGNORE INTO domainlist_by_group (domainlist_id, group_id) VALUES (?, 0);", (row[0],))

conn.commit()
conn.close()
print("Insercion SQL completada.")
"""

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(PI_IP, username=PI_USER, password=PI_PASS, timeout=10)

sftp = ssh.open_sftp()
with sftp.file('/tmp/inject_rules.py', 'w') as f:
    f.write(py_script)
sftp.close()

stdin, stdout, stderr = ssh.exec_command(f"echo {PI_PASS} | sudo -S python3 /tmp/inject_rules.py && sudo pihole -g && sudo systemctl restart pihole-FTL")
print(stdout.read().decode('utf-8', errors='ignore'))
ssh.close()
print("¡Listas y reglas actualizadas con éxito!")
