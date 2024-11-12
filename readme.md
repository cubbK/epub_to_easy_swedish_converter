# Epub to Lätt Svenska Converter

Convert your books to easy swedish with the help of LLMs

Supports both _swedish_ to _easy swedish_ conversions and _english_ to _easy swedish_ conversions.

Adaptable to any language

## Why?

I want to read swedish books. Unfortunatelly I'm not at the level that I can understand ones I actually want to read, thus this tool.

## How?

It converts the epub to html with pandadoc and then for every paragraph it runs an LLM prompt with https://docs.gpt4all.io/index.html and bundles the modified content back into .epub.

## Getting Started

TODO

## Run Source

```
pip install -r requirements.txt
```

```
python3 main.py ./example.epub
```
