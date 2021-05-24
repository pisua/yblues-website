import ycappuccino.core
import ycappuccino.mongo
import logging
import argparse

# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Setup logs
    logging.basicConfig(level=logging.INFO)
    root_path = None
    parser = argparse.ArgumentParser(description='argument for yblues application')
    parser.add_argument('--root-path', dest='root_path', action='store_const',
                        const=root_path,  default=None,
                        help='path of application modules and packages')

    args = parser.parse_args()

    ycappuccino.core.init(root_path=args.root_path,port=9001)
    # Run the server
    ycappuccino.core.start()

