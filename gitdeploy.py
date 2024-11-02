import os

def rebase() -> None:
    with open(htmlfile) as f:
        for line in f:
            if line.startswith('<base>'):
                line = '<base href="https://cereal137.github.io/">'

    pass