import pypandoc
import os
from bs4 import BeautifulSoup
import sys
from tqdm import tqdm
from gpt4all import GPT4All

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
                if(len(element.text) < 30) :
                    continue

                print("Processing: ", element.text, index)
                model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
                with model.chat_session():
                    new_text = model.generate(f"with the following text in quotes: '{element.text}' which is in swedish. Convert it to easy swedish that can be understood at A2 level. Output ONLY the converted text and nothing more! If the text cannot be converted output the original. DO NOT add any comments. remove '. speak in SWEDISH.", max_tokens=2048)
                    element.string = new_text + ' ۞'
                    # update the file for faster feedback
                    with open(f"./output/{filename}_latt_svenska.html", 'w') as output:
                        output.write(soup.prettify())
        
        with open(f"./output/{filename}_latt_svenska.html", 'w') as output:
            output.write(soup.prettify())

        pypandoc.convert_text(soup.prettify(), 'epub', format='html', outputfile=f"./output/{filename}_latt_svenska.epub")
        print("Done writing new book to ", f"./output/{filename}_latt_svenska.epub")