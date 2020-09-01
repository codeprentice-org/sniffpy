import sniffpy
import requests

r = requests.get("https://httpbin.org/image/jpeg")
mime_type = sniffpy.sniff(r.content) #returns a MIMEType object

print(mime_type.type) #prints "image"
print(mime_type.subtype) #prints "jpeg"

print(mime_type) #prints "image/jpeg"
