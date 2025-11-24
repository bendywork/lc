class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA, pB = headA, headB

        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA


if __name__ == '__main__':
    s = Solution()

    # listA = [1,9,1,2,4]
    # listB = [3,2,4]
    # intersectVal = 2  ---> 即节点值为 2 的位置是交点

    # 构造链表 A 的前三个独立节点 [1,9,1]
    A1 = ListNode(1)
    A2 = ListNode(9)
    A3 = ListNode(1)
    A1.next = A2
    A2.next = A3

    # 构造链表 B 的第一个节点 [3]
    B1 = ListNode(3)

    # 构造公共部分 [2,4]
    C1 = ListNode(2)
    C2 = ListNode(4)
    C1.next = C2

    # 将公共部分接到 A 和 B
    A3.next = C1
    B1.next = C1

    # 传入 A 和 B 的头节点
    res = s.getIntersectionNode(A1, B1)
    print(res.val if res else None)
