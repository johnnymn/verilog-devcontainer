#!/usr/bin/env bash

for i in **/*.{v,sv}; do
    [ -f "$i" ] || break

    verible-verilog-lint "$i"
done
