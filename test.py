import getpass
import os

user = getpass.getuser()

print("计算机用户名为：", user)
print("我的:")        #可查2023年单子(其中8000最终是我垫)  (微粒贷帮还)                                    （word可查）
myfee_wihtout_interest = (20000+8000+1643.52+4255.01) + (3891.14+3923.83+3976.40+3162.75+3848.3+808.68)+(2480+500+1000+2900+8000+2700+1000+1000+5000);
print(myfee_wihtout_interest) #我的 不包含佳佳的 不包含招行和温行的利息
############################################################################################################################
                    #  1月    2月    3月    4月    5月   6月（开始本息 -> 濛濛转了2122.2）
zhaoshang_interest = 238.08+238.08+222.72+238.08+230.4+ 0;
print(zhaoshang_interest)#招行利息
############################################################################################################################
                #   1月    2月     3月     4月      5月       6月 
wenzhou_interest = 594.17+594.17+555.83+594.17+(402.5+172.5)+594.17;
print(wenzhou_interest)#温行利息
############################################################################################################################
#print("佳佳的:")
#print(15000)#佳佳的
print("------------------------------------------------------------")
print("记录在账的总共：")
total_in_record = myfee_wihtout_interest+zhaoshang_interest+wenzhou_interest;
print(total_in_record)
print("------------------------------------------------------------")
#print("总共：")
#print(myfee_wihtout_interest+zhaoshang_interest+wenzhou_interest+15000)
print("------------------------------------------------------------")
def getStringFromNumber(size,value):
        """
        转为十六进制（Hex）字符串
        :param size:
        :param value:
        :return:
        """
        size=int(size)
        value=int(value)
        by = bytearray([])
        for i in range(1,size+1):
            val = value >> 8 * (size - i) & 255
            by.append(val)
        val = by.hex()
        print("============================================================")
        print("%s转为%s个字节十六进制（Hex）字符串:%s"%(value,size,val))
        print("============================================================")
        print("path >> %s ",os.path);
        print(__name__)
        '''
        //print(">>> %s "os.getlogin())
        '''
        #print(60735.07-(25000+27000+8333.33+330))
        return val
#或者50的hex值
print("未记录入账的：")
not_in_record = 3318+5000+2122.2+909+575+200+1400-10000-2000+5730+5000-(17800-2698.98-4430.33-2122.2)+10000+2849.58-4000-5000-2000+800+2480+1000-5000+358+1800-6000+2500-8000+9426.63
print(not_in_record)

print("拍拍帮还：")
Oct_paipai = 229.49+9455.95+266.01+6755.24+4170.78;
print(Oct_paipai) #20877.47

#10月帮还招行贷和抖音
Oct_zhaoAndTiktok = 31.21+2091.49+2709.33
print("10月帮还招行贷和抖音帮还：")
print(Oct_zhaoAndTiktok)

print("总共欠款：")                                              #6000这个现金欠了比较久 濛濛Excel里也有记录
print(total_in_record+not_in_record+Oct_paipai+Oct_zhaoAndTiktok+6000)
getStringFromNumber(1,50)