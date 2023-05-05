# This is a sample Python script.
import Variables

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #   Outputting variables using the print() method
    print_hi('PyCharm')
    print(f"x is an int {Variables.x} {type(Variables.x)}")  # type() method
    # displays the variables type
    print(f"y is a string {Variables.y} {type(Variables.y)}")
    print(f"z is a float {Variables.z} {type(Variables.z)}")
    print(f"val_one = {Variables.val_one}")
    print(f"vals four five and six = {Variables.val_four}")

    print(f"list for unpacking = {Variables.list_one} {Variables.list_two} "
          f"{Variables.list_three}")
    print("Concatenating variables " + Variables.list_one + Variables.list_two +
          Variables.list_three + "support only + the same type")
    print("Comma seperated variables support different types", Variables.x,
          Variables.y, Variables.z)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
