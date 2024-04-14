/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
     ListNode f;
    public boolean isPalindrome(ListNode head) {
        f=head;
        return check(head);
}
boolean check(ListNode n)
{
    if(n!=null){
        if(!check(n.next))
        {
            return false;
        }
        if(n.val!=f.val)
        {
            return false;
        }
        f=f.next;
    }
    return true;
}
}
