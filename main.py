import pypandoc
import os
from bs4 import BeautifulSoup
import sys

filepath = sys.argv[1]
print("Starting...")
print("Extracting epub file: " + filepath);

pathname, filename = os.path.split(filepath)
targetfilename = 'index.html'

pypandoc.convert_file(filepath,
                  format='epub',
                  to='html5',
                  extra_args=[
                      '--read=epub',
                      f'--extract-media={pathname}/output',
                      '--wrap=none',
                      '--standalone',
                  ],
                  encoding='utf-8',
                  outputfile=pathname + '/output/' + targetfilename,
                  filters=None,
                  verify_format=True
                 )
print("Done extracting epub file")

with open('./output/index.html') as f:
    html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    descendants_list = list(soup.descendants)
    total_elements = len(descendants_list) - 1

    for index, element in enumerate(descendants_list):
        print("process block ", index, " of " ,total_elements)
        if element.name == 'p' or element.name == 'h1' or element.name == 'h2' or element.name == 'h3' or element.name == 'h4' or element.name == 'h5' or element.name == 'h6' or element.name == 'li':
            element.string = "translated text"

    pypandoc.convert_text(soup.prettify(), 'epub', format='html', outputfile=f"./output/{filename}_latt_svenska.epub")
    print("Done writing new book to ", f"./output/{filename}_latt_svenska.epub")