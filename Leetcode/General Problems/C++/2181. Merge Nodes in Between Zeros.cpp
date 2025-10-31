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
    void insertAtTail(ListNode *&tail, int d)
    {
        ListNode *temp = new ListNode(d);
        tail->next = temp;
        tail = temp;
    }
    ListNode* remove(ListNode* head)
    {
        if (head == NULL)
            return NULL;
        ListNode* temp = head;
        head = head->next;
        delete temp;
        return head;
    }
    ListNode* mergeNodes(ListNode* head) {
        ListNode* temp=new ListNode(),*tail=temp;
        int sum=0;
        while(head!=NULL){
            if(head->val==0){
                insertAtTail(tail,sum);
                sum=0;
            }
            else{
                sum+=head->val;
            }
            head=head->next;
        }
        temp=remove(temp);
        temp=remove(temp);
        return temp;
    }
};