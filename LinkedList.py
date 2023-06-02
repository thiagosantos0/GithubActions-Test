from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None


    def push(self, new_data):
        '''
            Adiciona um nó no início da lista.
        '''
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        '''
            Adiciona um nó no final da lista
        '''
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node
    
    def getCount(self):
        '''
            Retorna o número de itens na lista
        '''
        temp = self.head
        count = 0

        while(temp):
            count += 1
            temp = temp.next

        return count

    def reverse(self):
        '''
            Retorna a lista encadeada invertida
        '''
        prev = None
        current = self.head
        
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def search(self, x):
        '''
            Verifica se o elemento 'x' está presente na lista
        '''
        temp = self.head
        while(temp):
            if(temp.data == x):
                return True
            temp = temp.next
        return False

    def delete(self, x):
        '''
            Deleta o elemento 'x' da lista se ele estiver presente.
        '''
        temp = self.head
        prev = temp 

        if(temp.data == x):
            self.head = temp.next
            return temp.data

        while(temp):
            if(temp.data == x):
                break
            prev = temp
            temp = temp.next
        
        if(not temp):
            return

        prev.next = temp.next
        return temp.data
    
    def getListValues(self):
        list_values = []
        temp = self.head
        while(temp):
            list_values.append(temp.data)
            temp = temp.next
        return list_values

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print("\n")



if __name__ == '__main__':
    llist = LinkedList()
    llist.push(6)
    llist.push(7)
    llist.push(8)
    llist.printList()
    llist.append(10)
    llist.append(11)
    llist.append(12)
    llist.printList()

    llist.reverse()
    llist.printList()

    print(f"Tamanho: {llist.getCount()}")
    print(f"13 Está presente na lista: {llist.search(13)}")
    print(f"8 Está presente na lista: {llist.search(8)}")

    llist.delete(6)
    llist.printList()


