#!/usr/bin/env python
import argparse
import os
import sys

import file_impex
from springer_link import SpringerLink

EXPORTS_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'exports'))


def main():
    args = parse_args()
    springer_link = SpringerLink(args)
    urls = file_impex.load_urls_from_csv(args.file)
    file_impex.ensure_folder_exists(args.download_folder)
    springer_link.download_ebooks(urls)
    print_summary(args)
    springer_link.browser_handler.kill()


def print_summary(args):
    sys.stdout.write('===== SUMMARY =====\r\n')
    sys.stdout.write('Download folder: {folder}\r\n'.format(folder=args.download_folder))
    sys.stdout.write('===================\r\n\r\n')
    sys.stdout.flush()


def parse_args():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-f", "--file", help="path to file with the list of URLs - separated by linebreak",
                           required=True)
    argparser.add_argument("-d", "--download_folder", help="destination folder for the downloads", required=False,
                           default=EXPORTS_FOLDER)
    argparser.add_argument("-v", "--verbose", help="increase output verbosity", action="count", required=False)
    argparser.add_argument("-x", "--show_browser", help="show the browser doing his work", action="store_true",
                           required=False)
    args = argparser.parse_args()
    return args


if __name__ == "__main__":
    main()
