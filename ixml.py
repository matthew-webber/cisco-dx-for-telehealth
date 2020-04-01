def get_xml_value(target, xml):
    return [node for node in xml.iter(target)][0]


def get_nested_xml(xml, *args):
    """
    provided with an xml root and e.g. "UserInterface", "ContactInfo", "Name", will produce node containing DX/SX name
    :param xml: XML root
    :param args: nested nodes
    :return: XML node
    """
    i = 0
    if len(args) == 1:
        return get_xml_value(args[0], xml)
    # if i == 0:
    #     i += 1
    return get_nested_xml(get_xml_value(args[0], xml), *args[1:])
    # else:

# def get_xml_nest(target1, target2, xml):
#     print([tag for tag in xml.iter(target1)])