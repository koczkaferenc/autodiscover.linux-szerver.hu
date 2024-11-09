from flask import Flask, request, Response
import dns.resolver
import sys

app = Flask(__name__)

# DNS TXT rekord lekérdezése
def get_config_from_dns(domain):
    try:
        # Lekérjük a TXT rekordot az adott domainhez
        result = dns.resolver.resolve(f"mcfg.{domain}", "TXT")
        # Kivesszük az értékeket a TXT rekordból
        for txt in result:
            config_data = txt.to_text().strip('"')
            config_dict = {}
            for param in config_data.split(","):
                key, value = param.split(":")
                config_dict[key] = value
            return config_dict
    except Exception as e:
        print(f"Hiba a DNS lekérdezésnél: {e}")
        return None

# Autodiscover útvonal (Outlook számára)
@app.route('/autodiscover/autodiscover.xml', methods=['POST'])
def autodiscover():
    domain = request.form.get("emailaddress").split("@")[-1]
    config = get_config_from_dns(domain)
    if not config:
        return Response(status=404)
    
    xml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
    <Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/responseschema/2006">
        <Response xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a">
            <Account>
                <AccountType>email</AccountType>
                <Action>settings</Action>
                <Protocol>
                    <Type>IMAP</Type>
                    <Server>{config["imap_server"]}</Server>
                    <Port>{config["imap_port"]}</Port>
                    {'<imapSSL>true</imapSSL>' if config["imap_ssl"] == 1}
                    {'<imapSSL>false</imapSSL>' if config["imap_ssl"] == 0}
                    {'<imapSTARTTLS>true</imapSTARTTLS>' if config["imap_tls"] == 1}
                    {'<imapSTARTTLS>false</imapSTARTTLS>' if config["imap_tls"] == 0}

                </Protocol>
                <Protocol>
                    <Type>SMTP</Type>
                    <Server>{config["smtp_server"]}</Server>
                    <Port>{config["smtp_port"]}</Port>
                    <SSL>{'true' if config["smtp_ssl"] == 1 else "false"}</SSL>
                </Protocol>
            </Account>
        </Response>
    </Autodiscover>"""
    return Response(xml_response, mimetype='application/xml')

# Autoconfig útvonal (Thunderbird számára)
@app.route('/mail/config-v1.1.xml', methods=['GET'])
def autoconfig():
    # Domain kivonása a GET kérésből
    domain = ".".join(request.host.split('.')[1:])
    print (request.args, flush=True)
    print (domain, flush=True)
    if not domain:
        return Response("Domain not provided", status=400)
    
    config = get_config_from_dns(domain)
    if not config:
        return Response("Configuration not found for domain", status=404)
    
    xml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
    <clientConfig version="1.1">
        <emailProvider id="{domain}">
            <domain>{domain}</domain>
            <incomingServer type="imap">
                <hostname>{config["imap_server"]}</hostname>
                <port>{config["imap_port"]}</port>
                <socketType>{"SSL" if config["imap_ssl"] == "1" else "STARTTLS"}</socketType>
                <authentication>password-cleartext</authentication>
            </incomingServer>
            <outgoingServer type="smtp">
                <hostname>{config["smtp_server"]}</hostname>
                <port>{config["smtp_port"]}</port>
                <socketType>{"SSL" if config["smtp_ssl"] == "SSL" else "STARTTLS"}</socketType>
                <authentication>password-cleartext</authentication>
            </outgoingServer>
        </emailProvider>
    </clientConfig>"""
    return Response(xml_response, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0" )
