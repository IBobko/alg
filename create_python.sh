#!/bin/bash

for i in {1..20}; do
    filename="script$i.py"
    touch "$filename"
    echo "#!/usr/bin/env python3" > "$filename"
    echo "import numpy as np" >> "$filename"
    echo "# This is a test Python script" >> "$filename"
    echo "# File: $filename" >> "$filename"
    echo "" >> "$filename"
    echo "print('Hello, world!')" >> "$filename"
    chmod +x "$filename"
done
