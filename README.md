# autodiscover.linux-szerver.hu
Autodiscover mailbox beállításhoz

mcfg IN TXT "imap_server:imap.group1-mail.hu,smtp_server:smtp.group1-mail.hu,imap_port:143,smtp_port:587,imap_ssl:1,smtp_ssl:1"

<autodiscover>
    <emailProvider>
        <domain>bitbazar.hu</domain>
        <imapServer>imap.bitbazar.hu</imapServer>
        <imapPort>993</imapPort>
        <imapSSL>true</imapSSL>
        <smtpServer>smtp.bitbazar.hu</smtpServer>
        <smtpPort>465</smtpPort>
        <smtpSSL>true</smtpSSL>
    </emailProvider>
</autodiscover>

<autodiscover>
    <emailProvider>
        <domain>bitbazar.hu</domain>
        <imapServer>imap.bitbazar.hu</imapServer>
        <imapPort>143</imapPort>
        <imapSSL>false</imapSSL>
        <imapSTARTTLS>true</imapSTARTTLS>
        <smtpServer>smtp.bitbazar.hu</smtpServer>
        <smtpPort>587</smtpPort>
        <smtpSSL>false</smtpSSL>
        <smtpSTARTTLS>true</smtpSTARTTLS>
    </emailProvider>
</autodiscover>

----


<autoconfig xmlns="http://schemas.microsoft.com/office/mail/configuration">
    <emailProvider>
        <domain>bitbazar.hu</domain>
        <imapServer>imap.bitbazar.hu</imapServer>
        <imapPort>993</imapPort>
        <imapSSL>true</imapSSL>  <!-- SSL beállítás -->
        <smtpServer>smtp.bitbazar.hu</smtpServer>
        <smtpPort>465</smtpPort>
        <smtpSSL>true</smtpSSL>  <!-- SSL beállítás -->
    </emailProvider>
</autoconfig>

<autoconfig xmlns="http://schemas.microsoft.com/office/mail/configuration">
    <emailProvider>
        <domain>bitbazar.hu</domain>
        <imapServer>imap.bitbazar.hu</imapServer>
        <imapPort>143</imapPort>
        <imapSSL>false</imapSSL>  <!-- Nincs SSL, de a STARTTLS aktiválható -->
        <imapSTARTTLS>true</imapSTARTTLS>  <!-- STARTTLS beállítás -->
        <smtpServer>smtp.bitbazar.hu</smtpServer>
        <smtpPort>587</smtpPort>
        <smtpSSL>false</smtpSSL>  <!-- Nincs SSL, de a STARTTLS aktiválható -->
        <smtpSTARTTLS>true</smtpSTARTTLS>  <!-- STARTTLS beállítás -->
    </emailProvider>
</autoconfig>