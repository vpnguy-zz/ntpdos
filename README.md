ntpdos<br />
Denial of service using NTP servers to amplify attacks <br />

Disclaimer: <strong> It appears someone is using an attack vector like this to DDOS cloudflare. I can not stress enough I have no involvement or participation in any such actions. This script is provided as is and its up to the end user to make mature and legal decisions about its usage. </strong>

Usage:<br />
<b>Please consult ntpdos.py -h</b>
<br />

Example:<br />
<b>ntpdos.py "1.2.3.4" "serverlist.txt" "10"</b>  -  Will attempt to spoof packets to 1.2.3.4 using NTP server list from serverlist.txt by creating 10 threads of senders
<br />
<br />
