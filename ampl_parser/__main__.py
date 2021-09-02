import os
from ampl_parser import AMPLParser

if __name__ == '__main__':
    new_parser = AMPLParser()
    new_parser.parse(f"{os.path.dirname(__file__)}/data/simple.mod")
