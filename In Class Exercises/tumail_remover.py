import re

data = open("email_test.txt.tex", 'r')

output_file = open('email_output.txt', 'w')
pattern = 'tu[a-z]\d{5}@temple\.edu'

for line in data:
    line = re.sub(pattern, '[REDACTED]', line)
    output_file.write(line) #writes new file

data.close()
output_file.close()
