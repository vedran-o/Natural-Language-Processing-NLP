main_list = ['aba', 'baba', 'curac', 'dikinson']
check_elements = ['ba', 'baba', 'dikinson']

tokens_without_sw = [word for word in main_list if word not in check_elements]
print(tokens_without_sw)