direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if(direction=='encode' or direction=='decode'):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    string_list=text.split(" ")

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    def encode(text,shift):
        new_string_list=[]
        for i in text:
            newWord=""
            for j in i:
                int_of_char_with_shift=ord(j)+shift
                if int_of_char_with_shift>122:
                    int_of_char_with_shift-=26
                newWord+=chr(int_of_char_with_shift)
            new_string_list.append(newWord)
        print(f"The encrypted text with shift of {shift} is: ",end='')
        for i in new_string_list:
            print(i,end=" ")
        print("\n")  

    def decode(text,shift):
        new_string_list=[]
        for i in text:
            newWord=""
            for j in i:
                int_of_char_with_shift=ord(j)-shift
                if int_of_char_with_shift<97:
                    int_of_char_with_shift+=26
                newWord+=chr(int_of_char_with_shift)
            new_string_list.append(newWord)
        print(f"The decrypted text with shift of {shift} is: ",end='')
        for i in new_string_list:
            print(i,end=" ")
        print("\n")  



    if(direction=='encode'):
        encode(string_list,shift)
    else:
        decode(string_list,shift)



else:
    print("Sorry wrong input! Try again")