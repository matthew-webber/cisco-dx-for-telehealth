import xml.etree.ElementTree as ET


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


if __name__ == '__main__':
    with open('testing/status.xml') as f:
        ixml = ET.fromstring(f.read())

    assert '29823@cucm.musc.edu' == get_nested_xml(ixml, "Registration/URI")[0].text,\
        f"Registration/URI should equal 29823 for David's DX80"
