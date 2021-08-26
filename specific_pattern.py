#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !/usr/bin/env python
import pandas as pd


def filter_seq_res(l,x1,x2,x3): # l 僅做標記
    result = 'no'
    percentage = 0
    if x1>=aa1p and x2>=aa2p and x3>=aa3p: #找三種aa
        result = 'yes'
        percentage = round(x1,2),round(x2,2),round(x3,2)
        #print(percentage)
        if aa2 == 'nothing': #如果只給一個aa，只印出一個percentage
            percentage = round(x1,2)        
            #print(percentage)
        elif aa2 != 'nothing' and aa3 == 'nothing': #如果只給兩個aa，只印出兩個percentage
            percentage = round(x1,2),round(x2,2)
            #print(percentage)
    return result,percentage
            


def filter_seq_total(l,x1,x2,x3): # l 僅做標記
    result = 'no'
    percentage = 0
    # x4 為3個胺基酸加起來總和比例
    x4 = x1 + x2 + x3
    
    if x4 >= aap:#找三種aa             
        result = 'yes'
        percentage = round(x1,2),round(x2,2),round(x3,2)
        if aa2 == 'nothing': #如果只給一個aa，只印出一個percentage
            percentage = round(x1,2)
        elif aa2 != 'nothing' and aa3 == 'nothing': #如果只給兩個aa，只印出兩個percentage
            percentage = round(x1,2),round(x2,2)
    return result,percentage

#確認是否為整數 用float()將內容文字轉成小數，若可以轉代表為數字，再進一步確認除以1的餘數是否為0，以確認是否為整數
def is_number(s):
    try:  
        s = float(s)
        if s%1 != 0:
            return False
        else:
            return True
    except ValueError:  # ValueError 傳入無效參數
        pass  
    try:
        import unicodedata 
        for i in s:
            unicodedata.numeric(i)  # 
            #return True
        return True
    except (TypeError, ValueError):
        pass
    return False

#確認是否為小數 
def is_float(s):
    try:  
        s = float(s)
        return True
    except ValueError:  # ValueError 傳入無效參數
        pass  
    try:
        import unicodedata 
        for i in s:
            unicodedata.numeric(i)  # 
            #return True
        return True
    except (TypeError, ValueError):
        pass
    return False

species = ['Arabidopsis thaliana','Bacillus subtilis','Escherichia coli','Homo sapiens',
           'Klebsiella pneumoniae','Listeria monocytogenes','Mus musculus','Saccharomyces cerevisiae','Salmonella enterica',
          'Staphylococcus aureus','Streptococcus agalactiae']
while True:
    print('Species availabled:\n')
    i = 1
    for spe in species:
        print(f'{i}) {spe}')
        i+=1

    
    #物種序列
    try:
        int_list = ['1','2','3','4','5','6','7','8','9','10','11']
        password = 'No'
        while password != 'ok':
            spec_num = input('Select the species number: ')
            if spec_num in int_list:
                spec_num = int(spec_num)
                password = 'ok'
            else:
                print("\n※Please enter the number from 1~11")
                
    except:
        print("\n※Please enter the number from 1~11")
    spec = species[spec_num-1]
    #print(spec)
    seq_file = f'./species/{spec}.txt'
    

    titles =[]
    seq_final =[]
    seq_line = ''
    with open(seq_file, 'r') as f:
        for line in f:
            line = line.replace('\n','')
            if line.startswith('>') or line.startswith('"'):
                titles.append(line)
                seq_final.append(seq_line)
                seq_line = ''
            else:
                seq_line += line.strip('\n')
    seq_final = seq_final[1:] 

              
    
    #查找amino acid的區間
    
    try:
        while password!= 'ok2':
            s_len = input('Analyze every x amino acids:')
            if is_number(s_len) == True:
                s_len =  int(s_len)
                password = 'ok2'
            else:
                print("\n※Please enter the integer")
            
    except:
        print("\n※Please enter the integer")
    
    #選擇胺基酸數目
    try:
        int_list = ['1','2','3']
        while password!='ok3':
            print('\nEnter the number of the searching amino acids')
            aa_num = input("\nFrom number 1 ~ 3: ")
            if aa_num in int_list:
                aa_num = int(aa_num)
                password = 'ok3'
            else:
                print("\n※Please enter the number from 1~3")
    except:
        print("\n※Please enter the number from 1~3")
                
    #選擇分析總和或是個別 
    try:
        int_list = ['1','2']
        while password !='ok4':
            print('\nAnalyze the sum percentage or respective percentage')
            print('\n1) Sum percentage 2) Respective percentage')
    
            option = input('')
            if option in int_list:
                option = option
                password = 'ok4'
            else:
                print("\n※Please enter the number from 1~2")
    except:
        print("\n※Please enter the number from 1~2")    
        
    #選擇總和
    if option == '1':
        int_list = ['A','F','C','U','D','N','E','Q','G','H','L','I','K','O','M','P','R','S','T','V','W','Y']
        try:            
            while password!='ok5':
                print('\nPlease enter the amino acids')
                aa1 = input('First amino acid (ex: D): ').upper()
                if aa1 in int_list:
                    password='ok5'
                else:
                    print('\n※Please enter the amino acid abbreviation')
        except:
            print('\n※Please enter the amino acid abbreviation')
        
        if aa_num >1:
            try:
                while password!='ok6':
                    aa2 = input('Second amino acid :').upper()
                    if aa2 in int_list and aa2 != aa1:
                        password='ok6'
                    else:
                        print('\n※Please enter the non-repetitive amino acid abbreviation')
            except:
                print('\n※Please enter the non-repetitive amino acid abbreviation')
        else:
            aa2 = 'nothing' #為了讓c2=0
            aa2p = 0
            
        if aa_num >2:
            try:
                while password!='ok7':
                    aa3 = input('Third amino acid :').upper()
                    if aa3 in int_list and aa3!=aa1 and aa3!=aa2:
                        password='ok7'
                    else:
                        print('\n※Please enter the non-repetitive amino acid abbreviation')
            except:
                print('\n※Please enter the non-repetitive amino acid abbreviation')
        else:
            aa3 = 'nothing' #為了讓c3=0
            aa3p = 0
        
        #aap = 0
        try:
            while password !='ok8':
                aap = input('Please enter the percentage for the sum of above amino acids:')
                if is_float(aap) == True:
                    aap =float(aap)
                    if aap <= 1 :
                        password = 'ok8'                    
                    else:
                        print('\n※The percentage need to be less than 1 ')
                else:
                    print('\n※Please enter the float')
        except:
            print('\n※Please enter the float')
    
    #選擇個別
    elif option == '2':
        int_list = ['A','F','C','U','D','N','E','Q','G','H','L','I','K','O','M','P','R','S','T','V','W','Y']
        
        try:
            
            while password !='ok9':
                print('\nPlease enter the amino acids and their respective percentage')
                aa1 = input('First (ex: D): ').upper()
                aa1p = input('Percentage requirement for %s (ex: 0.2): ' %aa1)
                if aa1 in int_list:
                    if is_float(aa1p) == True:
                        aa1p = float(aa1p)
                        if aa1p <= 1 :
                            password = 'ok9'
                        else:
                            print('\n※The percentage need to be less than 1 ')
                    else:
                        print('\n※Please enter the float')
                else:
                    print('\n※Please enter the amino acid abbreviation')
        except:
            print('\n※Please enter the amino acid abbreviation')
        
        
        if aa_num >1:
            try:
                while password !='ok10':
                    aa2 = input('Second amino acid:').upper()
                    aa2p = float(input('Percentage requirement for %s: ' %aa2)) 
                    if aa2 in int_list and aa2 != aa1:
                        if is_float(aa2p) == True:
                            aa2p = float(aa2p)
                            if aa2p <= 1 :
                                password = 'ok10' 
                            else:
                                print('\n※The percentage need to be less than 1 ')
                        else:
                            print('\n※Please enter the float')
                    else:
                        print('\n※Please enter the non-repetitive amino acid abbreviation')
            except:
                print('\n※Please enter the amino acid abbreviation')
                    
        else:
            aa2 = 'nothing' #為了讓c2=0
            aa2p = 0
            
        if aa_num >2:
            try:
                while password!='ok11':
                    aa3 = input('Third amino acid:').upper()
                    aa3p = float(input('Percentage requirement for %s: ' %aa3))
                    if aa3 in int_list and aa3 != aa2 and aa3!=aa1:
                        if is_float(aa3p) == True:
                            aa3p = float(aa3p)
                            if aa3p <= 1 :
                                password = 'ok11' 
                            else:
                                print('\n※The percentage need to be less than 1 ')
                        else:
                            print('\n※Please enter the float')
                    else:
                        print('\n※Please enter the non-repetitive amino acid abbreviation')
            except:
                print('\n※Please enter the amino acid abbreviation')
        else:
            aa3 = 'nothing' #為了讓c3=0
            aa3p = 0

    

    #選擇輸出檔名
                    
    #%%           
    output = input('Save output file name as "%s_output.fasta"\n    Press enter to continue or enter a new file name:' %(spec))+'.fasta'
    if output == '.fasta':
        output = '%s_output.fasta' %spec
        output2 = '%s_output.xlsx' %spec
    #先清空output
    with open(output,'w') as f2, open(output2, 'w') as f3:
        f2.truncate()
        f3.truncate()
        
    #創建dataframe

    if aa_num == 3:
        df = pd.DataFrame(columns = ["ID", "Sequence", aa1,aa2,aa3,"Total length", "Start","End"])
    elif aa_num == 2:
        df = pd.DataFrame(columns = ["ID", "Sequence", aa1,aa2,"Total length" ,"Start","End"])
    elif aa_num == 1:
        df = pd.DataFrame(columns = ["ID", "Sequence", aa1,"Total length", "Start","End"])
        
    with open(output,'a') as f2, open(output2, 'a') as f3:
        for i1,i2 in zip(titles,seq_final):
            #若protein序列少於100個胺基酸 就直接算整個的比例 ##100 為可換區間
            if len(i2) <= s_len: #100
                if len(i2) <= s_len: #若長度不滿所要區間
                    c1 = i2.count(aa1)
                    c2 = i2.count(aa2)
                    c3 = i2.count(aa3)
                    x1 = c1/len(i2)
                    x2 = c2/len(i2)
                    x3 = c3/len(i2)
                    
                    if option == '1':
                        result,percentage = filter_seq_total('short',x1,x2,x3)
                        if result == 'yes':
                            print(i1,file=f2)
                            print(i2,file=f2)
                            if aa_num == 3:
                                df = df.append({'ID':i1,'Sequence':i2,aa1:percentage[0],aa2:percentage[1],aa3:percentage[2],"Total length":len(i2),'Start':1,'End':len(i2)},ignore_index=True)

                            elif aa_num == 2:
                                df = df.append({'ID':i1,'Sequence':i2,aa1:percentage[0],aa2:percentage[1],"Total length":len(i2),'Start':1,'End':len(i2)},ignore_index=True)

                            elif aa_num == 1:
                                df = df.append({'ID':i1,'Sequence':i2,aa1:percentage[0],"Total length":len(i2),'Start':1,'End':len(i2)},ignore_index=True)

                            
                    elif option =='2':
                        result,percentage = filter_seq_res('short',x1,x2,x3)
                        if result == 'yes':
                            print(i1,file=f2)
                            print(i2,file=f2)
                            if aa_num == 3:
                                df = df.append({'ID':i1,'Sequence':i2,aa1:percentage[0],aa2:percentage[1],aa3:percentage[2],"Total length":len(i2),'Start':1,'End':len(i2)},ignore_index=True)

                            elif aa_num == 2:
                                df = df.append({'ID':i1,'Sequence':i2,aa1:percentage[0],aa2:percentage[1],"Total length":len(i2),'Start':1,'End':len(i2)},ignore_index=True)

                            elif aa_num == 1:
                                df = df.append({'ID':i1,'Sequence':i2,aa1:percentage[0],"Total length":len(i2),'Start':1,'End':len(i2)},ignore_index=True)
                         
                    #D = i2.count('D')
                    #E = i2.count('E')
                    #x1 = D/len(i2)
                    #x2 = E/len(i2)       
                    
            else:
                times = len(i2) - (s_len) +1  #先計算需要算幾次才能輪完整個protein  ##100 為可換區間
                origin = 0
                count_list = []

                while origin <= times:
                    origin+=1
                    c1 = i2[origin:origin+s_len].count(aa1)
                    c2 = i2[origin:origin+s_len].count(aa2)
                    c3 = i2[origin:origin+s_len].count(aa3)
                    x1 = c1/s_len
                    x2 = c2/s_len
                    x3 = c3/s_len
                    
                    if option == '1':
                        result,percentage = filter_seq_total('long',x1,x2,x3)
                        if result =='yes':
                            count_list.append([percentage,origin,origin+100])
                    elif option =='2':
                        result,percentage =  filter_seq_res('long',x1,x2,x3)
                        if result == 'yes':
                            count_list.append([percentage,origin,origin+100])
                    
                
                #將結果排序，最大的排前面
                
                if aa_num == 3:
                    count_list.sort(reverse=True,key = lambda s: s[0][0]+s[0][1]+s[0][2])
                elif aa_num == 2:
                    count_list.sort(reverse=True,key = lambda s: s[0][0]+s[0][1])
                elif aa_num == 1:
                    count_list.sort(reverse=True,key = lambda s: s[0][0])
                    
                    
                #若是其中有發現到超過比例的，下面這個List就不會為空，因此就會將其存到output中
                if count_list:
                    print(i1,file=f2)
                    print(i2,file=f2)
 
                    
                    if aa_num == 3:
                        df = df.append({'ID':i1,'Sequence':i2,aa1:count_list[0][0][0],aa2:count_list[0][0][1],aa3:count_list[0][0][2],"Total length":len(i2),'Start':count_list[0][1],'End':count_list[0][2]},ignore_index=True)
                    elif aa_num == 2:
                        df = df.append({'ID':i1,'Sequence':i2,aa1:count_list[0][0][0],aa2:count_list[0][0][1],"Total length":len(i2),'Start':count_list[0][1],'End':count_list[0][2]},ignore_index=True)
                    elif aa_num == 1:
                        df = df.append({'ID':i1,'Sequence':i2,aa1:count_list[0][0][0],"Total length":len(i2),'Start':count_list[0][1],'End':count_list[0][2]},ignore_index=True)
                    
    print('\nPlease check the output file!')
    
    #將結果寫到excel檔裡
    #print(df)
    writer = pd.ExcelWriter(output2, engine = 'xlsxwriter')
    df.to_excel(writer, sheet_name = 'top_sequence')
    worksheet = writer.sheets['top_sequence']
    worksheet.set_column('B:B', 100) 
    worksheet.set_column('C:H', 18) 
    workbook = writer.book

    writer.save()
    try:
        int_list = ['Y','N']
        while password !='ok12':
            again = input('Do you want to do another analysis [Y]/N ?').upper()
            if again in int_list:
                password = 'ok12'
            else:
                print('\n※Please enter Y or N')
    except:
        print('\n※Please enter Y or N')
    if again == 'N':
        print('\nThank you!')
        break
    
    

