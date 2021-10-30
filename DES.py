initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]
# Final Permutation Table
final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32,
               39, 7, 47, 15, 55, 23, 63, 31,
               38, 6, 46, 14, 54, 22, 62, 30,
               37, 5, 45, 13, 53, 21, 61, 29,
               36, 4, 44, 12, 52, 20, 60, 28,
               35, 3, 43, 11, 51, 19, 59, 27,
               34, 2, 42, 10, 50, 18, 58, 26,
               33, 1, 41, 9, 49, 17, 57, 25 ]
keyp = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4 ]
pc2_table = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32 ]
shift_table = [1, 1, 2, 2,
                2, 2, 2, 2,
                1, 2, 2, 2,
                2, 2, 2, 1 ]
exp_d = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
         12, 13, 12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21, 20, 21,
         22, 23, 24, 25, 24, 25, 26, 27,
         28, 29, 28, 29, 30, 31, 32, 1 ]
sbox =  [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
            
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],
   
         [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
       
          [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],
        
          [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
       
         [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],
         
          [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],
        
         [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]
pbox= [ 16,  7, 20, 21,
        29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2,  8, 24, 14,
        32, 27,  3,  9,
        19, 13, 30,  6,
        22, 11,  4, 25 ]
def permutate(arr,table):
    arr_block=''
    for i in range(len(table)):
        x=table[i]-1
        y=arr[x]
        arr_block+=y
    return arr_block
def desPlaintextBlock():
    f=open("plaintext.txt",'r')
    str=f.read()
    y=""
    for x in str:
        y+=format(ord(x), 'b')
    arr_of_blocks=[]
    chunk_size =64
    arr_of_blocks = [y[i:i+chunk_size] for i in range(0, len(y), chunk_size)]
    last_block=arr_of_blocks[len(arr_of_blocks)-1]
    count=len(last_block)
    if (count <64):
        app=64-count
        for x in range(app):
            last_block='0'+last_block
    arr_of_blocks.pop()
    arr_of_blocks.append(last_block)
    # arr_of_blocks[len(arr_of_blocks)-1]=int(last_block)
    f.close()
    print(arr_of_blocks)
    return arr_of_blocks
def desCiphertextBlock():
    f=open("ciphertext.txt",'r')
    str_r=f.read()
    arr_of_blocks=[]
    chunk_size =64
    arr_of_blocks = [str_r[i:i+chunk_size] for i in range(0, len(str_r), chunk_size)]
    last_block=arr_of_blocks[len(arr_of_blocks)-1]
    count=len(last_block)
    if (count <64):
        app=64-count
        for x in range(app):
            last_block='0'+last_block
    arr_of_blocks.pop()
    arr_of_blocks.append(last_block)
    # arr_of_blocks[len(arr_of_blocks)-1]=int(last_block)
    f.close()
    return arr_of_blocks
def desInitialPermutation (arr_of_blocks):
    return permutate(arr_of_blocks,initial_perm)
def desFinalPermutation (ip_blocks):
    return permutate(ip_blocks,final_perm)
def hex2bin(s):
    mp = {'0' : "0000",
          '1' : "0001",
          '2' : "0010",
          '3' : "0011",
          '4' : "0100",
          '5' : "0101",
          '6' : "0110",
          '7' : "0111",
          '8' : "1000",
          '9' : "1001",
          'A' : "1010",
          'B' : "1011",
          'C' : "1100",
          'D' : "1101",
          'E' : "1110",
          'F' : "1111" }
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin
def PC1(key):
    return permutate(key,keyp)
def PC2(key):
    return permutate(key,pc2_table)
# shifting the bits towards left by nth shifts
def shift_left(k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
        for j in range(1,len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k 
def getSubkeys ():
    f=open("secretkey.txt",'r')
    str=f.read()
    key=hex2bin(str)
    arr_of_subkeys=[]
    arr_of_PC1=(PC1(key))
    C=arr_of_PC1[0:28]
    D=arr_of_PC1[28:56]
    for i in range(16):
        # Shifting the bits by nth shifts by checking from shift table
        C = shift_left(C, shift_table[i])
        D = shift_left(D, shift_table[i])
        combine_subkey = C + D
        round_sub_key=PC2(combine_subkey)
        arr_of_subkeys.append(round_sub_key)
    f.close()
    return arr_of_subkeys
def s_box(chunks):
    sbox_res=""
    i=0
    for x in chunks:
        row=x[:1]+x[5:6]
        col=x[1:5]
        row=int(row,2)
        col=int(col,2)
        res=format(sbox[i][row][col],"b")
        #Padding 0 if less than four binary came
        if len(res)<4:
            remain=4-len(res)
            for z in range(remain):
                res='0'+res
        sbox_res+=res
    return sbox_res
def xor(arr1,arr2):
    xor_res=""
    for i in range(len(arr1)):
         xor_res+=str(int(arr1[i])^int(arr2[i]))
    return xor_res
def rounds(ip_block,keys):
    L=ip_block[0:32]
    R=ip_block[32:64]
    l=1
    for x in keys:
        R_ir=permutate(R,exp_d)
        xor_res=xor(R_ir,x)
        n = 6
        chunks = [xor_res[i:i+n] for i in range(0, len(xor_res), n)]
        sbox_res=s_box(chunks)
        pbox_res=permutate(sbox_res,pbox)
        xor_pbox_res=xor(pbox_res,L)
        IR=R
        R=xor_pbox_res
        L=IR
        l+=1
    # 32-bit swap
    result=R+L
    return result

def encryption(keys):
    arr_of_blocks=desPlaintextBlock()
    ip_blocks=[]
    # final_ip_blocks=[]
    for x in arr_of_blocks:
        ip_blocks.append(desInitialPermutation(x))
    encrypted_blocks=[]
    swaped_blocks=[]
    for x in ip_blocks:
        swaped_blocks.append(rounds(x,keys))
    for x in swaped_blocks:
        encrypted_blocks.append(desFinalPermutation(x))
    cipher_str=""
    for x in encrypted_blocks:
        cipher_str+=x
    f=open("ciphertext.txt","w")
    f.write(cipher_str)
    f.close()
def decryption(keys):
    arr_of_blocks=desCiphertextBlock()
    ip_blocks=[]
    # final_ip_blocks=[]
    for x in arr_of_blocks:
        ip_blocks.append(desInitialPermutation(x))
    decrypted_blocks=[]
    swaped_blocks=[]
    for x in ip_blocks:
        swaped_blocks.append(rounds(x,keys))
    for x in swaped_blocks:
        decrypted_blocks.append(desFinalPermutation(x))
    plain_str=""
    plain_arr=[]
    for x in decrypted_blocks:
        plain_str+=x
        plain_arr.append(x)
    print(plain_str)
    

keys=getSubkeys()
rev_keys=keys[::-1]
encryption(keys)
decryption(rev_keys)