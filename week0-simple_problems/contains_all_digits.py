def contains_digits(number, digits):
	return(set(digits).issubset(set(number_to_list(number))))
	#return digits in number_to_list(number) 


def number_to_list(n):
	list=[]
	my_number=n
	while (my_number>0):
		my_digit=my_number%10	
		list = [my_digit] + list			
		my_number=my_number // 10
		#print(n)
	return list


def  main():
	print(contains_digits(402123, [0,3,4]))
	print(contains_digits(666, [6,4]))
	print(contains_digits(123456789, [1,2,3,0]))
	print(contains_digits(456, []))

if __name__ == '__main__':
	main()