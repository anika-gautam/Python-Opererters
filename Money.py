amount=int(input("Enter the amount:"))
note1=(amount//100)
note2=(amount%100)//50
note3=((amount%100)%50)//10
print( "Notes of hundred rupees",note1) 
print("Notes of 50 rupees", note2)
print("Notes of 10 rupees", note3)