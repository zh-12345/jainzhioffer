import sys

def f1():
    while True:
        # try:
        for lines in sys.stdin:
            # vec=[x for x in lines.strip().split()]
            vec = lines.split()
            vec = sorted(vec)
            vec = ' '.join(vec)
            print(vec)

ss= 'i am a student'
s = ss.split()
for i,element in enumerate(s):
    s[i] = element[::-1]
    print (i,s[i])
s= " ".join(s)
print(s)