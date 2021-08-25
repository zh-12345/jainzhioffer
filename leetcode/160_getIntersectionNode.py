from Linked_list.SingleLinkList import SingleNode, SingleLinkList
# class SingleNode():
#     def __init__(self,item):
#         self.item = item
#         self.node = None
class Solution():
    def getIntersctionNode(self,headA,headB):
        if not headA or not headB:
            return None
        lengthA = self.length(headA)
        lengthB = self.length(headB)
        p1 =headA
        p2 =headB

        while lengthA < lengthB:
            p2 =p2.next
            lengthB -= 1
        while lengthA > lengthB:
            p1 = p1.next
            lengthA -= 1
        while p1 and p2 and p1 != p2:
            p1 =p1.next
            p2=p2.next
        return p1


    def length(self,head):
        if not head:
            return 0
        cur = head
        count =0
        while cur:
            count += 1
            cur = cur.next
        return count

if __name__ == "__main__":
    h = Solution()
    li = SingleLinkList()
    node1 = SingleNode(6)
    node2 = SingleNode(7)
    li.append(2)
    li.append(3)
    li.appendSameNode(node1)
    li.appendSameNode(node2)
    # li.append(6)
    # li.append(7)
    li.add(1)
    li.travel()
    li2 = SingleLinkList()
    li2.append(5)
    li2.appendSameNode(node1)
    # li2.appendSameNode(node2)
    # li2.append(6)
    # li2.append(7)
    li2.add(4)
    li2.travel()

    result = h.getIntersctionNode(li._head, li2._head)
    print(result.item)