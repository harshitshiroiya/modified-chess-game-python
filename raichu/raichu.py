
#!/usr/bin/env python
# coding: utf-8



#
# raichu.py : Play the game of Raichu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
# Harshit Shiroiya - hshiroiy@iu.edu, Rutul Patel - rpp@iu.edu, Abhay Rajde - abrajde@iu.edu
#
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import os
import time
import numpy as np
import copy


def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))




def list_to_string(s,N):
    l_to_s = ""
    for i in range(0,N):
        for j in range(0,N):
             l_to_s+=s[i][j]
    return l_to_s


#referred from https://github.com/Chirag-Galani/B551-Elements-Of-Artificial-Intelligence/blob/master/Assignment%202/part1/pichu.py

def checkMove(board,player,curr_piece_x,curr_piece_y,next_x,next_y):
    
    if board[next_x][next_y]!=".":
        if (player == "w" and board[next_x][next_y] in "wW@") or (player == "b" and board[next_x][next_y] in "bB$"):
            return 0
        if (board[curr_piece_x][curr_piece_y]=="w" and board[next_x][next_y] in "b") or (board[curr_piece_x][curr_piece_y] == "b" and board[next_x][next_y] in "w"):
            return 2
        if (board[curr_piece_x][curr_piece_y] == "w" and board[next_x][next_y] in "B$") or (board[curr_piece_x][curr_piece_y] == "b" and board[next_x][next_y] in "W@"):
            return 0
        if (board[curr_piece_x][curr_piece_y] == "W" and board[next_x][next_y] in "bB" ) or (board[curr_piece_x][curr_piece_y] == "B" and board[next_x][next_y] in "wW"):
            return 2
        if (board[curr_piece_x][curr_piece_y] == "W" and board[next_x][next_y] in "$") or (board[curr_piece_x][curr_piece_y] == "B" and board[next_x][next_y] in "@"):
            return 0        
        if (board[curr_piece_x][curr_piece_y] == "@" and board[next_x][next_y] in "bB$") or (board[curr_piece_x][curr_piece_y] == "$" and board[next_x][next_y] in "wW@" ):
            return 2        
    return 1

#For Traversing of each element referred from Part 1 and Part 2 from A0

def pichu(board,player,N):
    pichu_list=[]
    x = N
    x1 = 0
    y = N
    y1 = 0
    for i in range (N):
        for j in range (N):
            position = board[i][j]
            col=0
            row=0
            if player=='w':
                if position == 'w':
                    
                    col = j+1
                    row = i+1
                    count = 0
                    while col<y and row<x:
                        piece_move = checkMove(board,player,i,j,row,col)
                        if count < 1:
                            if piece_move == 1 and row < x-1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col] = position
                                pichu_list.append(new_board)
                            if piece_move == 1 and row == x-1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]="@"
                                pichu_list.append(new_board)
                            if piece_move == 0:
                                break
                        
                            if piece_move == 2 and col < x-1 and row < x-2 :
                                if(board[row + 1][col+1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row += 1
                                    col += 1
                                    new_board[row][col] = position
                                    pichu_list.append(new_board) 
                                break
                            if piece_move == 2 and col < y-1 and row == x-2 :
                                if(board[row + 1][col+1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row += 1
                                    col += 1
                                    new_board[row][col] = "@"
                                    pichu_list.append(new_board) 
                                break
                        count += 1
                        col += 1
                        row += 1
                   
                
                    col = j-1
                    row = i+1
                    count=0
                    while col >= y1 and row < x:
                        piece_move = checkMove(board,player,i,j,row,col)
                        if count < 1:
                            if piece_move == 1 and row < x-1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col] = position
                                pichu_list.append(new_board)
                            if piece_move==1 and row == x-1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]="@"
                                pichu_list.append(new_board)
                            if piece_move== 0:
                                break
    
                            if piece_move==2 and col > 0 and row < x-2:
                                if(board[row+1][col-1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row += 1
                                    col -= 1
                                    new_board[row][col] = position
                                    pichu_list.append(new_board)
                                break
                            elif piece_move == 2 and col > 0 and row == x-2:
                                if(board[row+1][col-1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row += 1
                                    col -= 1
                                    new_board[row][col]="@"
                                    pichu_list.append(new_board)
                                break
                        count+=1       
                        col -= 1
                        row += 1
                        
            if (player=='b'):
                if position == 'b':
                    
                    
                    col = j+1
                    row = i-1
                    count = 0 
                    while col < y and row >= x1:
                        piece_move = checkMove(board,player,i,j,row,col)
                        if count < 1:
                            if piece_move==1 and row > 0:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col] = position
                                pichu_list.append(new_board)
                            if piece_move==1 and row == 0:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]="$"
                                pichu_list.append(new_board)
                            if piece_move==0:
                                break
                    
                            if piece_move==2 and col < y-1 and row>1:
                                if(board[row-1][col+1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row-=1
                                    col+=1
                                    new_board[row][col] = position
                                    pichu_list.append(new_board)
                                break
                            if piece_move==2 and col < y-1 and row == 1:
                                if(board[row-1][col+1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row -= 1
                                    col += 1
                                    new_board[row][col]="$"
                                    pichu_list.append(new_board)
                                break
                        count += 1       
                        col += 1
                        row-=1
                    
                    
                    
                    col = j-1
                    row = i-1
                    count = 0
                    while col >= y1 and row >= x1:
                        piece_move = checkMove(board,player,i,j,row,col)
                        if count < 1:
                            if piece_move == 1 and row > 0:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col] = position
                                pichu_list.append(new_board)
                            if piece_move==1 and row==0:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]="$"
                                pichu_list.append(new_board)
                            if piece_move==0:
                                break
                        
                            if piece_move == 2 and col > 0 and row > 1:
                                if(board[row-1][col-1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row -= 1
                                    col -= 1
                                    new_board[row][col] = position
                                    pichu_list.append(new_board) 
                                break
                            if piece_move == 2 and col > 0 and row == 1:
                                if(board[row-1][col-1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row -= 1
                                    col -= 1
                                    new_board[row][col]="$"
                                    pichu_list.append(new_board) 
                                break
                        count += 1
                        col -= 1
                        row -= 1

    return pichu_list                







def pikachu(board,player,N):
    pikachu_list=[]
    x = N
    x1 = 0
    y = N
    y1 = 0

    for i in range (N):
        for j in range (N):
            position = board[i][j]
            col=0
            row=0
            if player == 'w':
                if position == 'W':
                    row = i+1
                    count = 0
                    while row < x:
                        piece_move = checkMove(board,player,i,j,row,j)
                        if count < 2:
                            if piece_move == 1 and row < x-1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][j]=position
                                pikachu_list.append(new_board)
                            if piece_move == 1 and row == x-1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][j]="@"
                                pikachu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move==2 and row < x-2:
                                if(board[row+1][j]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][j]="."
                                    row += 1
                                    new_board[row][j]=position
                                    pikachu_list.append(new_board) 
                                break
                            if piece_move == 2 and row == x-2:
                                if(board[row+1][j]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][j]="."
                                    row += 1
                                    new_board[row][j]="@"
                                    pikachu_list.append(new_board) 
                                break
                        count+=1
                        row += 1



                    col = j-1
                    count=0
                    while col>=y1:
                        piece_move = checkMove(board,player,i,j,i,col)
                        if count < 2:
                            if piece_move == 1 and row < x-1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[i][col]=position
                                pikachu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move==2 and col>0:
                                if(board[i][col-1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[i][col]="."
                                    col -= 1
                                    new_board[i][col]=position
                                    pikachu_list.append(new_board)
                                break
                        count+=1      
                        col -= 1



                    col = j+1
                    count=0
                    while col < y1:
                        piece_move = checkMove(board,player,i,j,i,col)
                        if count<2:
                            if piece_move==1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[i][col]=position
                                pikachu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move==2 and col < y-1:
                                if(board[i][col+1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[i][col]="."
                                    col += 1
                                    new_board[i][col]=position
                                    pikachu_list.append(new_board)    
                                break
                        count += 1
                        col += 1 

            if player == 'b':
                if position == 'B':
               
                    col = j-1
                    count = 0
                    while col >= y1:
                        piece_move = checkMove(board,player,i,j,i,col)
                        if count < 2:    
                            if piece_move==1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[i][col]=position
                                pikachu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move==2 and col>0:
                                if(board[i][col-1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[i][col]="."
                                    col -= 1
                                    new_board[i][col]=position
                                    pikachu_list.append(new_board) 
                                break
                        count += 1      
                        col -= 1



                    col = j+1
                    count=0
                    while col < y:
                        piece_move = checkMove(board,player,i,j,i,col)
                        if count < 2:
                            if piece_move==1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[i][col]=position
                                pikachu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move == 2 and col < y-1:
                                if(board[i][col+1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[i][col]="."
                                    col += 1
                                    new_board[i][col]=position
                                    pikachu_list.append(new_board)   
                                break
                        count += 1
                        col += 1
                    
                    row = i-1
                    count=0
                    while row > x1:
                        piece_move = checkMove(board,player,i,j,row,j)
                        if count < 2:
                            if piece_move==1 and row>0:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][j]=position
                                pikachu_list.append(new_board)
                            if piece_move==1 and row == 0:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][j]="$"
                                pikachu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move==2 and row>1:
                                if(board[row-1][j]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][j]="."
                                    row-=1
                                    new_board[row][j]=position
                                    pikachu_list.append(new_board)
                                break
                            if piece_move==2 and row==1:
                                if(board[row-1][j]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][j]="."
                                    row -= 1
                                    new_board[row][j]="$"
                                    pikachu_list.append(new_board) 
                                break
                        count+=1
                        row-=1
    

    return pikachu_list                    





def raichu(board,player,N):
    raichu_list=[]
    x = N
    x1 = 0
    y = N
    y1 = 0

    for i in range (N):
        for j in range (N):
            position = board[i][j]
            col=0
            row=0
            if player == 'w':
                if position == '@':


                    row = i-1
                    while row > x1:
                        piece_move = checkMove(board,player,i,j,row,j)
                        if piece_move == 1:
                            new_board = copy.deepcopy(board)
                            new_board[i][j]="."
                            new_board[row][j]=position
                            raichu_list.append(new_board)
                        if piece_move==0:
                            break
                        if piece_move==2 and row>0:
                            if(board[row-1][j]=="."):
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][j]="."
                                row -= 1
                                new_board[row][j]=position
                                raichu_list.append(new_board)
                            break
                        row -= 1   


                    row = i+1
                    while row < x:
                        piece_move = checkMove(board,player,i,j,row,j)
                        if piece_move==1:
                            new_board = copy.deepcopy(board)
                            new_board[i][j]="."
                            new_board[row][j]=position
                            raichu_list.append(new_board)
                        if piece_move==0:
                            break
                        if piece_move==2 and row < x-1:
                            if(board[row+1][j]=="."):
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][j]="."
                                row+=1
                                new_board[row][j]=position
                                raichu_list.append(new_board)
                            break
                        row+=1


                    col = j-1
                    while col>=y1:
                        piece_move = checkMove(board,player,i,j,i,col)
                        if piece_move==1:
                            new_board = copy.deepcopy(board)
                            new_board[i][j]="."
                            new_board[i][col]=position
                            raichu_list.append(new_board)
                        if piece_move==0:
                            break
                        if piece_move==2 and col > 0:
                            if(board[i][col-1]=="."):
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[i][col]="."
                                col-=1
                                new_board[i][col]=position
                                raichu_list.append(new_board)   
                            break
                        col-=1


                    col = j+1
                    while col < y:
                        piece_move = checkMove(board,player,i,j,i,col)
                        if piece_move==1:
                            new_board = copy.deepcopy(board)
                            new_board[i][j]="."
                            new_board[i][col]=position
                            raichu_list.append(new_board)
                        if piece_move==0:
                            break
                        if piece_move == 2 and col < y-1:
                            if(board[i][col+1]=="."):
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[i][col]="."
                                col+=1
                                new_board[i][col]=position
                                raichu_list.append(new_board)   
                            break
                        col += 1
                    #upper diagonal right
                    col = j+1
                    row = i-1
                    while col < y and row >= x1:
                        piece_move = checkMove(board,player,i,j,row,col)
                        if piece_move==1:
                            new_board = copy.deepcopy(board)
                            new_board[i][j]="."
                            new_board[row][col]=position
                            raichu_list.append(new_board)
                        if piece_move==0:
                            break
                        if piece_move==2 and col < y-1 and row > 0:
                            if(board[row-1][col+1]=="."):
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]="."
                                row-=1
                                col+=1
                                new_board[row][col]=position
                                raichu_list.append(new_board)  
                            break
                        col += 1
                        row -= 1

                    col = j-1
                    row = i-1
                    while col >= y1 and row >= x1:
                        piece_move = checkMove(board,player,i,j,row,col)

                        if piece_move==1:
                            new_board = copy.deepcopy(board)
                            new_board[i][j]="."
                            new_board[row][col]=position
                            raichu_list.append(new_board)
                        if piece_move==0:
                            break
                        if piece_move==2 and col > 0 and row > 0:
                            if(board[row-1][col-1] == "."):
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]="."
                                row -= 1
                                col -= 1
                                new_board[row][col]=position
                                raichu_list.append(new_board) 
                            break
                        row -= 1
                        col -= 1


                    col = j+1
                    row = i+1
                    while col < y and row < x:
                        piece_move = checkMove(board,player,i,j,row,col)
                        if piece_move==1:
                            new_board = copy.deepcopy(board)
                            new_board[i][j]="."
                            new_board[row][col]=position
                            raichu_list.append(new_board)
                        if piece_move==0:
                            break
                        if piece_move == 2 and col < y-1 and row < x-1:
                            if(board[row+1][col+1]=="."):
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]="."
                                row += 1
                                col += 1
                                new_board[row][col]=position
                                raichu_list.append(new_board)   
                            break
                        col += 1
                        row += 1


                    col = j-1
                    row = i+1
                    while col >= y1 and row < x:
                        piece_move = checkMove(board,player,i,j,row,col)

                        if piece_move==1:
                            new_board = copy.deepcopy(board)
                            new_board[i][j]="."
                            new_board[row][col]=position
                            raichu_list.append(new_board)
                        if piece_move== 0:
                            break
                        if piece_move==2 and col >0 and col < N-1:
                            if(board[row+1][col-1]=="."):
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]="."
                                row += 1
                                col -= 1
                                new_board[row][col] = position
                                raichu_list.append(new_board)
                            break

                        col -= 1
                        row += 1



                if player == 'b':
                    if position == '$':

                        row = i-1
                        while row > x1:
                            piece_move = checkMove(board,player,i,j,row,j)
                            if piece_move == 1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][j]=position
                                raichu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move==2 and row>0:
                                if(board[row-1][j]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][j]="."
                                    row -= 1
                                    new_board[row][j]=position
                                    raichu_list.append(new_board)
                                break
                            row -= 1   


                        row = i+1
                        while row < x:
                            piece_move = checkMove(board,player,i,j,row,j)
                            if piece_move==1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][j]=position
                                raichu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move==2 and row < N-1:
                                if(board[row+1][j]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][j]="."
                                    row+=1
                                    new_board[row][j]=position
                                    raichu_list.append(new_board)
                                break
                            row+=1


                        col = j-1
                        while col >= y1:
                            piece_move = checkMove(board,player,i,j,i,col)
                            if piece_move==1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[i][col]=position
                                raichu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move==2 and col > 0:
                                if(board[i][col-1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[i][col]="."
                                    col-=1
                                    new_board[i][col]=position
                                    raichu_list.append(new_board)   
                                break
                            col -= 1

                        col = j+1
                        while col < y:
                            piece_move = checkMove(board,player,i,j,i,col)
                            if piece_move==1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[i][col]=position
                                raichu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move==2 and col < y-1:
                                if(board[i][col+1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[i][col]="."
                                    col+=1
                                    new_board[i][col]=position
                                    raichu_list.append(new_board)   
                                break
                            col += 1
                        #upper diagonal right
                        col = j+1
                        row = i-1
                        while col < y and row >= x1:
                            piece_move = checkMove(board,player,i,j,row,col)
                            if piece_move==1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]=position
                                raichu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move==2 and col < y-1 and row > 0:
                                if(board[row-1][col+1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row-=1
                                    col+=1
                                    new_board[row][col]=position
                                    raichu_list.append(new_board)  
                                break
                            col += 1
                            row -= 1


                        col = j-1
                        row = i-1
                        while col >= y1 and row >= x1:
                            piece_move = checkMove(board,player,i,j,row,col)

                            if piece_move==1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]=position
                                raichu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move == 2 and col > 0 and row > 0:
                                if(board[row-1][col-1] == "."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row -= 1
                                    col -= 1
                                    new_board[row][col]=position
                                    raichu_list.append(new_board) 
                                    break
                            row -= 1
                            col -= 1


                        col = j+1
                        row = i+1
                        while col < y and row < x:
                            piece_move = checkMove(board,player,i,j,row,col)
                            if piece_move==1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]=position
                                raichu_list.append(new_board)
                            if piece_move==0:
                                break
                            if piece_move == 2 and col < y-1 and row < x-1:
                                if(board[row+1][col+1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row += 1
                                    col += 1
                                    new_board[row][col]=position
                                    raichu_list.append(new_board)   
                                    break
                            col += 1
                            row += 1


                        col = j-1
                        row = i+1
                        while col >= y1 and row < x:
                            piece_move = checkMove(board,player,i,j,row,col)

                            if piece_move==1:
                                new_board = copy.deepcopy(board)
                                new_board[i][j]="."
                                new_board[row][col]=position
                                raichu_list.append(new_board)
                            if piece_move== 0:
                                break
                            if piece_move==2 and col >0 and col < y-1:
                                if(board[row+1][col-1]=="."):
                                    new_board = copy.deepcopy(board)
                                    new_board[i][j]="."
                                    new_board[row][col]="."
                                    row += 1
                                    col -= 1
                                    new_board[row][col] = position
                                    raichu_list.append(new_board)
                                    break

                            col -= 1
                            row += 1
                        
                        
                else:
                    continue
                    
    return raichu_list





#referred code from https://github.com/BharathaAravind/Artificial-Intelligence-B551/blob/master/Assignment3/part1/pichu.py
def successor(board,player,N):
    successor_list = []
    if player == 'w':
        for i in pichu(board,'w',N):
            score = cost_evaluation(i,'w',N)
            successor_list.append(i)
        for i in pikachu(board,'w',N):
            score = cost_evaluation(i,'w',N)
            successor_list.append(i)
        for i in raichu(board,'w',N):
            score = cost_evaluation(i,'w',N)
            successor_list.append(i)

    else:
        for i in pichu(board,'b',N):
            score = cost_evaluation(i,'b',N)
            successor_list.append(i)
        for i in pikachu(board,'b',N):
            score = cost_evaluation(i,'b',N)
            successor_list.append(i)
        for i in raichu(board,'b',N):
            score = cost_evaluation(i,'b',N)
            successor_list.append(i)
    return successor_list




def cost_evaluation(Board,player,N):    
    s=0       # we are initializing s as 0

    if player == 'w' or player == 'W':    
        for i in range(N):
            for j in range(N):
                if Board[i][j] == 'w':
                    s += 1
                if Board[i][j] == 'W':
                    s += 10
                if Board[i][j] == '@':
                    s += 50
                if Board[i][j] == 'b':
                    s -= 1
                if Board[i][j] == 'B':
                    s -= 10
                if Board[i][j] == '$':
                    s -= 50
    if player == 'b' or player == 'B':    
        for i in range(N):
            for j in range(N):
                if Board[i][j] == 'w':
                    s -= 1
                if Board[i][j] == 'W':
                    s -= 10
                if Board[i][j] == '@':
                    s -= 50
                if Board[i][j] == 'b':
                    s += 1
                if Board[i][j] == 'B':
                    s += 10
                if Board[i][j] == '$':
                    s += 50
                    
    return s




#referred from https://github.com/Chirag-Galani/B551-Elements-Of-Artificial-Intelligence/blob/master/Assignment%202/part1/pichu.py
def minmax(Board,c1,depth,player,c2,N):
    if c1 == depth:
        return cost_evaluation(Board,player,N),Board
    if player=='w':
        side='b'
    if player=='b':
        side='w'
    if c2 == 1:
        maxi=0
        new_Board=[]
        for i in successor(Board,player,N):
            p,q=minmax(i,c1+1,depth,side,-1,N)
            if maxi<=p:
                maxi=p
                new_Board=i
#         return eval(new_Board,player),new_Board
        return cost_evaluation(Board,player,N),new_Board
    if c2 == -1:
        mini=0
        new_Board=[]
        for i in successor(Board,player,N):
            p,q=minmax(i,c1+1,depth,side,1,N)
            if mini>=p:
                mini=p
                new_Board=i
       
        return cost_evaluation(Board,player,N),new_Board

        
        
        
def find_best_move(Board, N, player,timelimit):
    Board=list(Board)
    Board=np.reshape(Board, (N, N))
#     type(Board)
    depth = 1
    while 1:
        p,q = minmax(Board,0,depth,player,-1,N)
        # print(p,q)
        yield list_to_string(q,N)
        depth += 1



# if __name__ == "__main__":
#     if len(sys.argv) != 5:
#         raise Exception("Usage: Raichu.py N player Board timelimit")
        
#     (_, N, player, board, timelimit) = sys.argv
#     N=int(N)
#     timelimit=int(timelimit)
#     if player not in "wb":
#         raise Exception("Invalid player.")

#     if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
#         print(len(board))
#         raise Exception("Bad Board string.")

#     print("Searching for best move for " + player + " from Board state: \n" + Board_to_string(board, N))
#     print("Here's what I decided:")
#     input_Board=convert(board,N)
#     for new_Board in find_best_move(input_Board, N, player):
#         print(new_Board)


# In[ ]:


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")
        
    (_,N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        print(len(board))
        raise Exception("Bad Board string.")

    print("Searching for best move for " + player + " from Board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for new_Board in find_best_move(board, N, player, timelimit):
        print(new_Board)


# if __name__ == "__main__":
#     ( N, player, board, timelimit) = ('8', 'w','........W.W.W.W..w.w.w.w................b.b.b.b..B.B.B.B........','10')
#     N=int(N)
#     timelimit=int(timelimit)
#     if player not in "wb":
#         raise Exception("Invalid player.")

#     if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
#         raise Exception("Bad board string.")

#     print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
#     print("Here's what I decided:")
#     for new_board in find_best_move(board, N, player, timelimit):
#         print(board_to_string(new_board, N))





