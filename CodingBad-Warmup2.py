{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red202\green202\blue202;}
{\*\expandedcolortbl;;\cssrgb\c83137\c83137\c83137;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl420\partightenfactor0

\f0\fs28 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #warmup-2\
#string_timies\
def string_times(str, n):\
  result = ""\
  for i in range(n):\
    result = result + str \
  return (result)\
\
#front_times\
def front_times(str, n):\
  if len(str) > 3:\
    return(str[:3]*n)\
  else:\
    return(str*n)\
\
def front_times(str, n):\
  front_len = 3\
  if front_len > len(str):\
    front_len = len(str)\
  front = str[:front_len]\
  \
  result = ""\
  for i in range(n):\
    result += front\
  return(result)\
\
#string_bits\
def string_bits(str):\
  result = ""\
  for i in range(len(str)):\
    if i % 2 == 0: \
      result += str[i]\
  return (result)\
\
#string_soplosion\
def string_splosion(str):\
  result= ""\
  for i in range(len(str)):\
    result += str[:i+1]\
  return (result) \
\
#array_count9\
def array_count9(nums):\
  count = 0\
  for i in nums:\
    if i == 9:\
      count += 1\
  return (count)\
\
#array_front\
def array_front9(nums):\
  end = len(nums)\
  if end > 4:\
    end = 4\
  \
  for i in range(end):\
    if nums[i] == 9:\
      return (True)\
  return(False)\
\
#array123\
def array123(nums):\
  for i in range(len(nums)-2):\
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] ==3:\
      return(True)\
  return(False)\
\
#string_match\
def string_match(a, b):\
  shorter = min(len(a),len(b))\
  count = 0\
  \
  for i in range(shorter-1):\
    a_sub = a[i:i+2]\
    b_sub = b[i:i+2]\
    if a_sub == b_sub:\
      count += 1\
  return (count)}