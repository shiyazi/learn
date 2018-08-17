weight = [4, 2, 9, 5, 5, 8, 5, 4, 5, 5]
value = [3, 8, 18, 6, 8, 20, 5, 6, 7, 15]
p = list(v / w for w, v in zip(weight, value))  # zip将list打包为元组
end = dict(zip(p,weight))

