#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Joey Brown w/ help from Coaches and Google"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument("text", help="text to be manipulated")
    parser.add_argument("-u", "--upper",
                        help="convert text to uppercase",
                        action="store_true")
    parser.add_argument("-l", "--lower",
                        help="convert text to lowercase",
                        action="store_true")
    parser.add_argument("-t", "--title",
                        help="convert text to titlecase",
                        action="store_true")
    return parser


def main(args):
    args = create_parser().parse_args(args)
    if not args:
        create_parser().print_usage()
        sys.exit(1)

    text = args.text

    if args.upper:
        text = text.upper()
    if args.lower:
        text = text.lower()
    if args.title:
        text = text.title()

    print(text)


if __name__ == '__main__':
    main(sys.argv[1:])
