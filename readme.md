# Convert subtitle to text file

Configs in `extract.py`:
```python
SUBS_DIR = 'srt'
SUBS_EXTENSION = ['.srt']
TEXT_EXTENSION = '.txt'
IGNORE_SUBDIR = []
```

New text files are generated in the same directory with original subtitle files.  

Notes:  
The script was wrote to extract text from the subtitle of Udacity videos initially.