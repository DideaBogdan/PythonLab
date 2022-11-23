import re



def find_in_XML(xml, attributes):
    for item in attributes.items():
        r = re.compile(f"<\w+\s+{item[0]}=\s+(\'|\"){item[1]}>", re.IGNORECASE)
        res = r.findall(xml)
        print(res)
    print(attributes)
with open('ex4_xml.xml', 'r') as f:
    data = f.read()
attrs = {"ZONE": "4", "light": "shade"}
find_in_XML(data, attrs)
