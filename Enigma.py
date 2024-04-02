
def decode():
    # Read the contents of the file
    with open("moje.txt", 'r') as file:
        lines = file.readlines()

    # Initialize a list to store the word-number pairs
    word1 = []
   
    msg = []

    # Iterate through the lines to extract words and their associated numbers
    for line in lines:
        parts = line.split()
        number = int(parts[0])
        word = parts[1]
        podlista = []
        podlista.append(number)
        podlista.append(word)
        word1.append(podlista)


    #sorting list by numbers, from low to high

    sort = sorted(word1, key=lambda x: x[0])

   #making list with array (1,3,6,10,15,21)
    fib=[]
    n=1
    for i in range(2,len(lines)):   
            fib.append(n)
            n=n+i
            
    #comparing list sort and fib

    for j in sort:
        if j[0] in fib:
            msg.append(j[1])
    #konverting list to string
    string = ' '.join(msg)
    print(string)
    
    
   
decode()
