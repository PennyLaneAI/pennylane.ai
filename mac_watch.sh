#!/bin/sh

python3 compile.py && open -a Google\ Chrome.app site/index.html && fswatch jinja | (while read; do python3 compile.py test; done)
