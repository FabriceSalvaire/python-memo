source .venv/bin/activate

append_to_python_path_if_not ${PWD}
append_to_python_path_if_not $PWD/examples/memo-tools
append_to_python_path_if_not $PWD/examples/references

append_to_python_path_if_not $PWD/rassumfrassum/src/
