import numpy as np                                      
import matplotlib.pyplot as plt


x =  np.arange(0,2*np.pi,0.1)           #  定義X軸的公式           
r = input("please input radius: ")      #  輸入一個值
r = int(r)                              #  定義輸入的值為整數

#=================將輸入的值儲存起來====================
file = open("data1.txt",mode="a")       #打開文字檔設定為"繼續寫入"
R = str(r)
file.write('the radius is: ')
file.write(R)
file.write('\n')
file.close()
#=======================================================

#=================sin cos tan 運算======================
s = r*np.sin(x)                         #  s=(sin)
c = r*np.cos(x)                         #  c=(cos)                   
t = r*np.tan(x)                         #  t=(tan)
plt.xlabel('wave', fontsize = 16)       #  將X軸的顯示文字設定為"wave"，字體大小為16             
plt.xticks(fontsize = 15)               #  x軸的數字大小                  
plt.yticks(fontsize = 15)               #  y軸的數字大小 
plt.grid(color = 'r', linestyle = '--', linewidth = 1)                # 我設置背景為"--"，顏色為紅色，線的寬度為1
plt.ylim(-10, 10)                       #把Y軸的極限控制在10到10                                       
line1, = plt.plot(x,s, color = 'r', linewidth = 3, label = 'sin')     #sin波為紅色，線的寬度為3，並且做標籤       
line2, = plt.plot(x,c, color = 'b', linewidth = 3, label = 'cos')     #cos波為藍色，線的寬度為3，並且做標籤 
line3, = plt.plot(x,t, color = 'g', linewidth = 3, label = 'tan')     #tan波為綠色，線的寬度為3，並且做標籤 

plt.legend(handles = [line1, line2, line3], loc='upper right')        #把我設定的標籤設定於右上角                                    
plt.savefig('wave Test.png')            #儲存檔案到D:/python/matplotlib

plt.show()                              #顯示波型 
