#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:05:54 2023

@author: domin
"""

def main():
    print("Matrix Calculator")
    arr = [[1, 2, 3, 4], [5, 6, 7], [9, 8, 7, 6]]
    printarr(arr)
    print("\n")
    fillUnique(arr)
    printarr(arr)
    
#fill for multivariable functions
def fillUnique(arr):
    maxsize = len(arr[0])
    for row in arr:
        if len(row) > maxsize:
            maxsize = len(row)
    for row in arr:
        while len(row) < maxsize:
            row.append(0)
            
#splits input string into a list of values, operators, and variables to determine composition of function 
#   var next to any var or val is implied multiplication, 
#   multi and divide combines terms, 
#   exponent seperates variables, 
#   everything past "=" gets inverted so function = 0, 
#   add and subtract adds seperates terms (subtract adds opposite)          
def getUnique(function):
    val = ''
    unique = []
    function = function.replace(" ", "")
    for char in function:
        if isDigit(char):
            val += char
        elif isOperator(char):
            if val != '':
                unique.append(val)
            unique.append(char)
            val = ''
        elif isVar(char):
            if val != '':
                unique.append(val)
            unique.append(char)
            val = ''
    if val != '':
        unique.append(val)
    return unique
                
def buildFunction(unique):
    for val in unique:
        print(val)
        
def isDigit(char):
    if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        return True
               
#checks if val is operator "=, +, -, ^, /, *" optional for trig, calc, logs, or other functions
def isOperator(char):
    operators = ["+", "-", "*", "/", "^", "="]
    if char in operators:
        return True
    return False

#is val a variable, gets used if optional operators are implemented and differentiation becomes nessesary
def isVar(char):
    return True
            
#fill for 1 variable functions (2x^2 + 5x + 1)
def fillX():
    return
            
            
def printarr(arr):
    for row in arr:
        print(row)

arr = getUnique("x^2 + z = 10 + 3^3")
buildFunction(arr)
#main()