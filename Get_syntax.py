import lists

def get_syntax(Syntax):
	if Syntax == 'basic html' or Syntax == 'html': #machine learning to learn these
		print(*HTML_BASIC)
	elif Syntax == 'heading':
		print(*lists.HTML_HEADINGS)
	else:
		print('Sorry syntax for this is not avaliable '+Syntax)
		#add a make a pull request function
syntax_of = input(str('What HTML Syntax you Want to see : '))
print(syntax_of)
get_syntax(syntax_of)
