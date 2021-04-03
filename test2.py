#Testing taking input, function call, while, if, return, lists 
def is_member(x:int, items:[int]) -> bool:
    i:int = 0
    while i < len(items):
        if items[i] == x:
            return True
        i += 1
    return False

def main():
    x: int = int( input() )
    if is_member(x, [4, 8, 15, 16, 23]):
        print("Item found!")    # Prints this
    else:
        print("Item not found.")

main()
