import re

print(""" 
Welcome to madlib game!

all you need is to think of an example of the below vocabs 
""")

vocabs_list=['Adjective','Adjective','A First Name','Past Tense Verb','A First Name','Adjective','Adjective',
'Plural Noun','Large Animal','Small Animal',"A Girl's Nam",'Adjective','Plural Noun','Adjective','Plural Noun',
'Number 1-50',"First Name's",'Number','Plural Noun','Number','Plural Noun']

input_list=[]

def input_vocabs():
    for i in range (len(vocabs_list)):
        input_val=input('>> Enter %s  '%(vocabs_list[i]))
        input_list.append(input_val)

input_vocabs()  



def read_template():
    with open('../assets/script.txt') as file:
        return file.read()

read_script=read_template()


def parse_template():
    modified_script=re.sub('{[^}]+}','{}',read_script)
    removed_str_parts=re.findall('{[^}]+}',read_script)
    return  modified_script, removed_str_parts

parsed_script=parse_template()


def merge():
    return parsed_script[0].format(*input_list)

merged_script=merge()



def copied_script():
    with open('../assets/script_copy.txt', 'wb') as script_write:
         return script_write.write(bytes(merged_script,'utf-8'))

copied_script()
