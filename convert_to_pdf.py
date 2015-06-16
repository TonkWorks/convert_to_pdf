#!/usr/bin/env python

import argparse
import os
import subprocess

__info__ = {
	'title': "Convert a document to pdf",
    'description': "Convert a document to pdf",
    'url': "http://github.com/TonkWorks/convert_a_document_to_pdf/archive/master.zip",
    'input': [
        {
            'label': 'Document to turn into a pdf',
            'type': 'file',
            'map': 'file',
        }
    ]
}

def script():
    parser=argparse.ArgumentParser()
    parser.add_argument('--file')

    args=parser.parse_args()
    file_path = args.file

    root = os.path.dirname(os.path.abspath(__file__))
    converter_path = os.path.join(root, "converter", "pyText2Pdf.py") #http://code.activestate.com/recipes/511465-pure-python-pdf-to-text-converter/
    subprocess.call(["python", converter_path, args.file])

if __name__ == '__main__':
	script()
