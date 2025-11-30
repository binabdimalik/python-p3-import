from .module1 import function1
# from .. import module3
from .. import module3

if __name__ == "__main__":
    print("--- Executing Relative Imports ---")

    function1()
# module3.function1()
    module3.function1