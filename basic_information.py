# In[]
import tkinter as tk
from tkinter import ttk
from Bio.Seq import Seq
from Bio.SeqUtils import GC
from Bio.Alphabet import IUPAC
from Bio import Entrez
from Bio import SeqIO
from primer3 import calcTm
# pip install biopython
# pip install Cython
# pip install primer3-py

root = tk.Tk()
root.title('Seq APP GUI(input ID)')
root.geometry('800x600')
#root.configure(background='white')

#label title 
header_label = tk.Label(root, text='Seq Analysis',fg='white',bg='grey',font=('Ink free',18))
header_label.pack()


def ID():
    id = IDseq.get()
    Entrez.email = str(email.get())
    result_handle = Entrez.efetch(db="nucleotide", rettype="gb",  id=str(id))
    seqRecord = SeqIO.read(result_handle, format='gb')
    global idseq
    idseq = seqRecord.seq
    result_frame.insert('end','Get Sequence Success!')
#Entrez.email = 'address@gmail.com'
#mRNA_id = "EU490707"

# Input block
ID_frame = tk.Frame(root)
ID_frame.pack()
# DNA ID
ID_label = tk.Label(ID_frame, text = 'DNA ID ',font=('Arial',12))
ID_label.pack(side='left')

IDseq = tk.StringVar()
ID_entry = tk.Entry(ID_frame,fg='blue',textvariable=IDseq ,bg='white',width=30)
ID_entry.pack(side='left')
# email
email_label = tk.Label(ID_frame, text = 'Email ',font=('Arial',12))
email_label.pack(side='left')
email = tk.StringVar()
email_entry = tk.Entry(ID_frame,fg='blue',textvariable=email ,bg='white',width=50)
email_entry.pack(side='left')
# get seq
clear_btn = tk.Button(ID_frame,text='Get Sequence',command=ID,font=('Arial',8))
clear_btn.pack()

def basic_info():
    seq = idseq
    seq_len = str(len(seq))
    seq_gcount = str(seq.count('G'))
    seq_gc = str(GC(seq))
    seq_ta = str(seq.count('TA'))
    result_frame.insert('end',
                        '\n\nLength: '+seq_len+'\nG Counts: '+seq_gcount+
                        '\nGC contents: '+seq_gc+
                        '\nTA contents: '+seq_ta+'\n')

def primer():
    seq = idseq
    forward_pr = seq[:20]
    forw_len = str(len(forward_pr))
    forw_gc = str(GC(forward_pr))
#    forw_tm = str(calcTm(forward_pr))
    reverse_pr = seq[-20:].reverse_complement()
    rev_len = str(len(reverse_pr))
    rev_gc = str(GC(reverse_pr))
#    rev_tm = str(primer3.calcTm(reverse_pr))
    result_frame.insert('end','\n\n----------Forward----------\n'+
                        'Sequence: '+forward_pr+
                        '\nLength: '+forw_len+
                        '\nGC content: '+forw_gc+
                        '\n----------Reverse----------\n'+
                        'Sequence: '+reverse_pr+
                        '\nLength: '+rev_len+
                        '\nGC content: '+rev_gc)

#    print("Forward_primer Tm 值為",primer3.calcTm(forward_pr)) #Primer Tm測試
#    print("Forward_primer Tm 值為",primer3.calcTm(reverse_pr)) #Primer Tm測試    

def transcribe_info():
    seq = idseq
    seq_rna = str(seq.transcribe())
    result_frame.insert('end','\nRNA: \n'+seq_rna+'\n')

def translate_info():
    seq = idseq
    seq_prot = str(seq.translate())
    result_frame.insert('end','\nProtein: \n'+seq_prot)

# calculate
Info_btn = tk.Button(root,text='Basic Information',command=basic_info)
Info_btn.pack()
RNA_btn = tk.Button(root,text='Transcribe',command=transcribe_info)
RNA_btn.pack()
PROT_btn = tk.Button(root, text='Translate',command=translate_info)
PROT_btn.pack()
Prim_btn = tk.Button(root, text='Primer Design',command=primer)
Prim_btn.pack()

# result 
result_frame = tk.Text(root,bd=5,width = 100, height = 20)
result_frame.pack()

# address@gmail.com
# EU490707

# clear
clear_btn = tk.Button(root,text='Clear',command=lambda: result_frame.delete('1.0',tk.END))
clear_btn.pack()

root.mainloop()
# In[] demo from http://kaiching.org/pydoing/py/python-library-tkinter.html
# In[ ]
dna_seq = Seq("GGATGGTTGTCTATTAACTTGTTCAAAAAAGTATCAGGAGTTGTCAAGGCAGAGAAGAGAGTGTTTGCA", IUPAC.unambiguous_dna)
# In[]
from Bio import Entrez
from Bio import SeqIO
import os

mRNA_id = "EU490707" #RNA_id
file_out_name= mRNA_id+".fasta"
Entrez.email = 'r08b48004@g.ntu.edu.tw' #改自己email
output_file=open(file_out_name,"a")

record_id= mRNA_id
result_handle = Entrez.efetch(db="nucleotide", rettype="gb",  id=record_id)
seqRecord = SeqIO.read(result_handle, format='gb')
result_handle.close()
output_file.write(seqRecord.format('fasta'))

output_file.close()
if os.path.isfile(file_out_name):
    print(file_out_name,"下載完成")

# In[]
from Bio.Seq import Seq
from Bio.SeqUtils import GC
from Bio import SeqIO
from primer3 import calcTm

for record in SeqIO.parse("EU490707.fasta","fasta"):
    print(record.id, str(record.seq[:20]), str(record.seq[-20:].reverse_complement()))
    forward_pr = str(record.seq[:20])
    reverse_pr = str(record.seq[-20:].reverse_complement())
    
print("-------------Forward區-----------------")
print("Sequence: ", forward_pr)
print ("Length : ", len(forward_pr))
print("GC contens: ", GC(forward_pr))
print("Forward_primer Tm 值為",calcTm(forward_pr)) #Primer Tm測試

print("-------------Reverse區-----------------")
print("Sequence: ", reverse_pr)
print ("Length : ", len(reverse_pr))
print("GC contens: ", GC(reverse_pr))
print("Forward_primer Tm 值為",calcTm(reverse_pr)) #Primer Tm測試
    

# In[]
import tkinter as tk
from tkinter import ttk
from Bio.Seq import Seq
from Bio.SeqUtils import GC
from Bio.Alphabet import IUPAC
from Bio import Entrez
from Bio import SeqIO
from primer3 import calcTm


root = tk.Tk()
root.title('Seq APP GUI(input sequence)')
root.geometry('800x600')

#label title 
header_label = tk.Label(root, text='Seq Analysis',fg='white',bg='grey',font=('Ink free',18))
header_label.pack()

IP_frame = tk.Frame(root)
IP_frame.pack(fill='x')
IP_label = tk.Label(IP_frame, text = 'DNA Sequence',font=('Arial',12))
IP_label.pack()
IPseq = tk.StringVar()
IP_entry = tk.Entry(IP_frame,fg='blue',textvariable=IPseq ,bg='white',width=50)
IP_entry.pack(fill='x')

def basic_info():
    seq = IPseq.get().upper()
    seq = Seq(str(seq),IUPAC.unambiguous_dna)
    seq_len = str(len(seq))
    seq_gcount = str(seq.count('G'))
    seq_gc = str(GC(seq))
    seq_reverse = str(seq[::-1])
    seq_RevComplement = str(seq.complement())
    seq_ta = str(seq.count('TA'))
    result_frame.insert('end','Sequence: '+seq+'\nReverse:  '+seq_reverse+
                        '\nReverse Complement: '+seq_RevComplement+
                        '\n\nLength: '+seq_len+'\nG Counts: '+seq_gcount+
                        '\nGC contents: '+seq_gc+
                        '\nTA contents: '+seq_ta+'\n')

def primer():
    seq = IPseq.get().upper()
    seq = Seq(str(seq),IUPAC.unambiguous_dna)
    forward_pr = seq[:20]
    forw_len = str(len(forward_pr))
    forw_gc = str(GC(forward_pr))
#    forw_tm = str(calcTm(forward_pr))
    reverse_pr = seq[-20:].reverse_complement()
    rev_len = str(len(reverse_pr))
    rev_gc = str(GC(reverse_pr))
#    rev_tm = str(primer3.calcTm(reverse_pr))
    result_frame.insert('end','\n\n----------Forward----------\n'+
                        'Sequence: '+forward_pr+
                        '\nLength: '+forw_len+
                        '\nGC content: '+forw_gc+
                        '\n----------Reverse----------\n'+
                        'Sequence: '+reverse_pr+
                        '\nLength: '+rev_len+
                        '\nGC content: '+rev_gc)

def transcribe_info():
    seq = IPseq.get().upper()
    seq = Seq(str(seq),IUPAC.unambiguous_dna)
    seq_rna = str(seq.transcribe())
    result_frame.insert('end','\nRNA: \n'+seq_rna+'\n')
    
def translate_info():
    seq = IPseq.get().upper()
    seq = Seq(str(seq),IUPAC.unambiguous_dna)
    seq_prot = str(seq.translate())
    result_frame.insert('end','\nProtein: \n'+seq_prot)

# GGATGGTTGTCTATTAACTTGTTCAAAAAAGTATCAGGAGTTGTCAAGGCAGAGAAGAGAGTGTTTGCA

# calculate
Info_btn = tk.Button(root,text='Basic Information',command=basic_info)
Info_btn.pack()
RNA_btn = tk.Button(root,text='Transcribe',command=transcribe_info)
RNA_btn.pack()
PROT_btn = tk.Button(root, text='Translate',command=translate_info)
PROT_btn.pack()
Prim_btn = tk.Button(root, text='Primer Design',command=primer)
Prim_btn.pack()

# result 
result_frame = tk.Text(root,bd=5,width = 100, height = 20)
result_frame.pack()

# clear
clear_btn = tk.Button(root,text='Clear',command=lambda: result_frame.delete('1.0',tk.END))
clear_btn.pack()

root.mainloop()
