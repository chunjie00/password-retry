password = 'a123456'
i = 3
while i > 0:
	pwd = input('请输入密码:')
	if pwd == password:
		print('登陆成功!')
		break
	else:
		i = i - 1
		print('密码错误!还剩余', i ,'次机会')
