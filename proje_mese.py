
with open("output_2022-09-02_15-08-11 .txt","r") as file:
    content_of_file = file.read()
    content_of_file=content_of_file.split("\n")
    str1 = ""

    liste = []

    for i in content_of_file:
        veri= i
        veri = str(veri)


        if veri.endswith(":") == True:
            saat = veri


        elif veri.isnumeric() == False and veri!="":

            veri=veri.split(" ")
            if len(veri)==3:
                veri.pop(0)
                listToStr = " ".join([str(j) for j in veri])

                kilogram = listToStr
                liste.append(saat)
                liste.append(milisaniye)
                if len(milisaniye)<3 or milisaniye == None:
                    liste.append("\t")
                    liste.append(" ")
                #Kilogram

                liste.append("\t")
                liste.append("\t")
                liste.append(kilogram)
                liste.append("\n")


        else:                                 #Milisaniye
            milisaniye = veri


    convert = "".join([str(k) for k in liste])


edited_data = open("edited_data.txt", "w")
edited_data.write(convert)
edited_data.close()

