#!/bin/sh

while inotifywait -e close_write jinja; do ./compile.py; done
