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
    public int sizeof(ListNode head) {
        ListNode temp = head;
        int count=0;
        while(temp!=null) {
            temp = temp.next;
            count++;
        }
        return count;
    }
    public ListNode reverseList(ListNode head) {
        int size = sizeof(head);
        int[] arr = new int[size];
        int i = 0;
        ListNode temp = head;
        while(temp!=null) {
            arr[i++] = temp.val;
            temp = temp.next;
        }
        ListNode ptr = head;
        i--;
        while(ptr!=null) {
            ptr.val = arr[i--];
            ptr = ptr.next;  
        }
        return head;
    }
}