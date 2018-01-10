def decrypt(string):
    # loop that will test each value between -25 & 25
    for i in range(-25, 26):
        # initialized variable to empty string
        newMessage = ''
        # loop that will iterate through each character in the string
        for j in string:
            # converts each character and shifts ASCII code by i
            newMessage += chr(ord(j) + i)
        # checks each message for and, not or the and prints the message and shift key
        if newMessage.find('and') != -1 or newMessage.find('the') != -1 or \
           newMessage.find('not') != -1:
            print("The key is:", i)
            print(newMessage)
            return


message1 = "M[h[@e^ddo#Yec[#bWj[b_[i$M[b_l[_dj^[Yeic_YXeedZeYai$M[[c[h][Z\hecc_YheX" \
           "[iWdZckYa$7f[iWh[ekhYeki_di$Ekhj^ek]^jiWdZ\[[b_d]iWh[dej\kbbokdZ[hekhemdYed" \
           "jheb$J^[h[cWoX[ckY^icWhj[hWdZl[hoZ_\\[h[djX[_d]i[bi[m^[h[$7dZedjefe\Wbbj^_im[h" \
           "[cWa_d]Wc[iie\ekhfbWd[jWdZX[Yec_d]WZWd][hjeekhi[bl[i$"

decrypt(message1)

# inserted additional backslashes to counter escapes or escape quotes
message2 = "=djgjbdnonjao`io\gf\]jpooc`\"`^jgjbt\"ja\ijmb\idnh5oc`o\gg`no\\fdioc`ajm`nod" \
           "noc`o\gg`noijoepno]`^\pn`dobm`ramjhoc`c\m_d`no\^jmi6dodnoc`o\gg`no\gn" \
           "j]`^\pn`ijjoc`mom``n]gj^f`_donnpigdbco'oc`njdg\mjpi_dor\\n_``k\i_md^c'ij" \
           "m\]]do^c`r`_ocmjpbcdon]" \
           "\mf\\n\\n\kgdib'\i_ijgph]`me\^f^podo_jri]`ajm`doh\opm`_)"

decrypt(message2)
