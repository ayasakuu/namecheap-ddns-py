# namecheap-ddns-py
Namecheap DDNS refresh client written in Python 3.

Add a cronjob that looks something like this and never worry about DDNS again.
<code>*/5 * * * * HOST DOMAIN DDNS-KEY</code>
<code>*/5 * * * * @ example.com abcdefghijk</code>

I advise not to refresh any more frequently than every 5 minutes.