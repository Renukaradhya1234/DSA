from BinaryNode import *


class BinaryNodeConnector :
    def __init__(self, NewData: int) -> None:
        self.RootNode: BinaryNode = BinaryNode(NewData)

    # >>>>>>>>>>>>>>>>>>>> CRUD operations starts<<<<<<<<<<<<<<<<<<<<

    # CREATE operation........
    def InsertData(self, NewData: int) -> None :
        self.RootNode.InsertData(NewData)
    
    # READ operation..........
    def InOrderTraversal(self) -> list[int] :
        # left -> root -> right
        Ouput: list[int] = []

        def NodeTraversal(Node: BinaryNode) -> None :
            if Node is None :
                return
            NodeTraversal(Node.GetLeftNode())
            Ouput.append(Node.GetData())
            NodeTraversal(Node.GetRightNode())

        NodeTraversal(self.RootNode)
        return Ouput
    # READ operation.........
    def PreOrderTraversal(self) -> list[int] :
        # root -> left -> right
        Output: list[int] = []

        def NodeTraversal(Node: BinaryNode) -> None :
            if Node is None:
                return
            Output.append(Node.GetData())
            NodeTraversal(Node.GetLeftNode())
            NodeTraversal(Node.GetRightNode())
        NodeTraversal(self.RootNode)

        return Output
    
    # READ operation.........
    def PostOrderTraversal(self) -> list[int] :
        # left -> right -> root
        Output: list[int] = []

        def NodeTraversal(Node: BinaryNode) -> None:
            if Node is None :
                return
            NodeTraversal(Node.GetLeftNode())
            NodeTraversal(Node.GetRightNode())
            Output.append(Node.GetData())
        NodeTraversal(self.RootNode)

        return Output


    def UpdateNodeValues(self, OldValue: int, NewValue: int) -> None :
        pass

    def DeleteNode(self, Value) -> None:
        pass
    # >>>>>>>>>>>>>>>>>>>> CRUD operations ends<<<<<<<<<<<<<<<<<<<<


if __name__ == "__main__" :
    userChoice = ("Enter the choice: " +
              "insert" + 
              "inorder" + 
              "preorder" + 
              "postorder" +
              "exit"
            )

    binaryConnector: BinaryNodeConnector = BinaryNodeConnector(eval(input("Enter the data: ")))
    while True :
        userInput = input(userChoice)
        match userInput :
            case "insert" :
                userData = eval(input("Enter the data: "))
                binaryConnector.InsertData(userData)
            case "inorder" :
                print(binaryConnector.InOrderTraversal())
            case "preorder" :
                print(binaryConnector.PreOrderTraversal())
            case "postorder" :
                print(binaryConnector.PostOrderTraversal())
            case "exit" :
                break