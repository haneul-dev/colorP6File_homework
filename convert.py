def convert_p6_to_p3(input_path, output_path):
    with open(input_path, 'rb') as f:
        magic = f.readline().strip()
        if magic != b'P6':
            return

        def read_non_comment(file):
            line = file.readline()
            while line.startswith(b'#'):
                line = file.readline()
            return line

        size_line = read_non_comment(f)
        width, height = map(int, size_line.strip().split())
        maxval = int(read_non_comment(f).strip())
        pixel_data = f.read()

    with open(output_path, 'w') as out:
        out.write("P3\n")
        out.write(f"{width} {height}\n")
        out.write(f"{maxval}\n")
        for i in range(0, len(pixel_data), 3):
            r = pixel_data[i]
            g = pixel_data[i+1]
            b = pixel_data[i+2]
            out.write(f"{r} {g} {b}\n")

convert_p6_to_p3("colorP6File.ppm", "colorP3File.ppm")
