# autodiscover.linux-szerver.hu
Autodiscover mailbox beállításhoz

mcfg IN TXT "imap_server:m2.linux-szerver.hu,smtp_server:m2.linux-szerver.hu,imap_port:143,smtp_port:587,imap_ssl:0,smtp_ssl:0,imap_tls:1,smtp_tls:1"

<Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/responseschema/2006">
  <Response>
    <Account>
      <AccountType>email</AccountType>
      <Action>settings</Action>
      <Protocol>
        <Type>IMAP</Type>
        <Server>imap.bitbazar.hu</Server>
        <Port>993</Port>
        <SSL>true</SSL>
        <AuthRequired>true</AuthRequired>
      </Protocol>
      <Protocol>
        <Type>SMTP</Type>
        <Server>smtp.bitbazar.hu</Server>
        <Port>465</Port>
        <SSL>true</SSL>
        <AuthRequired>true</AuthRequired>
      </Protocol>
    </Account>
  </Response>
</Autodiscover>

Starttls esetén:

<Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/responseschema/2006">
  <Response>
    <Account>
      <AccountType>email</AccountType>
      <Action>settings</Action>
      <Protocol>
        <Type>IMAP</Type>
        <Server>imap.bitbazar.hu</Server>
        <Port>143</Port>
        <SSL>false</SSL>
        <AuthRequired>true</AuthRequired>
        <TLS>true</TLS>
      </Protocol>
      <Protocol>
        <Type>SMTP</Type>
        <Server>smtp.bitbazar.hu</Server>
        <Port>587</Port>
        <SSL>false</SSL>
        <AuthRequired>true</AuthRequired>
        <TLS>true</TLS>
      </Protocol>
    </Account>
  </Response>
</Autodiscover>

----

Thunderbird

<clientConfig version="1.1">
    <emailProvider id="example.com">
        <domain>example.com</domain>
        <incomingServer type="imap">
            <hostname>imap.example.com</hostname>
            <port>993</port>
            <socketType>SSL</socketType>
            <authentication>password-cleartext</authentication>
            <username>%EMAILADDRESS%</username>
        </incomingServer>
        <outgoingServer type="smtp">
            <hostname>smtp.example.com</hostname>
            <port>465</port>
            <socketType>SSL</socketType>
            <authentication>password-cleartext</authentication>
            <username>%EMAILADDRESS%</username>
        </outgoingServer>
    </emailProvider>
</clientConfig>


<clientConfig version="1.1">
    <emailProvider id="example.com">
        <domain>example.com</domain>
        <incomingServer type="imap">
            <hostname>imap.example.com</hostname>
            <port>143</port>
            <socketType>STARTTLS</socketType>
            <authentication>password-cleartext</authentication>
            <username>%EMAILADDRESS%</username>
        </incomingServer>
        <outgoingServer type="smtp">
            <hostname>smtp.example.com</hostname>
            <port>587</port>
            <socketType>STARTTLS</socketType>
            <authentication>password-cleartext</authentication>
            <username>%EMAILADDRESS%</username>
        </outgoingServer>
    </emailProvider>
</clientConfig>
