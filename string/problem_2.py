letter='''
Dear <|Name|>,
you are selected!
<|Date|>
'''
letter=letter.replace("<|Name|>","Binit")
letter=letter.replace("<|Date|>","20 june")
print(letter)