# #CASE:1 IF THERE IS NO EXCEPTION RAISED
# # def nested(a,b):
# #     try:
# #         if a%2==0:
# #             print("division satisfied")
# #         else:
# #             print("division not satisfied")
# #         try:
# #             if a*b:
# #                 print("multiplication satisfied")
# #             else:
# #                 print("multiplication is not satisfied")
# #         except BaseException:
# #             print("above multiplication must be something wrong")
# #             print("once check above multiplication condition ")
# #         finally:
# #             print("multiplication condition will be end")
# #             print("Rewrite another way")
# #     except BaseException:
# #         print("above division must be something wrong")
# #         print("once check above division condition")
# #     finally:
# #         print("division condition will be end")
# #         print("Try to write something new method")
# # a=int(input("enter a number"))
# # b=int(input("enter a number"))
# # nested(a,b)

# # # CASE:2 IF EXCEPTION RAISED AT STATEMENT-2 AND EXCEPT BLOCK IS MATCHED
# # def nested(a,b):
# #     try:
# #         if a%2==0: #stmt-1
# #             print("division satisfied")
# #         else:
# #             print("division not satisfied")
# #         try:
# #             if a*b:
# #                 print("multiplication satisfied")
# #             else:
# #                 print("multiplication is not satisfied")
# #         except ValueError:
# #             print("above multiplication must be something wrong")
# #             print("once check above multiplication condition ")
# #         finally:
# #             print("multiplication condition will be end")
# #             print("Rewrite another way")
# #     except ValueError:
# #         print("above division must be something wrong")
# #         print("once check above division condition")
# #     finally:
# #         print("division condition will be end")
# #         print("Try to write something new method")
# # a=int(input("enter a number"))
# # b=int(input("enter a number"))
# # nested(a,b)





# # def nested(a,b):
# #     try:
# #         if a%2==0: #stmt-1
# #             print("division satisfied")
# #         else:
# #             print("division not satisfied")
# #         try:
# #             if a*b:
# #                 print("multiplication satisfied")
# #             else:
# #                 print("multiplication is not satisfied")
# #         except TypeError:
# #             print("above multiplication must be something wrong")
# #             print("once check above multiplication condition ")
# #         finally:
# #             print("multiplication condition will be end")
# #             print("Rewrite another way")
# #     except TypeError:
# #         print("above division must be something wrong")
# #         print("once check above division condition")
# #     finally:
# #         print("division condition will be end")
# #         print("Try to write something new method")
# # a=int(input("enter a number"))
# # b=int(input("enter a number"))
# # nested(a,b)

# # try:
# #     print(10/2)
# #     print(2*2)
# #     print(10/0)
# #     try:
# #         if x%2==1:
# #             print("odd number")
# #     except ValueError:
# #         print("ok")
# # except ZeroDivisionError:
# #     print("division erroe")

# # case:IF EXCEPTION RAISED AT STATEMENT-2 AND EXCEPT BLOCK IS MATCHED 
# # try:
# #     print(10/3)#statment-1
# #     print(10/0)#statment-2
# #     print(10/2)#statment-3
# #     try:
# #         print("inner try 1")#statment-4
# #         print("inner try 2")#statment-5
# #         print("inner try 3")#statment-6
# #     except :
# #         print("inner except block")#statment-7
# #     finally:
# #         print("inner finally block")#statment-8
# #     print("normal statment ")#statment-9
# # except ZeroDivisionError :
# #     print("outer except block")#statment-10
# # finally:
# #     print("outer finally block")#statment-11
# # print("outside the blocks")#statment-12



# # case:IF EXCEPTION RAISED AT STATEMENT-3 AND EXCEPT BLOCK IS MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except :
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12


# # case:IF EXCEPTION RAISED AT STATEMENT-3 AND EXCEPT BLOCK IS  not matched MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except :
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ValueError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12


# # case:IF EXCEPTION RAISED AT STATEMENT-3 AND EXCEPT BLOCK IS  not  MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except :
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ValueError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12


# # case:IF EXCEPTION RAISED AT STATEMENT-4 AND EXCEPT BLOCK IS   MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print(10/0)#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except ZeroDivisionError:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12


# # case:IF EXCEPTION RAISED AT STATEMENT-4 AND EXCEPT BLOCK IS not MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print(10/0)#statment-4
#         print("inner try 2")#statment-5
#         print("inner try 3")#statment-6
#     except ValueError:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12


# # case:IF EXCEPTION RAISED AT STATEMENT-5 AND EXCEPT BLOCK IS  MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print(10/0)#statment-5
#         print("inner try 3")#statment-6
#     except ZeroDivisionError:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12



# # case:IF EXCEPTION RAISED AT STATEMENT-5 AND EXCEPT BLOCK IS not MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print(10/0)#statment-5
#         print("inner try 3")#statment-6
#     except :
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12

# # case:IF EXCEPTION RAISED AT STATEMENT-6 AND EXCEPT BLOCK IS MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(10/0)#statment-6
#     except ZeroDivisionError:
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12


# # case:IF EXCEPTION RAISED AT STATEMENT-6 AND EXCEPT BLOCK IS not MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(10/0)#statment-6
#     except :
#         print("inner except block")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12

# # case:IF EXCEPTION RAISED AT STATEMENT-7 AND EXCEPT BLOCK IS  MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(10/0)#statment-6
#     except ZeroDivisionError:
#         print(10/0)#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12


# # case:IF EXCEPTION RAISED AT STATEMENT-7 AND EXCEPT BLOCK IS not MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(10/0)#statment-6
#     except ZeroDivisionError:
#         print(10/0)#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12


# # case:IF EXCEPTION RAISED AT STATEMENT-8 AND EXCEPT BLOCK IS MATCHED 
# try:
#     print(10/3)#statment-1
#     print(10/2)#statment-2
#     print(10/0)#statment-3
#     try:
#         print("inner try 1")#statment-4
#         print("inner try 2")#statment-5
#         print(10/0)#statment-6
#     except ZeroDivisionError:
#         print("inner except error")#statment-7
#     finally:
#         print("inner finally block")#statment-8
#     print("normal statment ")#statment-9
# except ZeroDivisionError :
#     print("outer except block")#statment-10
# finally:
#     print("outer finally block")#statment-11
# print("outside the blocks")#statment-12

