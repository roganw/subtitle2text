# -*- encoding: utf-8 -*-
import pysrt
import os
import re

SUBS_DIR = 'srt'
SUBS_EXTENSION = ['.srt']
TEXT_EXTENSION = '.txt'
IGNORE_SUBDIR = []


def extract_text(root, filename, extension):
    """
    generate text file
    @param root: absolutely file path
    @param filename: srt filename
    @param extension: srt extension
    @return: None
    """
    subs = pysrt.open(os.path.join(root, filename))
    text = '\n'.join([sub.text for sub in subs])

    rep_str = re.compile(extension + '$')
    new_file = rep_str.sub(TEXT_EXTENSION, filename)
    new_file = os.path.join(root, new_file)

    with open(new_file, 'w') as f:
        f.write(text)


def process_dir():
    """
    traverse directory to extract text from srt files
    @return: None
    """
    for root, dirs, files in os.walk(SUBS_DIR, topdown=True):
        if root.split('/')[-1].lower() in IGNORE_SUBDIR:
            continue
        for filename in files:
            extension = os.path.splitext(filename)[1].lower()
            if extension in SUBS_EXTENSION:
                extract_text(root, filename, extension)


process_dir()

