#!/usr/bin/env bash

set -e

if ! command -v verible-verilog-lint &> /dev/null
then
    echo "verible-verilog-lint could not be found"
    exit 1
fi

for i in src/verilog/*.{v,sv}; do
    [ -f "$i" ] || break

    verible-verilog-lint "$i"
done
