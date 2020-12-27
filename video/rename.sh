#!/usr/bin/env bash
# Purpose: batch file rename

# 
ls -v | cat -n | while read n f; do mv -n "$f" "$n.mp4"; done