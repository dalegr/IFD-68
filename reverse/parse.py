f = open('default.bin', 'rb')
fout = open('default.keypmap.bin', 'wb')
f.seek(0x18, 0)
while True:
    f.seek(0x10 + 0x1b + 0x02, 1)
    b1 = f.read(1)
    if not b1: break
    b2 = f.read(1)
    f.seek(1, 1)
    b3 = f.read(1)
    b4 = f.read(1)
    print('mod1=0x%X key1=0x%X -> mod2=0x%X key2=0x%X' % (int.from_bytes(b1, byteorder='little'), int.from_bytes(b2, byteorder='little'), int.from_bytes(b3, byteorder='little'), int.from_bytes(b4, byteorder='little')))
    fout.write(b1)
    fout.write(b2)
    fout.write(b3)
    fout.write(b4)
    f.seek(0x39, 1)
fout.close()
f.close()
