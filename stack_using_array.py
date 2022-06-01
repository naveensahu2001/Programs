class Stack: 
    items = [];

    def __init__(self):
        self.items = []

    def  pushing(self, element): 
        self.items.append(element) 

    def  poping(self): 
        if len(self.items) == 0:
            print('Can not pop form an empty list')
        self.items.pop();
        print('Last item has been poped from the list')

    def  show(self): 
        for i in self.items:
            print(i)

    def isEmpty(self):
        print(len(self.items) == 0)

    def peeking(self):
        if len(self.items) == 0:
            print('Stack is Empty')
        print(self.items[len(self.items) - 1]) 
if __name__ == '__main__':
    s=Stack()
    s.pushing(input("Enter elemnets to push"))
    s.show()
    s.pushing(input("Enter elemnets to push"))
    s.show()
    s.poping()
    s.show()
    s.peeking()
