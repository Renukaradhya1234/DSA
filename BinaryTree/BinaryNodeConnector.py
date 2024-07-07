from BinaryNode import *


class BinaryNodeConnector :
    def __init__(self, NewData: int) -> None:
        self.RootNode: BinaryNode = BinaryNode(NewData)

    # >>>>>>>>>>>>>>>>>>>> CRUD operations starts<<<<<<<<<<<<<<<<<<<<

    # CREATE operation........
    def InsertData(self, NewData: int) -> None :
        self.RootNode.InsertData(NewData)
    
    # READ operation..........
    def DisplayTreeValues(self) -> None :
        self.DisplayLeftNode(self.RootNode)
        self.DisplayRightNode(self.RootNode.GetRightNode())

    def UpdateNodeValues(self, OldValue: int, NewValue: int) -> None :
        pass

    def DeleteNode(self, Value) -> None:
        pass
    # >>>>>>>>>>>>>>>>>>>> CRUD operations ends<<<<<<<<<<<<<<<<<<<<


    def DisplayLeftNode(self, Node: BinaryNode) -> None: 
        if Node is None :
            return
        Node.DisplayData()
        self.DisplayLeftNode(Node.GetLeftNode())

    def DisplayRightNode(self, Node: BinaryNode) -> None:
        if Node is None :
            return
        Node.DisplayData()
        self.DisplayRightNode(Node.GetRightNode())


userChoice = ("Enter the choice: " +
              "1. Insert Data" + 
              "2. Display Data" + 
              "3. Exit"
            )

binaryConnector: BinaryNodeConnector = BinaryNodeConnector(eval(input("Enter the data: ")))
while True :
    userInput = input(userChoice)
    match userInput :
        case "1" :
            userData = eval(input("Enter the data: "))
            binaryConnector.InsertData(userData)
        case "2" :
            binaryConnector.DisplayTreeValues()
        case "3" :
            break