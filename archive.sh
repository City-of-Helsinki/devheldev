#!/usr/bin/env bash

wget --mirror            \
    --convert-links     \
    --html-extension    \
    --wait=2            \
    -o log              \
    --exclude-directories='/paatokset' \
    https://dev.hel.fi
