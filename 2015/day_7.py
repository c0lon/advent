#!/usr/bin/env python

from copy import deepcopy
from pprint import pprint
import re
import sys

ASSIGN_RE = re.compile(r'([\d\w]+) -> (\w+)')
UNARY_RE  = re.compile(r'NOT ([\d\w]+) -> (\w+)')
BINARY_RE = re.compile(r'([\d\w]+) (AND|OR|LSHIFT|RSHIFT) ([\d\w]+) -> (\w+)')

def resolve(circuit, operand):
    while True:
        _operand = circuit.get(operand)
        if _operand is None or isinstance(_operand, tuple):
            return operand
        if isinstance(_operand, int):
            return _operand
        elif isinstance(_operand, str):
            return resolve(circuit, _operand)

def build_circuit(data):
    circuit = {}
    for line in data.splitlines():
        match_assign = ASSIGN_RE.match(line)
        match_unary = UNARY_RE.match(line)
        match_binary = BINARY_RE.match(line)

        if match_assign:
            value = match_assign.group(1)
            result = match_assign.group(2)

            try:
                circuit[result] = int(value)
            except ValueError:
                circuit[result] = value

        elif match_unary:
            operand = match_unary.group(1)
            result = match_unary.group(2)

            try:
                operand = int(operand)
            except ValueError:
                circuit[result] = ('not', operand)
            else:
                circuit[result] = ~operand

        elif match_binary:
            operand_1 = match_binary.group(1)
            op = match_binary.group(2).lower()
            operand_2 = match_binary.group(3)
            result = match_binary.group(4)

            try:
                operand_1 = int(operand_1)
            except ValueError:
                pass

            try:
                operand_2 = int(operand_2)
            except ValueError:
                pass

            circuit[result] = (op, operand_1, operand_2)

    return circuit


def resolve_circuit(circuit):
    _circuit = deepcopy(circuit)
    for wire, value in circuit.items():

        if isinstance(value, str):
            _circuit[wire] = resolve(circuit, value)

        elif isinstance(value, tuple):
            if len(value) == 2:
                op, operand = value
                operand = resolve(circuit, operand)

                try:
                    _circuit[wire] = ~operand
                except TypeError:
                    _circuit[wire] = ('not', operand)

            elif len(value) == 3:
                op, operand_1, operand_2 = value

                if op == 'and':
                    func = lambda x, y: x & y
                elif op == 'or':
                    func = lambda x, y: x | y
                elif op == 'lshift':
                    func = lambda x, y: x << y
                elif op == 'rshift':
                    func = lambda x, y: x >> y

                operand_1 = resolve(circuit, operand_1)
                operand_2 = resolve(circuit, operand_2)

                try:
                    _circuit[wire] = func(operand_1, operand_2)
                except TypeError:
                    _circuit[wire] = (op, operand_1, operand_2)

        circuit = _circuit

    return circuit


def wire_signals(filepath):
    data = open(filepath).read()
    circuit = build_circuit(data)

    while not isinstance(circuit.get('a'), int):
        circuit = resolve_circuit(circuit)

    return circuit['a']


def wire_signals_2(filepath):
    data = open(filepath).read()
    circuit = build_circuit(data)
    circuit['b'] = wire_signals(filepath)

    while not isinstance(circuit.get('a'), int):
        circuit = resolve_circuit(circuit)

    return circuit.get('a')


if __name__ == '__main__':
    filepaths = ['day_7_input.txt']
    if len(sys.argv) > 1:
        filepaths.extend(sys.argv[1:])

    for filepath in filepaths:
        # print(wire_signals(filepath))
        print(wire_signals_2(filepath))