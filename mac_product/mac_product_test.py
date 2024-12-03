def generate_exact_mac_addresses(count, prefix="34:BB:11"):  
    """  
    精确生成指定数量的MAC地址，并将它们作为生成器返回。  
      
    :param count: 要生成的MAC地址精确数量  
    :param prefix: MAC地址的前缀，默认为"34:A3:11"  
    :return: 生成MAC地址<生成器> 
    """  
    byte1, byte2, byte3 = 0, 0, 0  
    while count > 0:  
        mac_address = f"{prefix}:{byte1:02X}:{byte2:02X}:{byte3:02X}"  
        yield mac_address  
        byte3 = (byte3 + 1) % 256  # 第三个字节循环  
        if byte3 == 0:  
            byte2 = (byte2 + 1) % 256  # 第二个字节循环  
            if byte2 == 0:  
                byte1 = (byte1 + 1) % 256  # 第一个字节循环  
        count -= 1  
  
# 生成10000个MAC地址  
mac_addresses = generate_exact_mac_addresses(10000)  #需要生成多少个MAC在这里修改
  
# 将MAC地址写入到文件  *一行写一个MAC 在file write函数里加 "\n"
with open("mac_auto_p.txt", "w") as file:  
    for mac in mac_addresses:  
        file.write(mac + "\n")