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
        Output: list[int] = []
        self.NodeTraversal(self.RootNode, Output, "in-order")
        return Output
    
    # READ operation.........
    def PreOrderTraversal(self) -> list[int] :
        # root -> left -> right
        Output: list[int] = []
        self.NodeTraversal(self.RootNode, Output, "pre-order")
        return Output
    
    # READ operation.........
    def PostOrderTraversal(self) -> list[int] :
        # left -> right -> root
        Output: list[int] = []
        self.NodeTraversal(self.RootNode, Output, "post-order")
        return Output


    def UpdateNodeValues(self, OldValue: int, NewValue: int) -> None :
        pass

    def DeleteNode(self, Value) -> None:
        pass
    # >>>>>>>>>>>>>>>>>>>> CRUD operations ends<<<<<<<<<<<<<<<<<<<<

    @staticmethod
    def NodeTraversal(Node: BinaryNode, Output: list, Type: str) -> None:
        if Node is None :
            return
        if Type == "in-order" :
            BinaryNodeConnector.NodeTraversal(Node.GetLeftNode(), Output, Type)
            Output.append(Node.GetData())
            BinaryNodeConnector.NodeTraversal(Node.GetRightNode(), Output, Type)
        elif Type == "pre-order" :
            # root -> left -> right
            Output.append(Node.GetData())
            BinaryNodeConnector.NodeTraversal(Node.GetLeftNode(), Output, Type)
            BinaryNodeConnector.NodeTraversal(Node.GetRightNode(), Output, Type)
        else :
            # left -> right -> root
            BinaryNodeConnector.NodeTraversal(Node.GetLeftNode(), Output, Type)
            BinaryNodeConnector.NodeTraversal(Node.GetRightNode(), Output, Type)
            Output.append(Node.GetData())


if __name__ == "__main__" :
    userChoice = ("Enter the choice: \n" +
              "insert\n" + 
              "inorder\n" + 
              "preorder\n" + 
              "postorder\n" +
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