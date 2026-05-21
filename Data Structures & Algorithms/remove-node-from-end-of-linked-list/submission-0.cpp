/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int ListSize(ListNode* head) {
        ListNode* temp = head;
        int count=0;
        while(temp!=NULL) {
            count++;
            temp = temp->next;
        }
        return count;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int size = ListSize(head);
        int index = size-n;
        int count = 0;
        ListNode* temp = head;
        cout << index << "-" << count << "-" << size;
        if (index>0) {
            while(temp!=NULL) {
                
                if (index==count && count!=size-1) {
                    ListNode* nextElem = temp->next;
                    temp->val = nextElem->val;
                    temp->next = nextElem->next;
                } 
                if (index==count+1 && count+1==size-1){
                    temp->next = nullptr;
                    
                    break;
                }
                count++;
                temp = temp->next;
            }
        } else if (index==0 && size==1) {
            ListNode* lst = NULL;
            return lst;
        } else if (index==0 && size>1) {
            head = head->next;
        }
       
    return head;
    }
};