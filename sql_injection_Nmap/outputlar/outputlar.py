import os
os.system("nmap -p 80 -script http-sitemap-generator -script http-php-version -script http-sql-injection -script ssl-ccs-injection -script http-csrf testphp.vulnweb.com https://nmap.org/nsedoc/scripts/http-xssed.html -oX sonuclar.xml")
