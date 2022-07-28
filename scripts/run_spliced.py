# This emulates the entrypoint without the sys.exit (which spack treats as an error?)
import re
import sys
from spliced.client import run_spliced

if __name__ == "__main__":
    sys.argv[0] = re.sub(r"(-script\.pyw|\.exe)?$", "", sys.argv[0])
    run_spliced()
