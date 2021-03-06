#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 01:23:50 2019

@author: y56
"""

class Node:
    def __init__(self, x):
        self.data = x
        self.next  =  None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, x):
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data,  "-> " , end = '')
            curr = curr.next
        print("null")
    def reverse(self, node):
        
        

        
#        if node.next == None:
#            self.head = node
#            return
#        self.reverse(node.next)
#        temp = node.next
#        temp.next = node
#        node.next = None
        
        
        print("head is", self.head.data)
        
        temp = self.head
        while temp:
            print(temp.data,  "-> " , end = '')
            temp = temp.next
        print("null")
        
        print("data =", node.data, end = '')
        if node == None or node.next == None: 
            # node == None is for empty l-lists
            # node.next == None is for non-empty l-lists, it is 
            print("   point of bouncing-back, bottum of recurrence")
            return node
        print("   one layer deeper")
        headOfRest = self.reverse(node.next)
        print("one layer back")
        print("headOfRest is", headOfRest.data)
        print("head       is", self.head.data)
        
        temp = headOfRest
        while temp:
            print(temp.data,  "-> " , end = '')
            temp = temp.next
        print("null")
        
        print("----")

        node.next.next = node    
        node.next = None
        
        temp = headOfRest
        while temp:
            print(temp.data,  "-> " , end = '')
            temp = temp.next
        print("null")
        
        return headOfRest
            
myLinkedList = LinkedList()
myLinkedList.push(1)
myLinkedList.push(2)
myLinkedList.push(3)
myLinkedList.push(4)
myLinkedList.printList()
#myLinkedList.reverse(myLinkedList.head)
myLinkedList.head = myLinkedList.reverse(myLinkedList.head);
myLinkedList.printList()
