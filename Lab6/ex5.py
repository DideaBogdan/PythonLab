import re


def find_in_XML(xml, attributes):
    for item in attributes.items():
        reg = '<[a-zA-Z]+\s*'
        reg += item[0] + '\s*=\s*("|\')' + item[1] + '("|\')\s*'
        r = re.compile(reg, re.IGNORECASE)
        res = r.search(xml)
        if res:
            print(xml)


attrs = {"class": "url", "name": "url-form", "data-id": "item"}


with open('ex4_xml.xml', 'r') as f:
    while True:
        data = f.readline()
        find_in_XML(data, attrs)
        if data == '':
            break

