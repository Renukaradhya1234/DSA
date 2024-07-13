from .SingleLinkedListConnector import SingleLinkedListConnector

class Starter :
    def __init__(self) :
        pass

    def Main(self) :
        Question = """
                    1. insertend
                    2. insertbegin
                    3. insertprev
                    4. insertpost
                    5. display
                    6. getdata
                    7. length
                    8. databyindex
                    9. indexbydata
                    10. update
                    11. updatebyindex
                    12. delete
                    13. deletebyindex
                    14. exit
                """

        connector = SingleLinkedListConnector(eval(input("Enter the data: ")))
        
        while True :
            print(Question) 
            UserChoice: str = input("Enter the Choice: ")

            match UserChoice :
                case "insertend" :
                    UserData: int = eval(input("Enter the Data: "))
                    connector.InsertDataToEnd(UserData)
                
                case "insertbegin" :
                    UserData: int = eval(input("Enter the Data: "))
                    connector.InsertDataToBegin()
                
                case "insertpre" :
                    UserOldData: int = eval(input("Enter the old Data: "))
                    UserNewData: int = eval(input("Enter the New Data: "))
                    connector.InsertDataToPrevNode(UserOldData, UserNewData, connector.RootNode)
                
                case "insertpost" :
                    UserOldData: int = eval(input("Enter the Old Data: "))
                    UserNewData: int = eval(input("Enter the New Data: "))
                    connector.InsertDataToNextNode(UserOldData, UserNewData)

                case "display" :
                    connector.DisplayAllData()
                
                case "getdata" :
                    print(connector.GetAllData())

                case "length" :
                    print(connector.GetLength())

                case "databyindex" :
                    UserData: int = eval(input("Enter the Index: "))
                    print(connector.GetDataByIndex(UserData))
                
                case "indexbydata" :
                    UserData: int = eval(input("Enter the Data: "))
                    print(connector.GetIndexByData(UserData))

                case "update" :
                    UserOldData: int = eval(input("Enter the Old Data: "))
                    UserNewData: int = eval(input("Enter the New Data: "))
                    connector.UpdateAllData(UserOldData, UserNewData)

                case "updatebyindex" :
                    UserData: int = eval(input("Enter the Index: "))
                    UserNewData: int = eval(input("Enter the New Data: "))
                    connector.UpdateDataByIndex(UserNewData, UserData)

                case "delete" :
                    UserData: int = eval(input("Enter the Data: "))
                    connector.DeleteNode(UserData, connector.RootNode)

                case "deletebyindex" :
                    UserData: int = eval(input("Enter the Index: "))
                    connector.DeleteNodeByIndex(UserData, connector.RootNode)

                case "exit" :
                    break

                