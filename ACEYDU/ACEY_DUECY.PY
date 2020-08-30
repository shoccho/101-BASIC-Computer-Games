import random

"""
GAME OF ACEY-DUCEY WRITTEN BY BILL PALMBY
ADLAI STEVENSON HIGH SCHOOL, PRAIRE VIEW, ILL
TRANSLATED TO RSTS/E BY DAVE AHL, DIGITAL

REWRITTEN IN PYTHON BY SHOCCHO
"""
print("""ACEY-DUCEY IS PLAYED IN THE FOLLOWING MANNER :
THE DEALER (COMPUTER) DEALS TWO CARDS FACE UP.
YOU HAVE THE OPTION TO BET OR NOT TO BET DEPENDING
ON WHETHER OR NOT YOU FEEL THE NEXT CARD WILL HAVE
A VALUE BETWEEN THE FIRST TWO
IF YOU DO NOT WANT TO BET, INPUT A 0. """)

print("")
N = 100
Q = 100

CARDS = [0,1,2,3,4,5,6,7,8,9,10,"JACK","QUEEN","KING","ACE"]
while True:
    print("YOU NOW HAVE {} DOLLARS".format(Q))
    print("HERE ARE YOUR NEXT TWO CARDS. . . ")
    A = random.randint(2, 14)
    B = random.randint(2, 14)
    if A>B:
        A, B = B, A
    print(CARDS[A])
    print(CARDS[B])
    print("")
    M = int(input("WHAT IS YOUR BET "))

    if M==0:
        print("CHICKEN!!")
        print("")
        continue
    while M>Q:
        print("SORRY, MY FIREND, BUT YOU BET TOO MUCH")
        print("YOU HAVE ONLY {} DOLLARS TO BET. ".format(Q))
        M = int(input("WHAT IS YOUR BET"))
    C = random.randint(2, 14)
    print(CARDS[C])
    print("")
    if C > A and C < B:
        print("YOU WIN!!!")
        Q += M
    else:
        print("SORRY, YOU LOSE")
        Q -= M
        if Q < 1:
            print("")
            print("SORRY, FRIEND, BUT YOU BLEW YOUR WAD. ")
            AS = input("TRY AGAIN (YES OR NO) ")
            if AS == "YES":
                Q=100
                continue
            else:
                print("O.K. HOPE YOU HAD FUN!!")
                break
