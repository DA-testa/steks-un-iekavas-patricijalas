# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
   pos=0
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
            pos=pos+1
            # Process opening bracket, write your code here
            
        if next in ")]}":
            if pos==0 and i==0:
                return 1
            if pos>0 and are_matching(opening_brackets_stack [pos-1].char,next):
                del opening_brackets_stack [-1]
                pos=pos-1
            else:
                return i+1
            # Process closing bracket, write your code here
            
    if pos==0:
        return 'Success'
    else:
        return opening_brackets_stack [-1].position+1



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
