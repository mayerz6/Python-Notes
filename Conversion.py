import re

# Define the input file name and output file name
input_file = '.\\x1000mega_asciifree.txt'
output_file = '.\\x1000mega_scrub.sql'

# Define the pattern to match email:password
pattern = r'(.+?)@(.+?):(.+)'

# Create FIle called - split-file.py or file-clunks.py

# Open the input file for reading and the output file for writing
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile: 
    
   # 
    for line in infile:
        # Search for the pattern in the line
        match = re.search(pattern, line)
        if match:
            # email = match.group(1)
            # password = match.group(3)
            
            # Generate SQL INSERT statement
            sql_insert = f'INSERT INTO `sep_combolist_2023` (email, password) VALUES ("{match.group(1)}@{match.group(2)}", "{match.group(3)}");\n'
            
            # Write the SQL statement to the output file
            outfile.write(sql_insert)

            
    
print(f'SQL INSERT statements written to {output_file}')
