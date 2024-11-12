# Epub to Lätt Svenska Converter :turtle: :books:

Convert your books to easy swedish with the help of LLMs

Supports _swedish_ to _easy swedish_ conversions.

## Example

Original:

> ...Han gick ut från brandstationen och längs den nattliga gatan mot tunnelbanan, där det tysta luftdrivna tåget gled ljudlöst fram på sin oljade bana nere i jorden och med en kraftig puff av varm luft knuffade ut honom mot rulltrappan av gräddfärgat tegel som ledde upp till förstaden. ...

Converted:

> ...Han gick ut från brandstationen och längs en mörk gata mot tunnelbanan, där tåget rullade fram på sin bana i jorden. När han kom upp till trappan ledde den honom upp till förstaden. ...

## Getting Started

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py ./example.epub
```

The conversion on my m1 pro takes

- ~100 minutes on the book with 45000 words(average book size) `example.epub`

## Why?

I want to read swedish books. Unfortunatelly I'm not at the level that I can understand ones I actually want to read, thus this tool.

## How?

It converts the epub to html with pandadoc and then for every paragraph it runs an LLM prompt with https://docs.gpt4all.io/index.html and bundles the modified content back into .epub. 

Maintains book special fromatting and images.

It uses the default Meta-Llama-3-8B-Instruct.Q4_0 that requires 8gb or ram and is not very fast but any model supported by https://docs.gpt4all.io/ is possible.
