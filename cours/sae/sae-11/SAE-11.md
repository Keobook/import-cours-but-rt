# SAE 11: Initiation à l'hygiène informatique et à la Cyberscurité

1. Présentation individuelle (17/11): Browser Hijacker (180s: 3min) (9/11)
2. En groupe (3 pers.): petite vidéo (Moi, Ben Kadhi Sirine, Toulliou Mattéo) (soutenance: 18/11) (9/11) (3min)
3. Indiquer comment on a fait toutes nos recherches -> aide au portfolio

## 1/ Browser Hijacking in 180 s (3 min.), audio file expected

### What's Browser Hijacking?

Browser Hijacking is a term used to class under one banner different types of attacks
on the browser client of a person/organisation

It compromises of :

- changing content into the browser
- modifying user-behaviors
- intercept information such as HTTP sessions, SSL client certificates, cookies (the famous ones)
- pivoting web traffic in order to access intranet of an entreprise/organisation

Here are different known usage of this type of attacks:

- Agent Tesla: A Trojan spyware written to work with the .NET framework (known as active since 2014)
- Carberp: A credential stealing malware which stole credentials and informations through a SSL session (known as active since 2009, source-code leaked in 2013)
- Chaes: A multistage information stealer developed in different prog. languages and collects credentials, payment information and financial ones. (known as active since 2020 with a deliberate zone of action in Latin America)
- Cobalt Strike: A commercial, full-featured, remote acces tool which "simulates" targeted attacks and "emulates" the post-exploitation actions of "advanced actors".
It's a fully featured software used to simulate malicious attacks and covers the capabilities of other tools such as Metasploit and Mimikatz, within the full range of ATT&CK attacks.
Overall, it can perform browser pivoting and inject into a user's browser to inherit cookies, authenticated HTTP sessions, and client SSL certificates.
- Dridex: A banking Trojan malware stealing credentials, certificates, cookies using web injects. (known as active since 2014)

The mitigations possible:

- Restricting user permissions and addressing Privilege Escalation and Bypass User Account Control opportunities can limit the exposure.
- Closing all browser sessions regularly and when they are no longer needed.

The Detection possible:

- The Logon Session: Authentication logs can be used to audit logins to specific web applications, but determining malicious logins versus benign logins may be difficult if activity matches typical user behavior.
- Process Access + Process Modification: This may be a difficult technique to detect because adversary traffic may be masked by normal user traffic. Monitor for Process Injection against browser applications.
