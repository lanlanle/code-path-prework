ListNode* Solution::subtract(ListNode* A) {
    // reverse linked list 
    ListNode* ptr = A->next;
    ListNode* rev = new ListNode(A->val);
    
    while(ptr!=NULL){
        ListNode* current = new ListNode(ptr->val);
        ListNode* tmp = rev;
        rev= current;
        rev->next = tmp;
        ptr = ptr->next;
    }
    
    ListNode* fast_ptr = A;
    ListNode* aptr = A;
    ListNode* bptr = rev;
    ListNode* subtractHead = new ListNode(0);
    ListNode* subptr = subtractHead;
    while ( fast_ptr!=NULL&& fast_ptr->next!=NULL){
        int diff = bptr->val - aptr->val;
        ListNode* current =new ListNode(diff);
        subptr->next = current;
        subptr=subptr->next;
        aptr = aptr->next;
        bptr = bptr->next;
        fast_ptr = fast_ptr->next->next;
    }
    subptr->next = aptr;
    return subtractHead->next;
    
}