# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press Ctrl+F8 to toggle the breakpoint.

data = {'data':1,'var':'one'}
class Demo():
    count=0
    def __init__(self):
        data.append(self)
    def printme(self):
        print(self.count)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(10):
        data.append(Demo())
    for i in data:
        print(i.count)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
