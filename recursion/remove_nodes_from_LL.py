
def removeNodes(head):
    # base
    if head is None or head.next is None:
        return head
    
    # hypothesis
    nextNode = removeNodes(head.next)

    # induction
    if head.val < nextNode.val:
        return nextNode
    
    head.next = nextNode
    return head

def reverseList(head):
    # base case
    if head is None or head.next is None:
        return head

    # hypothesis
    last = reverseList(head.next)

    # induction
    head.next.next = head
    head.next = None

    return last


