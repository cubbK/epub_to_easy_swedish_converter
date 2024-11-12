import pypandoc
import os
from bs4 import BeautifulSoup
import sys
from tqdm import tqdm

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

    for index, element in tqdm(enumerate(descendants_list), total=total_elements, desc="Processing blocks", unit="block"):
        if element.name in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']:
            element.string = "translated text"

    pypandoc.convert_text(soup.prettify(), 'epub', format='html', outputfile=f"./output/{filename}_latt_svenska.epub")
    print("Done writing new book to ", f"./output/{filename}_latt_svenska.epub")