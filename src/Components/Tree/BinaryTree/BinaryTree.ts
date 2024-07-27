class BinaryTreeNode {
    LeftNode: BinaryTreeNode | null;
    Data: number;
    RightNode: BinaryTreeNode | null;
    constructor(Data: number) {
        this.LeftNode = null;
        this.Data = Data; 
        this.RightNode = null;
    }
}

class BinaryTreeConnector {
    private RootNode: BinaryTreeNode | null;
    private InsertDataHelper(Data: number, Node: BinaryTreeNode): void {
        if (Data <= Node.Data) {
            if (Node.LeftNode) {
                this.InsertDataHelper(Data, Node.LeftNode);
            }
            else {
                Node.LeftNode = new BinaryTreeNode(Data);
            }
        }
        else {
            if (Node.RightNode) {
                this.InsertDataHelper(Data, Node.RightNode);
            }
            else {
                Node.RightNode = new BinaryTreeNode(Data);
            }
        }
    }

    // Create Operation.....
    InsertData(Data: number): void {
        if (this.RootNode) {
            this.InsertDataHelper(Data, this.RootNode);
        }
        else {
            this.RootNode = new BinaryTreeNode(Data);
        }
    }

    private InOrderTraversalHelper(Output: Array<number>, Node: BinaryTreeNode | null): void {
        if (Node) {
            this.InOrderTraversalHelper(Output, Node.LeftNode);
            Output.push(Node.Data);
            this.InOrderTraversalHelper(Output, Node.RightNode);
        }
    }
    
    // Read Operation.....
    InOrderTraversal(): Array<number> {
        // left -> data -> right
        var Output: Array<number> = []
        if (this.RootNode) {
            this.InOrderTraversalHelper(Output, this.RootNode.LeftNode);
            Output.push(this.RootNode.Data);
            this.InOrderTraversalHelper(Output, this.RootNode.RightNode);
        }
        return Output;
    }


    private PreOrderTraversalHelper(Output: Array<number>, Node: BinaryTreeNode | null): void {
        if (Node) {
            Output.push(Node.Data);
            this.PreOrderTraversalHelper(Output, Node.LeftNode);
            this.PreOrderTraversalHelper(Output, Node.RightNode);
        }
    }

    // Read Operation.....
    PreOrderTraversal(): Array<number> {
        // data -> left -> right
        var Output: Array<number> = [];
        if (this.RootNode) {
            Output.push(this.RootNode.Data);
            this.PreOrderTraversalHelper(Output, this.RootNode.LeftNode);
            this.PreOrderTraversalHelper(Output, this.RootNode.RightNode);
        }
        return Output;
    }

    private PostOrderTraversalHelper(Output: Array<number>, Node: BinaryTreeNode | null): void {
        if (Node) {
            this.PostOrderTraversalHelper(Output, Node.LeftNode);
            this.PostOrderTraversalHelper(Output, Node.RightNode);
            Output.push(Node.Data);
        }
    }

    // Read Operation...
    PostOrderTraversal(): Array<number> {
        // left -> right -> data
        var Output: Array<number> = [];

        if (this.RootNode) {
            this.PostOrderTraversalHelper(Output, this.RootNode.LeftNode);
            this.PostOrderTraversalHelper(Output, this.RootNode.RightNode);
            Output.push(this.RootNode.Data);
        }
        return Output;
    }

    private FindTheMinValueHelper(Node: BinaryTreeNode): number {
        if (! Node.LeftNode) {
            return Node.Data;
        }
        return this.FindTheMinValueHelper(Node.LeftNode);
    }

    FindTheMinValue(): number | null {
        if (this.RootNode) {
            return this.FindTheMinValueHelper(this.RootNode);
        }
        return null
    }

    private FindTheMaxValueHelper(Node: BinaryTreeNode): number {
        if (! Node.RightNode){
            return Node.Data;
        }
        return this.FindTheMaxValueHelper(Node.RightNode);
    }

    FindTheMaxValue(): number | null {
        if (this.RootNode) {
            return this.FindTheMaxValueHelper(this.RootNode);
        }
        return null
    }

    private FindTheMaxNode(Node: BinaryTreeNode): BinaryTreeNode {
        if (! Node.RightNode) {
            return Node;
        }
        return this.FindTheMaxNode(Node.RightNode);
    }

    private FindTheMinNode(Node: BinaryTreeNode): BinaryTreeNode {
        if (! Node.LeftNode) {
            return Node;
        }
        return this.FindTheMinNode(Node.LeftNode);
    }

    private DeleteBinaryNodeHelper(DeleteData: number,Node: BinaryTreeNode | null): null | BinaryTreeNode {
        if (! Node) {
            return null;
        }

        if (DeleteData < Node.Data) {
            Node.LeftNode = this.DeleteBinaryNodeHelper(DeleteData, Node.LeftNode);
        }
        else if(DeleteData > Node.Data){
            Node.RightNode = this.DeleteBinaryNodeHelper(DeleteData, Node.RightNode);
        }
        else {
            if (!Node.LeftNode && !Node.RightNode) {
                return null;
            }
            else if (!Node.LeftNode) {
                return Node.RightNode;
            }
            else if (!Node.RightNode) {
                return Node.LeftNode;
            }
            else {
                var Temp_Node = this.FindTheMinNode(Node.RightNode);
                Node.Data = Temp_Node.Data;
                
                Node.RightNode = this.DeleteBinaryNodeHelper(Temp_Node.Data, Node.RightNode);
            }
        }
        return Node;
    }

    // Delete Operation....
    DeleteBinaryNode(Data: number): void {
        this.RootNode = this.DeleteBinaryNodeHelper(Data, this.RootNode);
    }
}


var binaryConnector = new BinaryTreeConnector()
binaryConnector.InsertData(10);
binaryConnector.InsertData(20);
binaryConnector.InsertData(30);
binaryConnector.InsertData(9);
binaryConnector.InsertData(8);

console.log("in-order:- ", binaryConnector.InOrderTraversal());
console.log("post-order:- ", binaryConnector.PostOrderTraversal());
console.log("pre-order:- ", binaryConnector.PreOrderTraversal());

binaryConnector.DeleteBinaryNode(9);
console.log("pre-order:- ", binaryConnector.PreOrderTraversal());


export default BinaryTreeNode;