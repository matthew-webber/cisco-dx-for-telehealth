import xml.etree.ElementTree as ET
from lxml import etree

# def get_xml_value(target, xml):
#     return [node for node in xml.iter(target)]
#
#
# def get_nested_xml(xml, node_path):
#     """
#     provided with an xml root and up to two-node length "Node/Path", returns the "Path" portion
#     :param xml: XML root
#     :param node_path: Target/Parent node path string
#     :return: list of matching XML nodes
#     """
#     node_path = node_path.split('/')
#     if len(node_path) > 2:
#         raise ValueError(f"Length of nodepath '{node_path}' >2 ")  # can only handle parent/child path length
#
#     if len(node_path) == 1:
#         # if multiple matches for parent node, look for child node in both and return list of parent nodes
#         # containing child node
#         node_matches = [(x := get_xml_value(node_path[0], node))[0] for node in xml
#                         if (x := get_xml_value(node_path[0], node))]
#
#         # # if only one node match, return it outside list, otherwise return all matches
#         # if len(node_matches) == 1:
#         #     return node_matches[0]
#
#         return node_matches
#
#     return get_nested_xml(get_xml_value(node_path[0], xml), *node_path[1:])

def get_xml_value(target, xml):
    return [node for node in xml.iter(target)]


def get_nested_xml(xml, node_path):
    """
    provided with an xml root and up to two-node length "Node/Path", returns the "Path" portion
    :param xml: XML root
    :param node_path: Target/Parent node path string
    :return: list of matching XML nodes
    """
    node_path = node_path.split('/')
    if len(node_path) > 2:
        raise ValueError(f"Length of nodepath '{node_path}' >2 ")  # can only handle parent/child path length

    if len(node_path) == 1:
        # if multiple matches for parent node, look for child node in both and return list of parent nodes
        # containing child node
        node_matches = [(x := get_xml_value(node_path[0], node))[0] for node in xml
                        if (x := get_xml_value(node_path[0], node))]

        # # if only one node match, return it outside list, otherwise return all matches
        # if len(node_matches) == 1:
        #     return node_matches[0]

        return node_matches

    return get_nested_xml(get_xml_value(node_path[0], xml), *node_path[1:])


def xmlify_xpath(xpath):

    xpath = xpath.lstrip("/").split("/")
    group2_list = []
    xpath[0] = xpath[0].lstrip('/')  # all of the cisco apis being with an x so get rid of that shit

    group2_openclosetags = []
    group1_opentag = []
    group1_closetag = []

    for word in xpath:
        group1_opentag.append(f'<{word}>')

    for word in xpath[::-1]:
        group1_closetag.append(f"</{word}>")

    for word in group2_list:
        group2_openclosetags.append(f"<{word}></{word}>")

    new_xml_call = group1_opentag + group2_openclosetags + group1_closetag
    new_xml_call = "".join(new_xml_call)

    return new_xml_call

if __name__ == '__main__':

    with open('testing/status.xml') as f:
        xml_str = f.read()
        ixml = etree.fromstring(xml_str)

    tree = etree.ElementTree(ixml)
    root = tree.getroot()

    match1 = get_nested_xml(tree, "Registration/URI")
    match2 = get_nested_xml(tree, "Software/DisplayName")
    callstring = match1[0].text
    version = match2[0].text

    new_xml_call = xmlify_xpath(tree.getpath(match1[0]))

    # assert callstring == '29823@cucm.musc.edu' f"Registration/URI should equal 29823 for David's DX80"
