# ----------------------------------------------------------코드업 100문제---------------------------------------------------------------------------
# a, b = map(int, input().split())
# if a >= b :
#     c = a
# else :
#     c = b
# print(c)

# a, b, c = map(int, input().split())
# d = ((a if (a < b) else b) if ((a if (a < b) else b)<c) else c)
# print(d) # c가 온다.

# a, b, c = map(int, input().split())
# if a%2 == 0 :
#     print("even")
# else:
#     print('odd')
# if b%2 == 0 :
#     print("even")
# else:
#     print('odd')
# if c%2 == 0 :
#     print("even")
# else:
#     print('odd')


# a = int(input())
# b = None
# if a < 0:
#     if a % 2 == 0:
#         b = "A"
#     else:
#         b = "B"
# else:
#     if a % 2 == 0:
#         b = "C"
#     else:
#         b = "D"
# print(b)

# # 6068
# a = int(input())
# if a > 100 or a < 0:
#     print("0~100점을 입력하세요.")
# elif a <= 100 and a >= 90:
#     print("A")
# else:
#     if a >= 70:
#         print("B")
#     else:
#         if a >= 40:
#             print("C")
#         else:
#             if a > 0:
#                 print("D")

# # 6069
# a = input()
# if a == "A":
#     print("best!!!")
# elif a == "B" :
#     print('good!!')
# elif a == "C":
#     print("run!")
# elif a == "D" :
#     print("slowly~")
# else :
#     print("what?")

# # 6070

# a = int(input())
# b = None
# if a // 3 == 1:
#     b = "spring"
# elif a // 3 == 2:
#     b = "summer"
# elif a // 3 == 3:
#     b = "fall"
# elif a // 3 == 4 or a // 3 == 0:
#     b = "winter"
# else:
#     b = "1월부터 12월 까지만 있어요. 왜이러셔?"
# print(b)

# # 6071
# n = int(1)
# while n != 0:
#     n = int(input())
#     if n == 0:
#         break
#     print(n)

# # 6072
# a = int(input())
# b = list(range(1, a + 1))
# b.reverse()
# for i in b:
#     print(i)

# #6073
# a = int(input())
# while a >= 1:
#     a -= 1
#     print(a)


# 6074

# char = ord(input())
# b = list(range(ord("a"), char + 1))
# for i in b:
#     print(chr(i), end=" ")

# 6075

# a = int(input())
# i = 0
# while i <= a:
#     print(i)
#     i += 1

# 6076

# a = int(input())
# for i in range(a + 1) :
#     print(i)

# 6077

# a = int(input())
# b = 0
# for i in range(1, a + 1):
#     if i % 2 == 0:
#         b = b + i
# print(b)


# 6078
# a = None
# while a != "q":
#     a = input()
#     print(a)

# 6079

# a = int(input())
# b = int(0)
# for i in range(1, a + 1):
#     b = b + i
#     if b >= a:
#         print(i)
#         break

# 6080

# a, b = map(int, input().split())
# for i in range(1, a + 1):
#     for j in range(1, b + 1):
#         print(i, j)

# 6081

# a = input()
# dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
# b = int(0)
# for i in range(1, 16):
#     b = dict[a]
#     print("%X" % b, "*", "%X" % i, "=", "%X" % (b * i), sep="")
# a = int(input(), 16)  # 16진수 변환.

# 6082

# a = int(input())
# for i in range(1, a + 1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print("X", end=" ")
#         continue
#     print(i, end=" ")

# 6085

# h, b, c = map(int, input().split())
# sum = h * b * c / 8 / 1024 / 1024
# print("%.2f" % sum, "MB")

# 6086

# a = int(input())
# s = int(0)
# for i in range(1, a + 1):
#     s += i
#     if s >= a:
#         break
# print(s)

# 6090

# s, m, d, n = map(int, input().split())
# count = int(1)
# while count != n :
#     s = s * m + d
#     count += 1
# print(s)

# 6091

# a, b, c = map(int, input().split())
# d = int(1)
# while d%a != 0 or d%b != 0 or d%c != 0 :
#     d += 1
# print(d)

# while False or False or True :
#     print(1)
#     break

# a = int(input())
# b = list(map(int, input().split()))
# cnt = []
# for i in range(1, 24):
#     cnt.append(0)
# for j in b:
#     j = j-1
#     cnt[j] = cnt[j] + 1
# for i in cnt:
#     print(i, end=" ")

# ----------------------------------------------------------코드업 100문제---------------------------------------------------------------------------
# a = int(input())
# b = list(map(int, input().split()))

# print(min(b))

# a = []
# for i in range(20):
#     a.append([])
#     for j in range(20):
#         a.append([0])
# print(a)

# d = []
# for i in range(19):
#     d.append([])
#     for j in range(19):
#         d[i].append(0)
# n = int(input())
# for i in range(n):
#     x, y = map(int,input().split())
#     x -= 1
#     y -= 1
#     d[y][x] = 1
# for i in d:
#     for j in i:
#         print(j, end=" ")
#     print()
# print(len(d[0]))

# lst = []
# for i in range(19):
#     lst.append(list(map(int, input().split())))
# n = int(input())
# for i in range(n):
#     x, y = map(int, input().split())
#     x -= 1
#     y -= 1
#     for j in range(19) :
#         if lst[x][j] == 0:
#             lst[x][j] = 1
#         elif lst[x][j] == 1:
#             lst[x][j] = 0
#     for k in range(19):
#         if lst[k][y] == 0:
#             lst[k][y] = 1
#         elif lst[k][y] == 1:
#             lst[k][y] = 0
# for i in lst :
#     for j in i :
#         print(j, end=" ")
#     print()


# lst = []
# x, y = map(int, input().split())
# for i in range(x) :
#     lst.append([])
#     for j in range(y) :
#         lst[i].append(0)

# n = int(input())
# for i in range(n) :
#     l, d, x, y = map(int, input().split())
#     x -= 1
#     y -= 1
#     if d == 1 :
#         for j in range(l):
#             lst[x + j][y] = 1
#     else :
#         for k in range(l):
#             lst[x][y + k] = 1
# for i in lst :
#     for j in i :
#         print(j, end=" ")
#     print()

# lst = []
# for i in range(10): #0~9까지 총 10번
#     lst.append(list(map(int, input().split()))) #lst에 어펜드 해라. 공백을 기준으로 값을 받아서.
# # 시작좌표 : 2, 2
# x = 1 #0부터 시작하니까 1. 만약 1부터 시작했으면 2로 하는게 맞음.
# y = 1
# while lst[y][x] != 2 : #현재 위치가 2가 아니라면. 즉 2라면 종료된다.
#     if lst[y][x + 1] == 0 : #현재 위치의 바로 x+1칸이 0이라면,
#         lst[y][x] = 9 # 현재 위치를 9로 만들어라. 왜? 다음칸으로 이동해야하니까. 지금위치를 9로 만들면 이동한 효과를 내는거지.
#         x += 1 #x에 1을 더해서 현재위치를 가로로 한칸으로 옮김. 즉 행임.
#     elif lst[y][x + 1] == 1: # 현재 위치의 바로 x+1칸이 1이라면,
#         lst[y][x] = 9  ## 현재 위치를 9로 만들어라. 왜? 다음칸으로 이동해야하니까.
#         y += 1 # y에 1을 더해서 현재위치를 세로로 한칸 옮김. 즉 열임.
#         if lst[y][x] == 1: #현위치가 1이라면,
#             break # 벽이니까 멈춰라.
#     elif lst[y][x + 1] == 2: #현위치 바로 옆이 2일떄,
#         lst[y][x] = 9 #현위치 9로 만들고 ,
#         x += 1 # x값 +1해줘라.
# if lst[y][x] != 1: #현위치가 1이면. 즉 벽이라면 9로 바꾸면 안되.
#     lst[y][x] = 9
# for i in lst:
#     for j in i:
#         print(j, end=" ")
#     print()
from re import S


ditc = {}

cnt = 0
# a, b, k = map(int, input().split())
# if k == 1:
#     for i in [10**n for n in range(1, 9)]: #이건 틀렸다. 시작값이 무조건 0이거나 1이 아니다. 틀린거임.
#         if b > i:

# elif k == 0:
#     pass
# else:
#     pass
# lst = list(range(a, b+1))
# for i in lst:
#     i = str(i)
#     k = str(k)
#     if k in i :
#         cnt = cnt + i.count(k)
# print(cnt)
# if n in ditc:
#     return ditc[n]


# for i in range(a, b+1):
#     i = str(i)
#     k = str(k)
#     cnt = cnt + i.count(k)
# print(cnt)

# a = list(range(1, 10000000))
# print(a)

# 문제가 뭐냐면.
# 1. 1부터 1억까지 모든 숫자에서 1이 몇번 등장하는가? 임.
# 2. 1~10까지는 2번 등장함.
# 3. 10~100까지는? 몰라. 11~20까지 10번등장. 21~30까지 1번등장. 31~40까지 1번등장. 41~50까지 1번등장. ... 81~90까지 전부 1번등장. 91~100까지 2번등장. 101~110까지
# n2= str(119)
# ns = str(1)

# print(ns in n2)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# a ~ b까지 k가 몇번 등장하는가? 단, b < 1억, k = 0~9
# def count_digit_occurrences(n, digit):
#     count = 0
#     for i in range(len(n)):
#         current_digit = int(n[i])
#         high = int(n[:i]) if i > 0 else 0
#         low = int(n[i + 1 :]) if i < len(n) - 1 else 0

#         if current_digit > digit:
#             count += (high + 1) * (10 ** (len(n) - i - 1))
#         elif current_digit == digit:
#             count += high * (10 ** (len(n) - i - 1)) + low + 1
#         else:
#             count += high * (10 ** (len(n) - i - 1))

#         # 특별한 경우: digit이 0일 때, 선행하는 0들은 세지 않음
#         if digit == 0:
#             count -= 10 ** (len(n) - i - 1)
#     return count


# def find_occurrences(a, b, k):
#     if a == 0 and k == 0:
#         return count_digit_occurrences(str(b), k) + 1
#     return count_digit_occurrences(str(b), k) - count_digit_occurrences(str(a - 1), k)


# # 예시 입력에 따른 수정
# a, b, k = map(int, input().split())

# # 수정된 함수를 사용한 결과 계산
# result = find_occurrences(a, b, k)
# print(result)

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# n = int(input())

# dict = {}
# for i in range(n):
#     a, b =map(int, input().split())
#     dict[a] = b
# keylst = []
# for i in dict.keys() :
#     keylst.append(i)
# keylst.sort()
# for i in keylst :
#     print(i, dict[i])

#  ------------------------------------- 재귀함수 ------------------------------------------------------
# n = int(input())
# def plus(n) :
#     if n == 0:
#         return
#     else:
#         plus(n - 1)
#         print(n)

# plus(n)

# ##
# a, b = map(int, input().split())
# def odd(n, m) :
#     if n > m :
#         return " "
#     elif n % 2 == 1:
#         return str(n) + " " + odd(n + 1, m)
#     else:
#         return odd(n +1, m)

# result = odd(a, b)
# print(result)

# ##
# import sys

# # 재귀 깊이 제한을 늘립니다.
# sys.setrecursionlimit(15000)
# n = int(input())
# def sum(n):
#     if n == 0:
#         return 0
#     else :
#         return (sum(n - 1)) + n

# print(sum(n))

# ##
# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else :
#         return n * fac(n -1)
# n = int(input())
# print(fac(n))

##
# def fibonachi(n, i, j):
#     cnt = 0
#     if n <= 3 :
#         if n == 1 or n == 2:
#             return 1
#         elif n == 3:
#             return 2
#     if (n-2) == cnt: #인덱스를 어떻게 맞출지 생각하자. 240223 17:56;
#         return j
#     if n > 20:
#         k = j
#         j = i + j
#         i = k
#         cnt += 1
#         return j
#     else :
#         if j == 0:
#             j = 1 + i
#             cnt += 1
#             return 1, i, j, fibonachi(n + 1, i, j)
#         else:
#             k = j
#             j = i + j
#             i = k
#             cnt += 1
#             return j, fibonachi(n + 1, i, j)

# n = int(input())
# print(fibonachi(n, 1, 0))


# 1 + a = b
# a + b = b
# b + b = b


##


# n = int(input())
# lst = list(map(int, input().split()))
# lst_sort = lst[:]
# lst_sort.sort()
# lst_revers = lst[:]
# lst_revers.sort(reverse=True)
# if lst == lst_sort:
#     print("오름차순")
# elif lst == lst_revers:
#     print("내림차순")
# else:
#     print("섞임")

# import numpy as np

# x = int(input())
# print(1 / (1 + np.exp(-x)))


# 그리디문제 --------------------------------------
# a, b, c, d, e = map(int, input().split())

# p = []
# j = []
# result = []
# # p 3개와 j2개를 각각 곱해서 나온 결과를 저장하고 가장 작은 값을 출력한다.
# for i in range(3):
#     p.append(int(input()))

# for i in range(2):
#     j.append(int(input()))

# for i in p:
#     for k in j:
#         result.append(round(((i + k) * 1.1), 2))

# result.sort()
# print(result[0])
# ------------------------------------------------------
