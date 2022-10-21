def build_xml_element(tag, content, **elements):
    xml_element = f'<{tag} '
    for element_key, element_value in elements.items():
        xml_element += element_key
        xml_element += "=\\\"" + element_value.strip() + "\\\""
    xml_element += "> " + content + f' </{tag}>'
    return xml_element


print(build_xml_element ("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))
