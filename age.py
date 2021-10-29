drving = input('請問你有沒有開過車?:')
if drving != '有' and drving != '沒有':
	print('請輸入有或沒有')
	raise SystemExit
age = input('請問你的年齡:')
age = int(age)
if drving == '有':
	if age >= 18:
		print('通過測試')
	else:
	    print('無照駕駛')
elif drving == '沒有':
	if age >= 18:
		print('可以考駕照')
	else:
		print('乖乖搭公車')