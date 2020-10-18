# Sniffpy

Sniffpy is a python implementation of [MIME Sniffing Standard](https://mimesniff.spec.whatwg.org/)
MIME sniffing describes algorithms that attempt to discern the correct MIME type of some given
data. The MIME type of a file or byte stream describes its format. For example, the MIME type of an image could be
`image/jpeg` or `image/png` depending on its exact format. MIME types consist of:

* the `type` which describesthe broad category of the data
* the `subtype` which describes the exact kind of data
* an optional `parameter` which gives further information about the data

The exact specification of MIME types can be found [here](https://tools.ietf.org/html/rfc6838)

## Example

The following is an example on how to use sniffpy to guess the MIME type of an HTTP response using requests

```
import requests

r = requests.get("https://httpbin.org/image/jpeg")
mime_type = sniffpy.sniff(r.content) #returns a MIMEType object

print(mime_type.type) #prints "image"
print(mime_type.subtype) #prints "jpeg"

print(mime_type) #prints "image/jpeg"
```

Documentation on how to use the package and how to contribute can be found on [here](https://sniffpy.readthedocs.io/en/latest/)
