#!/usr/bin/env python3

###
# Day 7 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

from collections import namedtuple
import copy


Gate = namedtuple('Gate', 'op in1 in2 out')


def get_value(wires, gate_in):
    if gate_in is None:
        return None
    try:
        return int(gate_in)
    except ValueError:
        return wires.get(gate_in)


def set_value(wires, out, val):
    if out not in wires:
        wires[out] = val


def simulate(gates, wires):
    for gate in copy.copy(gates):
        val1 = get_value(wires, gate.in1)
        val2 = get_value(wires, gate.in2)
        if (gate.op is None or gate.op == 'NOT') and val1 is not None:
            if gate.op is None:
                set_value(wires, gate.out, val1)
            else: # NOT
                set_value(wires, gate.out, 65535 - val1)
            gates.remove(gate)
        elif val1 is not None and val2 is not None: # 2-arg OP
            if gate.op == 'AND':
                set_value(wires, gate.out, val1 & val2)
            elif gate.op == 'OR':
                set_value(wires, gate.out, val1 | val2)
            elif gate.op == 'LSHIFT':
                set_value(wires, gate.out, val1 << val2)
            elif gate.op == 'RSHIFT':
                set_value(wires, gate.out, val1 >> val2)
            gates.remove(gate)


def run(lines, wires):
    gates = set()  # gates that have not been calculated yet 
    outputs = set()
    for line in lines:
        fragments = line.split()
        if len(fragments) == 5:
            in1, op, in2, arrow, out = fragments
        elif len(fragments) == 4:
            op, in1, arrow, out, in2 = *fragments, None
        elif len(fragments) == 3:
            op, in1, arrow, out, in2 = None, *fragments, None
        if not out.isdigit():
            outputs.add(out)
        gates.add(Gate(op, in1, in2, out))

    while outputs - set(wires):
        simulate(gates, wires)
    return wires


def part_one(lines):
    '''
    This year, Santa brought little Bobby Tables a set of wires and bitwise
    logic gates! Unfortunately, little Bobby is a little under the recommended
    age range, and he needs help assembling the circuit.

    Each wire has an identifier (some lowercase letters) and can carry a 16-bit
    signal (a number from 0 to 65535). A signal is provided to each wire by a
    gate, another wire, or some specific value. Each wire can only get a signal
    from one source, but can provide its signal to multiple destinations. A
    gate provides no signal until all of its inputs have a signal.

    The included instructions booklet describes how to connect the parts
    together: x AND y -> z means to connect wires x and y to an AND gate, and
    then connect its output to wire z.

    Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If,
    for some reason, you'd like to emulate the circuit instead, almost all
    programming languages (for example, C, JavaScript, or Python) provide
    operators for these gates.

    In little Bobby's kit's instructions booklet (provided as your puzzle
    input), what signal is ultimately provided to wire a?
    '''
    return run(lines, {})['a']


def part_two(lines, wires):
    '''
    Now, take the signal you got on wire a, override wire b to that signal, and
    reset the other wires (including wire a). What new signal is ultimately
    provided to wire a? 
    '''
    return run(lines, wires)['a']


def main():
    with open('input/day07.txt') as f:
        lines_strip = (line.strip() for line in f)
        lines = [line for line in lines_strip if line]

    example_lines = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i',
    ]
    assert run(example_lines, {}) == {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123, 
        'y': 456,
    }

    part_one_result = part_one(lines)
    print(part_one_result)
    print(part_two(lines, {'b': part_one_result}))
    

if __name__ == '__main__':
    main()
