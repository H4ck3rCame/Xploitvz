# -*- coding: utf-8 -*-
import requests,sys

codi = str(sys.argv[1])

print "\n - Created by H4ck3rCame -\n"
print " If not you, who? If not now, when?"
print "  _   _            _      ____             _    _ "
print " | | | | __ _  ___| | __ | __ )  __ _  ___| | _| |"
print " | |_| |/ _` |/ __| |/ / |  _ \ / _` |/ __| |/ / |"
print " |  _  | (_| | (__|   <  | |_) | (_| | (__|   <|_|"
print " |_| |_|\__,_|\___|_|\_\ |____/ \__,_|\___|_|\_(_)"

print "\n[*] Searching credentials in XPLOITV & XPLOITZ with the identifier %s..." % (codi)

def xploitv(codi):
	r = requests.get("http://server2.lincehost.com/~neek/exe/xploitv.php?bb="+codi)
	content = r.text.encode("UTF-8")[6:-3]
	content = content.replace("\\","")
	content = content.replace("u00f1","ñ")
	content = content.replace("u00f3","ó")
	f = open(codi+"_xploitv.html", "a")
	f.write("<title>"+codi+"_xploitv.html"+"</title>")
	f.write("<meta charset='UTF-8'>")
	f.write(content)
	f.close()

def xploitz(codi):
	payload = {'identifier': codi}
	r = requests.post("http://www.xploitz.net/search.php", data=payload)
	content = r.text.encode("UTF-8")
	content = content.replace('src="flags/','src="http://www.xploitz.net/flags/')
	content = content.replace('src="favicon/','src="http://www.xploitz.net/favicon/')
	content = content.replace('src="/cdn-cgi','src="http://www.xploitz.net/cdn-cgi')
	f = open(codi+"_xploitz.html", "a")
	f.write("<title>"+codi+"_xploitz.html"+"</title>")
	f.write("<meta charset='UTF-8'>")
	f.write(content)
	f.close()

print "[*] Generating HTML files..."

#xploitv(codi)
xploitz(codi)

print "[*] Finished!"