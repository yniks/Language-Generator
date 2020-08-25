# String Generator

## A PEG like language generator powered by logical/arithmetic operators.
## Enter Grammer -> Iterate over Sentences of that grammer
##### Example:
```python3
BNF_AKTU_ROLLNumber='''S::=Y-C-B-R
D::=1|7|8|9|2|3|4|5|6|7|0
Y::=DD
C::=DDD
B::=DD
R::=DDD'''

BNF_MOBILE_PHONE_NUMBER='''S::=FATUUUUUUUUUU
F::=+|
A::=91|90|93|92|102|1|2|4|0
T::=7|8|9
U::=1|2|3|4|5|6|7|8|9'''
```
### Above grammer can produce:
Mobilephone Numbers like ```+919787618222 or 07878987865 ... ```

AKTU Univerisity rollnumbers like ```1713310127 or 1713310110 ```

### TODO : Implement
  - [x] logical Sum
  - [ ] logical Product
  - [x] chaining
  - [ ] Negation 

NOTE: ```logical product``` is not applicable in a linear single chain, like in string generation
