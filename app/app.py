from flask import Flask, request, Response
import dns.resolver
import sys

app = Flask(__name__)

# DNS TXT rekord lekérdezése
def get_config_from_dns(domain):
    try:
        # Lekérjük a TXT rekordot az adott domainhez
        # "imap_server:m2.linux-szerver.hu,smtp_server:m2.linux-szerver.hu,imap_port:143,smtp_port:587,imap_ssl:0,smtp_ssl:0,imap_tls:1,smtp_tls:1"
        result = dns.resolver.resolve(f"mcfg.{domain}", "TXT")
        for txt in result:
            config_data = txt.to_text().strip('"')
            config_dict = {}
            for param in config_data.split(","):
                key, value = param.split(":")
                config_dict[key] = value
            print (config_dict, flush=True)
            return config_dict
    except Exception as e:
        return ''

# Autodiscover útvonal (Outlook számára)
@app.route('/autodiscover/autodiscover.xml', methods=['POST'])
def autodiscover():
    domain = request.form.get("emailaddress").split("@")[-1]
    config = get_config_from_dns(domain)
    if not config:
        return Response(status=404)
    
    xml_response = f"""<?xml version="1.0" encoding="UTF-8"?>
    <Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/responseschema/2006">
        <Response">
            <Account>
                <AccountType>email</AccountType>
                <Action>settings</Action>
                <Protocol>
                    <Type>IMAP</Type>
                    <Server>{config["imap_server"]}</Server>
                    <Port>{config["imap_port"]}</Port>
                    {'<SSL>true</SSL>' if config["imap_ssl"] == '1' else '<TLS>true</TLS>' if config["imap_tls"] == '1' else '' }
                    <AuthRequired>true</AuthRequired>
                </Protocol>
                <Protocol>
                    <Type>SMTP</Type>
                    <Server>{config["smtp_server"]}</Server>
                    <Port>{config["smtp_port"]}</Port>
                    {'<SSL>true</SSL>' if config["smtp_ssl"] == '1' else '<TLS>true</TLS>' if config["smtp_tls"] == '1' else '' }
                    <AuthRequired>true</AuthRequired>
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
                {'<socketType>SSL</socketType>' if config["imap_ssl"] == '1' else '<socketType>STARTTLS</socketType' if config["imap_tls"] == '1' else '' }
                <authentication>password-cleartext</authentication>
            </incomingServer>
            <outgoingServer type="smtp">
                <hostname>{config["smtp_server"]}</hostname>
                <port>{config["smtp_port"]}</port>
                {'<socketType>SSL</socketType>' if config["smtp_ssl"] == '1' else '<socketType>STARTTLS</socketType' if config["smtp_tls"] == '1' else '' }
                <authentication>password-cleartext</authentication>
                <username>%EMAILADDRESS%</username>
            </outgoingServer>
        </emailProvider>
    </clientConfig>"""
    return Response(xml_response, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0" )
