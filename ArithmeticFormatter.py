def arithmetic_arranger(problems, doer=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    arranged_problems = '    '
    el1 = []
    el2 = []
    el3 = []
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for problem in problems:
        elemtens = problem.split(' ')
        el1.append(elemtens[0])
        el2.append(elemtens[1])
        el3.append(elemtens[2])

    """ print(el1)
    print(el2)
    print(el3) """
    for i, j, k in zip(el1, el3, el2):
        if k not in ['-', '+']:
            return "Error: Operator must be '+' or '-'."
        if not i.isdigit():
            return "Error: Numbers must only contain digits."
        if not j.isdigit():
            return "Error: Numbers must only contain digits."
        if len(i) > 4 or len(j) > 4:
            return "Error: Numbers cannot be more than four digits."
        if len(i) > len(j):
            line1 = line1+'  '+'{:>}'.format(str(i))+'    '
            line2 = line2 + str(k)+' '+' ' * (len(i)-len(j)) + \
                '{:>}'.format(str(j))+'    '
        elif len(i) < len(j):
            line1 = line1+' '*(len(j)-len(i)+2)+'{:>}'.format(str(i))+'    '
            line2 = line2+str(k)+' '+'{:>}'.format(str(j))+'    '
        elif len(i) == len(j):
            line1 = line1+'  '+'{:>}'.format(str(i))+'    '
            line2 = line2+str(k)+' '+'{:>}'.format(str(j))+'    '
        #print(i, j, max(len(i),len(j)))
        line3 = line3+('-'*(max(len(i), len(j))+2))+'    '
        if doer == True:
            if k == '+':
                x = str(int(i)+int(j))
                if len(x) > max(len(i), len(j)):
                    line4 = line4+' '+'{:>}'.format(x)+'    '
                else:
                    line4 = line4+'  '+'{:>}'.format(x)+'    '
            else:
                x = str(int(i)-int(j))
                if len(x) > max(len(i), len(j)):
                    line4 = line4+' '+'{:>}'.format(x)+'    '
                else:
                    line4 = line4+'  '+'{:>}'.format(x)+'    '

    line1 = line1.rstrip()+'\n'
    line2 = line2.rstrip()+'\n'
    line3 = line3.rstrip()
    arranged_problems = line1 + line2 + line3
    if doer == True:
        arranged_problems += '\n'
        arranged_problems += line4.rstrip()

    return arranged_problems


print(arithmetic_arranger(
    ["3 + 855", "988 + 40"], True))
file1 = open("testumeu.txt", "w")
file1.write('Andrei:\n')
file1.writelines((arithmetic_arranger(
    ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'])))
