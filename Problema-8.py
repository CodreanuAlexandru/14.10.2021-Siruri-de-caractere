a=input('Introduceti sirul de caractere:')
for i in range(len(a)):
    if a[i]!=' ' and a[i]!='Z':
        a=a.replace(a[i],chr(ord(a[i])+1))
    if a[i]=='Z':
            a=a.replace(a[i],'A')
    if a[i]==' ':
        a=a.replace(a[i],'-')
print(a)