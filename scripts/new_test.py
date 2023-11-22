input_vcf_filename = 'path_to_input_file.vcf'
output_header_filename = 'path_to_output_header_file.vcf'  

with open(input_vcf_filename, 'r') as input_file, open(output_header_filename, 'w') as output_file:
    for line in input_file:
        if line.startswith('#'):
            output_file.write(line)
