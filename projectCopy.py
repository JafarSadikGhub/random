# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:43:59 2018

@author: Asus
"""


try:
    
    input = open("C:/Users/Asus/Desktop/CSE332Proj3ct/input.txt", "r")
    output = open("C:/Users/Asus/Desktop/CSE332Proj3ct/output.txt", "a")
    for line in input:
        inst=line.replace(',','\t')
        inst = inst.split()
        for single_inst in inst:
            if single_inst == "ADD":
                output.write("0000 ")
            elif single_inst == "SUB":
                output.write("0001 ")
            elif single_inst == "AND":
                output.write("0010 ")
            elif single_inst == "OR":
                output.write("0011 ")
            elif single_inst == "ANDi":
                output.write("0100 ")
            elif single_inst == "ORi":
                output.write("0101 ")
            elif single_inst == "ADDi":
                output.write("0110 ")
            elif single_inst == "XOR":
                output.write("0111 ")
            elif single_inst == "NOR":
                output.write("1100 ")
            elif single_inst == "lui":
                output.write("1101 ")
            elif single_inst == "lb":
                output.write("1110 ")
            elif single_inst == "sb":
                output.write("1110 ")    
            elif single_inst == "sll":    #r-format
                output.write("1000 ")     
            elif single_inst == "srl":    #r-format
                output.write("1001 ")
            elif single_inst == "lw":     #i-format
                output.write("1010 ")
            elif single_inst =="sw":      #i-format
                output.write("1011 ")
            elif single_inst == "$rd":
                output.write("01 ")
            elif single_inst == "$rs":
                output.write("10 ")
            elif single_inst == "$rt":
                output.write("11 ")
            elif single_inst == "0":
                output.write("00 ")
            elif single_inst =="1":
                output.write("01 ")
            elif single_inst =="2":
                output.write("10 ")
            elif single_inst =="3":
                output.write("11 ")
        
        output.write('\n')
    output.close()
    input.close()
    input = open("C:/Users/Asus/Desktop/CSE332Proj3ct/input.txt", "r")
    result = open("C:/Users/Asus/Desktop/CSE332Proj3ct/output.txt", "r")
    asmblyCode = input.read()
    machineCode = result.read()
    print("Assembly code:\n" + asmblyCode+ "\n\nMachine Code:\n" +machineCode)
finally:
    input.close()
    output.close()    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        