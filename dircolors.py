#!/usr/bin/env python

import os.path, yaml
from glob import glob

ME = os.path.splitext(os.path.basename(__file__))[0]

def here(fn):
    return os.path.join(os.path.dirname(__file__), fn)

def main():
    tmpl = open(here(ME+'.tmpl')).read()
    for yml in glob(here('*.yml')):
        data = yaml.load(open(yml).read())
        fmt = data['format']
        lines = []
        for n, exts in data['extensions'].items():
            for ext in exts:
                lines.append(' '.join([ext, fmt.format(n=n)]))
        open(os.path.splitext(yml)[0], 'w').write(
                tmpl.replace('{{DATA}}', '\n'.join(lines))
                )

if __name__ == '__main__': main()
