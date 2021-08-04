import pandas as pd
import streamlit as st
import altair as alt

st.write("""
         
         # DNA Nucleotide Count Web App
         
         This app counts counts the nucleotide composition of query DNA! 
         
         Uses Pandas, altair, and streamlit.
         
         
         """)


st.header('Enter DNA sequence')

sequence_input = ">DNA Query \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

    
    
sequence = st.text_area("Sequence input", sequence_input, height=250).upper()
sequence = sequence.splitlines()
#sequence #prints the sequence in split newlines
sequence = sequence[1:] #skips the sequence name
sequence = ''.join(sequence)


st.write("""
         ***
         """)

st.header('INPUT (DNA Query)')

sequence

    

st.header('OUTPUT (DNA Nucleotide Count)')

###Print dictionary
st.subheader('1. Print dictionary')

def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X

###Print text
st.subheader('2. Print Text')

st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

###Display dataframe
st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(X, orient='index') # make dataframe
df = df.rename({0: 'count'}, axis='columns') # rename the 0 col to = count
df.reset_index(inplace=True) # reset to have a index
df = df.rename(columns = {'index': 'nucleotide'}) # rename that new index to nucleotide
st.write(df)

###Display Bar Chart
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
)

p = p.properties(
    width = alt.Step(80)
)

st.write(p)
