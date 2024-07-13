from .SingleLinkedList import SingleLinkedNode


class SingleLinkedListConnector :
    def __init__(self, Data) -> None:
        self.RootNode = SingleLinkedNode(Data)

    # >>>>>>>>>>>>>>>> CRUD Operations <<<<<<<<<<<<<<<<<<<<
    
    # Create Operation.........
    def InsertDataToEnd(self, NewData: int) -> None :
        self.RootNode.InsertDataToEnd(NewData)

    # Create Operation.........
    def InsertDataToBegin(self, NewData: int) -> None :
        NewNode: SingleLinkedNode = SingleLinkedNode(NewData)
        NewNode.UpdateNextNode(self.RootNode)

        self.RootNode = NewNode
    
    # Create Operation......
    def InsertDataToPrevNode(self, OldData: int, NewData: int, Node: SingleLinkedNode, PrevNode: SingleLinkedNode | None = None) :
        # first call will be newdata, rootnode, prevnode = none
        if Node is None :
            return 
        if Node.GetData() == OldData :
            NewNode: SingleLinkedNode = SingleLinkedNode(NewData)
            if  PrevNode is None:
                # prevnode is none means, current node must be root node.....
                NewNode.UpdateNextNode(Node)
                self.RootNode = NewNode
            else :
                # prevnode -> nextnode
                # prevnode -> newnode -> nextnode
                NewNode.UpdateNextNode(PrevNode.GetNextNode())
                PrevNode.UpdateNextNode(NewNode)
        self.InsertDataToPrevNode(OldData, NewData, Node.GetNextNode(), Node)

    # Create Operation....
    def InsertDataToNextNode(self, OldData: int, NewData: int) :
        self.RootNode.InsertDataToAfterNode(OldData, NewData)

    # Read Operation.......
    def DisplayAllData(self) -> None:
        self.NodeTraversal(self.RootNode, "display")

    # Update Operation.....
    def UpdateAllData(self, OldData: int, NewData: int) -> None :
        self.NodeTraversal(self.RootNode, "update", OldData, NewData)

    # delete Operation....
    def DeleteNode(self, Value) -> None :
        if self.RootNode.GetData() == Value :
            self.RootNode = self.RootNode.GetNextNode()
        else :
            Node: SingleLinkedNode | None = self.GetNodeByValue(self.RootNode, Value, "before")

            if Node is not None :
                Node.UpdateNextNode(Node.GetNextNode().GetNextNode())

    # Node Helper......
    @staticmethod
    def NodeTraversal(Node: SingleLinkedNode, Operation: str, OldData = None, NewData = None) -> None :
        if Node is None :
            return 
        if Operation == "display" :
            print(Node.GetData())
        elif Operation == "update" :
            if OldData == Node.GetData() :
                Node.UpdateData(NewData)
        SingleLinkedListConnector.NodeTraversal(Node.GetNextNode(), Operation, OldData, NewData)

    # Node Helper....
    @staticmethod
    def GetNodeByValue(Node: SingleLinkedNode, Value: int, Type = "current") :
        if Node is None :
            return None
        if Node.GetData() == Value :
            if Type == "current" :
                return Node
            elif Type == "after" :
                return Node.GetNextNode()
        else :
            NextNode: SingleLinkedNode | None = Node.GetNextNode()
            if Type == "before" and NextNode and NextNode.GetData() == Value :
                return Node
        return SingleLinkedListConnector.GetNodeByValue(Node.GetNextNode(), Value, Type)