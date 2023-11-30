def parse_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            if 'capgemini' in line:
                line = line.replace('capgemini', 'gmail')
            outfile.write(line)

input_file = 'Email_list.txt'
output_file = 'new_list.txt'

parse_file(input_file, output_file)
