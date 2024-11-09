#!/usr/bin/python3

TTL=300
AUTODISCOVER_SERVER="pm.linux-szerver.hu"
AUTODISCOVER_PORT=80
MX="pm.linux-szerver.hu"
SMTP_IP="87.229.94.230"
DOMAINKEY="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDSTM1izh8o/P4PeLgw7JUSyFk7o9lpvuZLl3zriafqFsUXtZt+JUGT6gisabfzpcwRaG2qSACcyx4n++ujA3/A0sPr+9vqZkcJMTcoii0nRpz5i0Y/waImQIC2kccMsvB7KmF6ytZ7Nb8rf5Tin3dHeCshEzMXWkSbMguejO7wBwIDAQAB"
SMTP_SERVER="m2.linux-szerver.hu"
SMTP_PORT=587
IMAP_SERVER="m2.linux-szerver.hu"
SMTP_SSL=0
SMTP_TLS=1
IMAP_PORT=143
IMAPS_PORT=143
IMAP_SSL=0
IMAP_TLS=1

print (f"""
$TTL {TTL}
@                  IN MX 10 {MX}.
@                  IN TXT "v=spf1 a mx ip4:{SMTP_IP} -all"
@                  IN CAA 0 issue "letsencrypt.org"
default._domainkey IN TXT "v=DKIM1; k=rsa; p={DOMAINKEY}"
_dmarc             IN TXT "v=DMARC1; p=none"
autoconfig         IN CNAME {AUTODISCOVER_SERVER}.
autodiscover       IN CNAME {AUTODISCOVER_SERVER}.

_autodiscover._tcp IN SRV 0 100 {AUTODISCOVER_PORT} {AUTODISCOVER_SERVER}.
_submission._tcp   IN SRV 0 1 {SMTP_PORT} {SMTP_SERVER}.
_imaps._tcp        IN SRV 0 1 {IMAPS_PORT} {IMAP_SERVER}.
_imap._tcp         IN SRV 0 1 {IMAPS_PORT} {IMAP_SERVER}.

mcfg               IN TXT "imap_server:{IMAP_SERVER},imap_port:{IMAPS_PORT},imap_ssl:{IMAP_SSL},imap_tls:{IMAP_SSL},smtp_server:{SMTP_SERVER},smtp_port:{SMTP_PORT},smtp_ssl:{SMTP_SSL},tls:{SMTP_TLS}"
""")

