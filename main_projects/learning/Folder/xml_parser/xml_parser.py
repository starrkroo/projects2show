import xml.etree.ElementTree as ET
from datetime import datetime

new_root = ET.Element('Menu')
new_branch_1 = ET.SubElement(new_root, 'Main')
new_branch_2 = ET.SubElement(new_root, 'News')
new_branc_item = ET.SubElement(new_branch_2, 'First')
new_item_of_branch = ET.SubElement(new_branch_2, 'Date')
new_branch_3 = ET.SubElement(new_root, 'About')


new_branch_1.text = 'Main text'
new_branc_item.text = 'Telegram in block'
new_branch_3.text = 'PrOxy fans'
new_item_of_branch= datetime.now()


for_file = ET.tostring(new_root)
f = open('New_list_of_users.xml', 'wb')
f.write(for_file)