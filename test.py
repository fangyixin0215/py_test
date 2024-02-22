import getpass
import os

user = getpass.getuser()

print("计算机用户名为：", user)
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
        print("===============================")
        print("%s转为%s个字节十六进制（Hex）字符串:%s"%(value,size,val))
        print("===============================")
        print("path >> %s ",os.path);
        print(__name__)
        '''
        //print(">>> %s "os.getlogin())
        '''
        print(60735.07-(25000+27000+8333.33+330))
        return val
getStringFromNumber(1,50)