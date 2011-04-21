#!/usr/bin/env python

import os.path, yaml

def get_file(ext=''):
    return os.path.splitext(__file__)[0]+ext

def get_data(ext=''):
    return open(get_file(ext)).read()

def output_data(data):
    s = []
    for a in data:
        for n in data[a]:
            for ext in data[a][n]:
                s.append('%s 0%s;3%s' % (ext, a, n))
    open(get_file(), 'w').write(
            get_data('.tmpl').replace('{{DATA}}', '\n'.join(s))
            )

def main():
    output_data(yaml.load(get_data('.yml')))

if __name__ == '__main__': main()
