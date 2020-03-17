import re

with open("command0.txt", "r") as f:
    xml_call = f.read()

xml_call = xml_call.split(" ")
group2_list = []
xml_call[0] = xml_call[0].lstrip('x')  # all of the cisco apis being with an x so get rid of that shit

# go thru each list element and if it has non-word characters, put it in its own list bc these are "group2"
# parameters.  When the

for _ in xml_call[::-1]:
    group2_node = re.search('\W+', _)
    if group2_node:
        xml_call.pop()
        cleaned_node = re.sub('\W+', '', _)
        if cleaned_node not in group2_list:
            group2_list.append(cleaned_node)

group2_openclosetags = []
group1_opentag = []
group1_closetag = []

for word in xml_call:
    group1_opentag.append(f'<{word}>')

for word in xml_call[::-1]:
    group1_closetag.append(f"</{word}>")

for word in group2_list:
    group2_openclosetags.append(f"<{word}></{word}>")

new_xml_call = group1_opentag + group2_openclosetags + group1_closetag
new_xml_call = "".join(new_xml_call)

with open("api_result.txt", "w") as f:
    f.write(new_xml_call)

