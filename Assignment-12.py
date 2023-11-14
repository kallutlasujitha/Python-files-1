
#CASE:1 NO EXCEPTION RAISED

# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except :
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7



#CASE:2 IF EXCEPTION RAISED AT STATEMENT-1 AND EXCEPT BLOCK IS MATCHED
 
# try:
#     print(10/0)#statment-1
#     print(10/3)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7



#CASE:3 IF EXCEPTION RAISED AT STATEMENT-1 AND EXCEPT BLOCK IS NOT  MATCHED
 
# try:
#     print(10/0)#statment-1
#     print(10/3)#statment-2
#     print(10/2)#statment-3
# except ValueError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7



#CASE:4 IF EXCEPTION RAISED AT STATEMENT-2 AND EXCEPT BLOCK IS MATCHED
 
# try:
#     print(10/3)#statment-1
#     print(10/0)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7 



#CASE:5 IF EXCEPTION RAISED AT STATEMENT-2 AND EXCEPT BLOCK  NOT  MATCHED
 
# try:
#     print(10/3)#statment-1
#     print(10/0)#statment-2
#     print(10/2)#statment-3
# except ValueError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7



#CASE:6 IF EXCEPTION RAISED AT STATEMENT-3 AND EXCEPT BLOCK IS MATCHED
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/0)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7 



#CASE:7 IF EXCEPTION RAISED AT STATEMENT-3 AND EXCEPT BLOCK  NOT  MATCHED
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/0)#statment-3
# except ValueError:
#     print("except block")#statment-4
# else:
#     print("else")#statment-5
# finally:
#     print("finally")#statment-6
# print("outside the block")#statment-7



#CASE:8 IF EXCEPTION RAISED AT STATEMENT-4 
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except :
#     print(10/0)#statment-4
#     print("except block -2")#statment-5
# else:
#     print("else")#statment-6
# finally:
#     print("finally")#statment-7
# print("outside the block")#statment-8



#CASE:9 IF EXCEPTION RAISED AT STATEMENT-5 
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print(10/0)#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print("finally")#statment-7
# print("outside the block")#statment-8



#CASE:10 IF EXCEPTION RAISED AT STATEMENT-6 
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print("except block-2")#statment-5
# else :
#     print(10/0)#statment-6
# finally:
#     print("finally")#statment-7
# print("outside the block")#statment-8



# CASE:11 IF EXCEPTION RAISED AT STATEMENT-7
  
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print("except block-2")#)#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print(10/0)#statment-7
# print("outside the block")#statment-8



#CASE:12 IF EXCEPTION RAISED AT STATEMENT-8 
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print("except block-2")#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print("final")#statment-7
# print(10/0)#statment-8



#CASE:13 IF EXCEPTION RAISED AT STATEMENT-3 AND STATEMENT-4 . AND HANDLING CODE ON STATEMENT-4

# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/0)#statment-3
# except ZeroDivisionError:
#     print(10/0)#statment-4
#     print("except block-2")#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print("final")#statment-7
# print(10/2)#statment-8



#CASE:14 IF EXCEPTION RAISED AT STATEMENT-3 AND STATEMENT-4 . AND  NO HANDLING CODE ON STATEMENT-4

# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/0)#statment-3
# except :
#     print(10/0)#statment-4
#     print("except block-2")#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print("final")#statment-7
# print(10/2)#statment-8



#CASE:16 IF EXCEPTION RAISED AT STATEMENT-4 AND STATEMENT-6
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print(10/0)#statment-4
#     print("except block")#statment-5
# else :
#     print(10/0)#statment-6
# finally:
#     print("final")#statment-7
# print(10/2)#statment-8



#CASE:17 IF EXCEPTION RAISED AT STATEMENT-5 AND STATEMENT-6
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print(10/0)#statment-5
# else :
#     print(10/0)#statment-6
# finally:
#     print("final")#statment-7
# print(10/2)#statment-8



#CASE:18 IF EXCEPTION RAISED AT STATEMENT-3 AND STATEMENT-5 AND HANDLING CODE ON STATEMENT-3
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/0)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print(10/0)#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print("final")#statment-7
# print(10/2)#statment-8



#CASE:19 IF EXCEPTION RAISED AT STATEMENT-6 AND STATEMENT-7 AND HANDLING CODE ON STATEMENT-3
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print("except block-2")#statment-5
# else :
#     print(10/0)#statment-6
# finally:
#     print(10/0)#statment-7
# print(10/2)#statment-8




#CASE:20 IF EXCEPTION RAISED AT STATEMENT-3 AND STATEMENT-7 AND HANDLING CODE ON STATEMENT-3
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/0)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print("except block-2")#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print(10/0)#statment-7
# print(10/2)#statment-8



#CASE:21 IF EXCEPTION RAISED AT STATEMENT-7 AND STATEMENT-8
  
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print("except block-2")#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print(10/0)#statment-7
# print(10/0)#statment-8



#CASE:22 IF EXCEPTION RAISED AT STATEMENT-4 AND STATEMENT-7
  
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print(10/0)#statment-4
#     print("except block-2")#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print(10/0)#statment-7
# print("outside the block")#statment-8



#CASE:23 IF EXCEPTION RAISED AT STATEMENT-5 AND STATEMENT-7 
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/2)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print(10/0)#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print(10/0)#statment-7
# print("outside the block")#statment-8



#CASE:24 IF EXCEPTION RAISED AT STATEMENT-3,STATEMENT-5 AND STATEMENT-7 AND HANDLING CODE ON STATEMENT-3
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/0)#statment-3
# except ZeroDivisionError:
#     print("except block")#statment-4
#     print(10/0)#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print(10/0)#statment-7
# print("outside the block")#statment-8



#CASE:25 IF EXCEPTION RAISED AT STATEMENT-3,STATEMENT-4 AND STATEMENT-7 AND HANDLING CODE ON STATEMENT-3
 
# try:
#     print(10/3)#statment-1
#     print(10/4)#statment-2
#     print(10/0)#statment-3
# except ZeroDivisionError:
#     print(10/0)#statment-4
#     print("except block-2")#statment-5
# else :
#     print("else")#statment-6
# finally:
#     print(10/0)#statment-7
# print("outside the block")#statment-8






