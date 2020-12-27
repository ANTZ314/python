#!/usr/bin/env bash
# Purpose: batch link listed videos in input file

ffmpeg -f concat -safe 0 -i input.txt -c copy output7.mp4