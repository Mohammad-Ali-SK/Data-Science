class Node:
    def __init__(self,prev=None,item=None,next = None):
        self.prev = prev
        self.item = item
        self.next = next
class DLL:
    def __init__(self):
        self.head = None
    
    def insert_f(self,data):
        if self.head is None:
            node = Node(None,data,self.head)
            self.head = node
        else:
            node = Node(None,data,self.head)
            self.head.prev = node
            self.head = node
    
    def insert_last(self,data):
        if self.head is None:
            node = Node(None,data,None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(itr,data,None)         
    
    def delete_frist(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            
            
    def delete_last(self):
        if self.head is None:
            return 
        elif self.head.next is None:
            return None
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.prev.next = None
    
    # def delete_item(self,data):
    #     if self.head is None:
    #         return print("There are no item are here...")
    #     else:
    #         itr = self.head
    #         while itr is not None:
    #             if itr.item == data:
    #                 if itr.next is not None:
    #                     itr.next.prev = itr.prev
    #                 if itr.next is not None:
    #                     itr.prev.next = itr.next
    #                 else:
    #                     self.head = None
    #                     break
    #             itr = itr.next
    
    def delete_item(self,data):
        if self.head is None:
            return None
        else:
            itr = self.head
            while itr is not None:
                if itr.item == data:
                    if itr.next is not None:
                        itr.next.prev = itr.prev
                    if itr.next is not None:
                        itr.prev.next = itr.next
                    else:
                        self.head = None
                itr = itr.next
                
                
                
                
                
                
    def search_node(self,data):
        if self.head is None:
            return
        itr = self.head
        while itr:
            if itr.item == data:
                return itr.item
            itr = itr.next
    def insert_af_data(self,data,insdata):
        if self.head is None:
            return
        if self.head.item == data:
            node = Node(self.head,insdata,self.head.next)
            self.head.next = node
            return
        itr = self.head
        while itr:
            if itr.item == data:
                node  = Node(itr,insdata,itr.next)
                itr.next = node
                # itr.prev = node
                break
            itr = itr.next   
            
    
    
    
    
    def get_last(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    def print_forward(self):
        if self.head is None:
            return print("There are no item are here...")
        itr = self.head
        listr = ""
        while itr:
            listr += str(itr.item) + '-->'
            itr = itr.next
        print(listr)
        
    def print_backward(self):
        if self.head is None:
            return print("There are no itme are here..")
        last_node = self.get_last()
        itr = last_node
        listr = ''
        while itr:
            listr += str(itr.item) + '-->'
            itr = itr.prev
        print(listr)
        
        
if __name__ == "__main__":
    li = DLL()
    li.insert_f(10)
    li.insert_f(9)
    li.insert_f(8)
    li.insert_last(11)
    li.insert_last(12)
    li.insert_last(13)
    # li.delete_frist()
    # li.delete_last()
    # li.delete_item(12)
    li.insert_af_data(13,67)
    li.print_forward()
    print(li.search_node(11))
    # li.print_backward()