sx,sy,tx,ty = map(int,input().split())
x_dis = tx - sx
y_dis = ty - sy
ans1 = "U"*y_dis + "R"*x_dis
ans2 = "D"*y_dis + "L"*x_dis
ans3 = "L" + "U"*(y_dis+1) + "R"*(x_dis+1) + "D"
ans4 = "R"+ "D"*(y_dis+1) + "L"*(x_dis+1) + "U"
print(ans1+ans2+ans3+ans4)