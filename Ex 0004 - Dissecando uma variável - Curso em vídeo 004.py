variable_in = input("\nWrite a text:\n\n")

print(f'What is the primitive type?: {type(variable_in)}'
      f'\nThere is only space?:    {variable_in.isspace()}'
      f'\nIs it numberic?:     {variable_in.isnumeric()}'
      f'\nIs it alphabetic?: {variable_in.isalpha()}'
      f'\nIs it UPPERCASE?:    {variable_in.isupper()}'
      f'\nIs it lowercase?:    {variable_in.islower()}'
      f'\nIs it Capitalized?:   {variable_in.istitle()}\n\n\n')
