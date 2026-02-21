input_file = "MmL_qq.12"   # <-- your original file
output_file = "second_qq.12"

with open(input_file, "r") as f:
    lines = f.readlines()

out_lines = []
i = 0
n = len(lines)

while i < n:
    line = lines[i]

    # If header line, copy it and process block
    if line.strip().startswith("#"):
        out_lines.append(line)
        i += 1

        block = []

        # Collect block lines until next header or EOF
        while i < n and not lines[i].strip().startswith("#"):
            if lines[i].strip():
                block.append(lines[i])
            i += 1

        if len(block) >= 2:
            # Take 3rd and 4th column from second bin
            second_bin = block[1].split()
            val3 = second_bin[2]
            val4 = second_bin[3]

            # Rewrite all bins in this block
            for b in block:
                cols = b.split()
                new_line = f" {cols[0]} {cols[1]} {val3} {val4}\n"
                out_lines.append(new_line)
        else:
            out_lines.extend(block)

    else:
        out_lines.append(line)
        i += 1

with open(output_file, "w") as f:
    f.writelines(out_lines)

print("Written:", output_file)
