# This file is from HLD-Equivalency
import argparse
from copy import deepcopy
import forseti.parser
import util

def runner(formula1, formula2, adjacency):
    formula1 = forseti.parser.parse(formula1)
    formula2 = forseti.parser.parse(formula2)
    print(type(formula1))

    statement1, steps1, isContra1 = util.convert(deepcopy(formula1), adjacency)
    statement2, steps2, isContra2 = util.convert(deepcopy(formula2), adjacency)

    return statement1 == statement2, [statement1, steps1, isContra1], [statement2, steps2, isContra2], formula1

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="Generate Truth Table for a logical formula")
    PARSER.add_argument('formula1', metavar='formula1', type=str, help='First formula to consider')
    PARSER.add_argument('formula2', metavar='formula2', type=str, help='Second formula to consider')
    PARSER_ARGS = PARSER.parse_args()
    equal, formula1, formula2 = runner(PARSER_ARGS.formula1, PARSER_ARGS.formula2)

"""     if equal:
        for steps, step_type in formula1[1]:
            for step in steps:
                print(util.pretty_print(step).ljust(120) + " | " + util.StepTypes.get_message(step_type))

        for steps, step_type in formula2[1]:
            for step in steps:
                print(util.pretty_print(step).ljust(120) + " | " + util.StepTypes.get_message(step_type))
 """