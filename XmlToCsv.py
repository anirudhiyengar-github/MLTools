import csv
import xml.etree.ElementTree as ET

def parse_xml(xml_file, csv_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header
        header = []
        for child in root[0]:
            header.append(child.tag)
        writer.writerow(header)
        
        # Write data
        for element in root.findall('object'):
            row = []
            for child in element:
                row.append(child.text)
            writer.writerow(row)

if __name__ == "__main__":
    xml_file = 'data.xml'
    csv_file = 'data.csv'
    parse_xml(xml_file, csv_file)
