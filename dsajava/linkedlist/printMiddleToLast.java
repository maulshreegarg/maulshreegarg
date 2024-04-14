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
    public ListNode middleNode(ListNode head) {
        ListNode t=head;
        int m=0;
        while(t!=null)
        {
            m++;
            t=t.next;
        }
       m=m/2;
       int tt=0;
       while(tt<m && head!=null)
       {
        head=head.next;
        tt++;
       }
       return head;
    }
  
}
