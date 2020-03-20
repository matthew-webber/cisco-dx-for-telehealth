import re

#todo fix the fact that if the telnet string in command0 has a newline, it will doubledouble the tag name

with open("command0.txt", "r") as f:
    xml_call = f.read()


def xmlify_telnet_string(telnet_string):

    telnet_string = telnet_string.split(" ")
    group2_list = []
    telnet_string[0] = telnet_string[0].lstrip('x')  # all of the cisco apis being with an x so get rid of that shit

    # go thru each list element and if it has non-word characters, put it in its own list bc these are "group2"
    # parameters.  When the

    for _ in telnet_string[::-1]:
        group2_node = re.search('\W+', _)
        if group2_node:
            telnet_string.pop()
            cleaned_node = re.sub('\W+', '', _)
            if cleaned_node not in group2_list:
                group2_list.append(cleaned_node)

    group2_openclosetags = []
    group1_opentag = []
    group1_closetag = []

    for word in telnet_string:
        group1_opentag.append(f'<{word}>')

    for word in telnet_string[::-1]:
        group1_closetag.append(f"</{word}>")

    for word in group2_list:
        group2_openclosetags.append(f"<{word}></{word}>")

    new_xml_call = group1_opentag + group2_openclosetags + group1_closetag
    new_xml_call = "".join(new_xml_call)

    return new_xml_call


new_xml_call = xmlify_telnet_string(xml_call)

with open("api_result.txt", "w") as f:
    f.write(new_xml_call)

