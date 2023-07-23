#!/bin/bash

echo "Enter the file extension to search for (e.g., txt, jpg, etc.):"
read extension

echo "Search results for .$extension files:"
find /path/to/directory -type f -name "*.$extension" 2>/dev/null
