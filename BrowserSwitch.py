#!/usr/bin/python

import json
import re
import subprocess
import sys

from urlparse import urlparse

DEFAULT_BROWSER = "Safari"


def openBrowser(args, browser):
    subprocess.call(["open", "-a", browser] + args)


def main(args):
    url = args[0]

    if url:
        urlParsed = urlparse(url)

        checks = json.load(open('checks.json', 'r'))

        for check in checks:
            if check.get('default', False):
                return openBrowser(args, check.get('browser', DEFAULT_BROWSER))

            for pattern in check.get('patterns', ()):
                if re.match(pattern, urlParsed.netloc):
                    return openBrowser(args, check.get('browser', DEFAULT_BROWSER))

        return openBrowser(args, DEFAULT_BROWSER)


if __name__ == "__main__":
    main(sys.argv[1:])
