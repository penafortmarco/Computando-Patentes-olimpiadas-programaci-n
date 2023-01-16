from patent import next_patent

while(True):
    patent = str(input('Give me a patent ')).upper()
    k = int(input('How many patents do you want to advance: '))
    new_patent = next_patent(patent, k)
    print(new_patent)
