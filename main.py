import pypandoc
import os
from bs4 import BeautifulSoup
from pypandoc.pandoc_download import download_pandoc

download_pandoc()

filepath = "/Users/dan.popa/work/epub_to_latt_svenska_converter/ebook2.epub"
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

with open('./output/index.html') as f:
    html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    for element in soup.descendants:
        if element.name == 'p' or element.name == 'h1' or element.name == 'h2' or element.name == 'h3' or element.name == 'h4' or element.name == 'h5' or element.name == 'h6' or element.name == 'li':
            element.string = "translated text"

    pypandoc.convert_text(soup.prettify(), 'epub', format='html', outputfile="./output/translated.epub")