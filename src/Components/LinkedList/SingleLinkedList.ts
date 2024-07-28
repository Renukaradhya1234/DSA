class SingleLinkedNode {
    NextNode: SingleLinkedNode | null;
    Data: number;
    constructor(Data: number) {
        this.Data = Data;
    }
}


class SingleLinkedNodeConnector {
    private RootNode: SingleLinkedNode | null;

    private static InsertDataHelper(Data: number, Node: SingleLinkedNode): void {
        if (!Node.NextNode) {
            Node.NextNode = new SingleLinkedNode(Data);
            return;
        }
        this.InsertDataHelper(Data, Node.NextNode);
    }

    // Create Operation....
    InsertData(Data: number): void {
        if (this.RootNode) {
            SingleLinkedNodeConnector.InsertDataHelper(Data, this.RootNode);
        }
        else {
            this.RootNode = new SingleLinkedNode(Data);
        }
    }

    private static ReadAllDataHelper(Output: Array<number>, Node: SingleLinkedNode | null): void {
        if (Node) {
            Output.push(Node.Data);
            this.ReadAllDataHelper(Output, Node.NextNode);
        }
    }
    // Read Operation....
    ReadAllData(): Array<number> {
        var Output: Array<number> = [];

        if (this.RootNode) {
            SingleLinkedNodeConnector.ReadAllDataHelper(Output, this.RootNode);
        }
        return Output;
    }

    private static UpdateAllDataHelper(OldData: number, NewData: number, Node: SingleLinkedNode | null): void {
        if (Node) {
            if (Node.Data === OldData) {
                Node.Data = NewData;
            }
            this.UpdateAllDataHelper(OldData, NewData, Node.NextNode);
        }
    }

    // Update Operation.....
    UpdateAllData(OldData: number, NewData: number): void {
        if (this.RootNode) {
            SingleLinkedNodeConnector.UpdateAllDataHelper(OldData, NewData, this.RootNode);
        }
    }

    private static GetLengthHelper(Count: number, Node: SingleLinkedNode | null): number {
        if (Node) {
            return this.GetLengthHelper(Count + 1, Node.NextNode);
        }
        return Count + 1;
    }

    GetLength(): number {
        var Count = 0

        if (this.RootNode) {
            Count = SingleLinkedNodeConnector.GetLengthHelper(Count, this.RootNode);
        }

        return Count;
    }

    private static DeleteNodeHelper(Data: number, Node: SingleLinkedNode | null): SingleLinkedNode | null {
        if (! Node) {
            return Node;
        }

        if (Node.Data === Data) {
            return Node.NextNode;
        }

        Node.NextNode = this.DeleteNodeHelper(Data, Node.NextNode);
        return Node;
    }

    // Delete Operation...
    DeleteNode(Data: number): void {
        this.RootNode = SingleLinkedNodeConnector.DeleteNodeHelper(Data, this.RootNode);
    }

    private static GetTheLengthHelper(Count: number, Node: SingleLinkedNode | null): number {
        if (Node) {
            return SingleLinkedNodeConnector.GetTheLengthHelper(Count + 1, Node.NextNode);
        }
        return Count;
    }

    GetTheLength(): number {
        var Count: number = 0;
        if (this.RootNode) {
            Count = SingleLinkedNodeConnector.GetTheLengthHelper(Count, this.RootNode);
        }
        return Count;
    }


    private static IsPresentHelper(Data: number, Node: SingleLinkedNode | null): boolean {
        if (Node) {
            if (Node.Data === Data) {
                return true;
            }
            return SingleLinkedNodeConnector.IsPresentHelper(Data, Node.NextNode);
        }
        return false;
    }

    IsPresent(Data: number): boolean {
        var Present: boolean = false;

        if (this.RootNode){
            Present = SingleLinkedNodeConnector.IsPresentHelper(Data, this.RootNode);
        }
        return Present;
    }
}

var SingleConnector = new SingleLinkedNodeConnector();
SingleConnector.InsertData(10);
SingleConnector.InsertData(20);
SingleConnector.InsertData(30);
SingleConnector.InsertData(40);
SingleConnector.InsertData(50);

console.log("Data:- ", SingleConnector.ReadAllData());
SingleConnector.UpdateAllData(10, 50);
console.log("Data:- ", SingleConnector.ReadAllData());
SingleConnector.DeleteNode(30);
console.log("Data:- ", SingleConnector.ReadAllData());

