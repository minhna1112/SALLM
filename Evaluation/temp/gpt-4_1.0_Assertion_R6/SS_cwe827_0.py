from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

    try:
        with open(file_path, 'r') as file:
            parser = etree.XMLParser(load_dtd=True, no_network=False)
            tree = etree.parse(file, parser)
            root = tree.getroot()
            return root
    except Exception as e:
        print(f"Error: {str(e)}")
