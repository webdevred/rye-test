
import argparse
import numpy as np
import re
from rs import calc_func, hello_func


def calc_procedure():

    def generate_matrix_from_raw_input(raw_input:str)->np.ndarray:
        try:
            pattern = r"(\s*)"+r"(\s+)".join([r"(?P<num{}>\d+)".format(i+1) for i in range(4)])+r"(\s*)"
            match = re.match(pattern, raw_input)
            matrix = np.array([int(match.group("num{}".format(i+1))) for i in range(4)]).reshape(2,2)
        except AttributeError as e:
            raise Exception("Invalid input!")
        return matrix
    
    raw_input1 = input('input four integers to create first 2x2 matrix.\n(e.g: 5 7 3 12): ',)
    arr1 = generate_matrix_from_raw_input(raw_input1)
    print("generated first matrix:\n", arr1)
    raw_input2 = input('input four integers to create second 2x2 matrix.\n(e.g: 5 7 3 12): ',)
    arr2 = generate_matrix_from_raw_input(raw_input2)
    print("generated second matrix:\n", arr2)
    result = calc_func(arr1, arr2)
    print("calculation result:\n",result)
    return

def hello_procedure():
    hello_func()
    return

subcommand_procedures = {
    'calc': calc_procedure,
    'hello': hello_procedure
}

def generate_args():
    parser = argparse.ArgumentParser(
        prog='rye-sample-command',
        description='Adaptively call rye-sample functions with corresponding commands',
        epilog='')
    parser.add_argument('subcommand', choices=list(subcommand_procedures.keys()))
    args = parser.parse_args()
    return args

def main():
    args = generate_args()
    selected_procedure = subcommand_procedures[args.subcommand]
    selected_procedure()

if __name__ == "__main__":
    main()
