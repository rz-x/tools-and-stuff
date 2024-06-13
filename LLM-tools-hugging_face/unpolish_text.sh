#!/bin/bash
# Hash Crack Challenge step
cat $1 |sed 'y/ąćęłńóśźżĄĆĘŁŃÓŚŹŻ/acelnoszzACELNOSZZ/' | tr -d '[:punct:]' | tr '[:upper:]' '[:lower:]' | tr -d ' '
