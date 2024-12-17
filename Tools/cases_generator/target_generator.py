"""Generate targets for computed goto dispatch
Reads the instruction definitions from bytecodes.c.
Writes the table to opcode_targets.h by default.
"""

import argparse

from analyzer import (
    Analysis,
    analyze_files,
)
from generators_common import (
    DEFAULT_INPUT,
    ROOT,
)
from cwriter import CWriter
from typing import TextIO


DEFAULT_OUTPUT = ROOT / "Python/opcode_targets.h"


def write_opcode_targets(analysis: Analysis, out: CWriter) -> None:
    """Write header file that defines the jump target table"""
    targets = ["&&_unknown_opcode,\n"] * 256
    for name, op in analysis.opmap.items():
        if op < 256:
            targets[op] = f"&&TARGET_{name},\n"
    """replace unknown_opcode to external_opcode"""
    replacement_targets = {
        119: "&&TARGET_CALL_EXTERNAL,\n",
        120: "&&TARGET_BINARY_OP_EXTERNAL,\n",
        121: "&&TARGET_BINARY_SUBSCR_EXTERNAL,\n",
    }
    for index, replacement in replacement_targets.items():
        assert targets[index] == "&&_unknown_opcode,\n"
        targets[index] = replacement
    
    out.emit("static void *opcode_targets[256] = {\n")
    for target in targets:
        out.emit(target)
    out.emit("};\n")

arg_parser = argparse.ArgumentParser(
    description="Generate the file with dispatch targets.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

arg_parser.add_argument(
    "-o", "--output", type=str, help="Generated code", default=DEFAULT_OUTPUT
)

arg_parser.add_argument(
    "input", nargs=argparse.REMAINDER, help="Instruction definition file(s)"
)

if __name__ == "__main__":
    args = arg_parser.parse_args()
    if len(args.input) == 0:
        args.input.append(DEFAULT_INPUT)
    data = analyze_files(args.input)
    with open(args.output, "w") as outfile:
        out = CWriter(outfile, 0, False)
        write_opcode_targets(data, out)
