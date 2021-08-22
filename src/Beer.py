

text_block = ""

test = range(99, -1, -1)

for beer_count in range(99, -1, -1):
    if beer_count >=2:
        text_block += f"{beer_count} bottles of beer on the wall, {beer_count} bottles of beer.  Take one down, pass it around, {beer_count}, bottles of beer on the wall."
    elif beer_count ==1:
        text_block += f"{beer_count} bottles of beer on the wall, {beer_count} bottles of beer.  Take one down, pass it around, {beer_count}, bottles of beer on the wall." 
    elif beer_count < 1:
        text_block += ("No more bottles of beer on the wall.  :(")  #This produces a huge string

text_block_array = [text_block[i:i+400] for i in range(0, len(text_block), 400)] #This turns the string into a list and limits it to 400 characters


for block in text_block_array: 
     print(block)

print('done')

        #for i in range(99, -1, -1):
    #if i >=2:
        #print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.  Take one down, pass it around, " +str(i) + " bottles of beer on the wall.")
    #elif i ==1:
        #print(str(i) + " bottle of beer on the wall, " + str(i) + " bottle of beer.  Take one down, pass it around, " +str(i) + " bottle of beer on the wall.")
    #elif i < 1:
        #print("No more bottles of beer on the wall.  :(")