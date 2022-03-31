#D21CE161
inputs = int(input())
for i in range(inputs):
    entries = input()
    length = len(entries)
    if length % 2 == 0:
        b, c = entries[:length//2], entries[length//2:]
    else:
        b, c = entries[:length//2], entries[length//2+1:]
    if sorted(b) == sorted(c):
        print("\nYES")
    else:
        print("\nNO")
