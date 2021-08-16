import re
import os

def main():
    for filename in os.listdir('./'):
        if filename.endswith('.js') and not filename.startswith('icons'):
            with open(filename) as f:
                lines = f.readlines()
                decalartion = ''
                svg = ''
                a = False
                for i in range(len(lines)):
                    if (not a and re.match("const.*", lines[i])):
                        decalartion = lines[i].split('=')[0] + "= "
                        a = True
                        continue
                    if (re.match(".*<svg.*", lines[i])):
                        for j in range(i, len(lines)):
                            svg = svg + lines[j]
                            if (re.match(".*</svg>", lines[j])):
                                break
                with open('icons.js', 'a') as r:
                    r.write(decalartion + '\n `' + svg + '`\n')
                
                    
                
if __name__ == '__main__':
    main()