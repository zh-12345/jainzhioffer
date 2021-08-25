from Linked_list.SingleLinkList import SingleNode, SingleLinkList
class Solution:
    def oddEvenList(self, head) :
        if head is None or head.next is None:
            return head

#         奇节点在前，偶节点在后，
#         明确要解决的问题
#         一共有三个步骤
#        确定奇指针，偶指针， 奇指针的下一个节点是奇节点，偶指针的下一个节点是偶节点，
#         同时奇节点的最后一个节点应该要指向偶节点的第一个节点
#         最后奇指针 ，偶指针都需要移动
        odd = head
        even = head.next
        while even != None and even.next != None:
            temp = odd.next
            # 奇数的下一个节点指向偶数节点的一个节点
            odd.next = even.next
            # 此时奇数的下一个节点已经改变了，不合适转移给偶数的下一个节点，
            even.next = even.next.next
            # 奇偶节点分别再向前走一步，奇节点指向当前奇节点的末尾，偶节点还是指向了偶节点
            odd.next.next = temp

            odd = odd.next
            even = even.next
        return head


#         用两个奇偶指针分别指向奇偶节点的起始位置，
#         另外需要一个单独的指针even_head来保存偶节点的起点位置，
#         然后把奇节点的指向偶节点的下一个(一定是奇节点)，
#         此奇节点后移一步，再把偶节点指向下一个奇节点的下一个(一定是偶节点)，
#         此偶节点后移一步，以此类推直至末尾，
#         此时把分开的偶节点的链表连在奇节点的链表后即可
    def oddEvenList1(self, head):
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        even_head = head.next
        while even != None and even.next != None:
           odd.next = even.next
           odd = odd.next
           even.next = odd.next
           even = even.next

        odd.next = even_head
        return head











if __name__ == "__main__":
    h = Solution()
    li = SingleLinkList()
    # print(li.is_empty())
    # print(li.length())
    i = 0
    while i < 5:
        li.append(i + 1)
        i += 1
    li.travel()
    # h.oddEvenList(li._head)
    h.oddEvenList1(li._head)
    li.travel()