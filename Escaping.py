#вывод текста двух переменных
some_string0="i'm a aaaaaaaa"
print(some_string0)
another_string0='i want to learn "python'
print (another_string0)
#i'm a aaaaaaaa
#i want to learn "python
enter='\n' #два пустых абзаца для разрыва сплошной стены текста
print(enter)
#
#escaping \ - чтобы можно было ставить кавычки в выводимом тексте.
some_string='i\'m a aaaaaaaa'
print (some_string)
another_string="i want to learn \"python\""
print (another_string)
#i'm a aaaaaaaa ; i want to learn "python"
enter='\n'
print(enter)
#
string_with_new_line='helllo \n My name is A'
print (string_with_new_line)

string_with_new_line='helllo \n \rMy name is A' #отсутствие отступа перед второй строкой
print (string_with_new_line)
#	Hello! 
#	I'm aaaaa!
#
enter1='\t' #один пустой абзац для разрыва сплошной стены текста
print(enter1)
#
numbers='1\t2345'     #отступы Tab в строке между символами
print (numbers)
abzac="\tHello! \n\tI'm aaaaa!"    #отступы и выравнивание отступов относительно друг друга
print (abzac)
#
