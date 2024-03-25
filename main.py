#1

class Mylist:

    def __init__(self, numList) -> None:
        self.numList = numList

    
    def get_item(self):
        result = {}

        for num in self.numList:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1

        for k, v in result.items():
            print(f'Numbers {k} meets {v} time(s)')

    def __str__(self) -> str:
        return(f'The list {self.numList}')

My_list = Mylist([1, 1, 3, 2, 1, 3, 4])
My_list.get_item()
print(My_list)