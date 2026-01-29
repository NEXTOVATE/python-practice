def dna_symbol(n):
    ans = ""
    dna = {"A":"T",
           "T":"A",
           "C":"G",
           "G":"C"}
    for i in n:
        ans += dna[i]

        

n = input("Enter the DNA string symbol : ")

print(dna_symbol(n))



