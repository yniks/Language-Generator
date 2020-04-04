'''USING single character names only,(yet),CAPS for non terminals'''

"""
P- postalcode
F- forwardsortationarea
Q- provarea
T- loctype
R- Rural
U- Urban
A- space
L- letter
D- Digit
O- localdeliveryunit
"""
Symbols="""A::=a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
D::=0|1|2|3|4|5|6|7|8|9
B::=(){}[]
M::=+|-|/|*
P::=~|`|!|@|#|$|%|&|?|"|:|'|;|.|,"""
BNF_POSTALCODE=('''S::=FAO
F::=QTL
O::=DLD
Q::=a|b|c|e|g|h|j|k|l|m|n|p|r|s|t|v|x|y
T::=R|U
R::=0
A::= 
U::=1|2|3|4|5|6|7|8|9
L::=a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
D::=0|1|2|3|4|5|6|7|8|9''')#inp[:-1])

"""
Y -year code of 2 digits
C -college code of 3 digits
B - Branch code of 2 digits
R - student number of 3 dogit
"""
BNF_AKTU_ROLLNumber='''S::=Y-C-B-R
D::=1|7|8|9|2|3|4|5|6|7|0
Y::=DD
C::=DDD
B::=DD
R::=DDD'''

BNF_MOBILE_PHONE_NUMBER=('''S::=FATUUUUUUUUUU
F::=+|
A::=91|90|93|92|102|1|2|4|0
T::=7|8|9
U::=1|2|3|4|5|6|7|8|9''')

from main import ParseAndGenerate
def printGeneratedLanguage(grammer,limit=10):
    for line in ParseAndGenerate(grammer,limit=limit):
        for each in line:
            print(each,end="")
        else:
            print()
while True:
    print("\033[33m=================== Generate Languge from Grammer ===============\033[0m")
    print("""0.Type One Line of Grammer
1.AKTU RollNumber
2.MOBILE Phone Number
3.PIN CodeNumber
    [\033[31mexit=Other Number\033[0m]""")
    try:
        choice=int(input())
        if choice==0:
            print("\033[34mFollowing Symbols are usable in the scope.\033[0m")
            print("""D == decimal digits
B == Brackets (){}[]
A == small alphabet
M == Mathmetical symbols ?*+-=<>^
P == Special Symbols""")
            line="S::="+input("\033[33mEnter BNF\033[0m: S::=")
            line+='\n'+Symbols
        elif choice==1:
            line=BNF_AKTU_ROLLNumber
        elif choice==2:
            line=BNF_MOBILE_PHONE_NUMBER
        elif choice==3:
            line=BNF_POSTALCODE
        else:
            print("\033[31mExiting..\033[0m")
            break
        limit=10
        try:
            limit=int(input(f"\033[33mEnter Number of Sentences[default={limit}]\033[0m:"))
        except:pass
        printGeneratedLanguage(line,limit)

    except BaseException as e:
        print("Error")
        pass
