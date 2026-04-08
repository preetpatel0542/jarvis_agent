"""Test script for JARVIS with predefined input"""
import sys

# Mock input to provide test commands
test_commands = [
    "time",
    "tell me about python",
    "joke",
    "exit"
]

test_input_iter = iter(test_commands)

# Override input function
original_input = input
def mock_input(prompt=""):
    cmd = next(test_input_iter, None)
    if cmd is None:
        raise EOFError()
    print(f"{prompt}{cmd}")
    return cmd

import builtins
builtins.input = mock_input

# Now run jarvis
from jarvis import main
main()
