class Solution {
    public ListNode removeElements(ListNode h, int val) {
    ListNode n=new ListNode();
    ListNode d=n;
    while(h!=null)
    {
        if(h.val!=val)
        {
            d.next=h;
            d=d.next;
        }
        h=h.next;
        
    }
    d.next=null;
    return n.next;
    }
}
