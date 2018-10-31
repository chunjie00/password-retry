password = '19961017'
i = 3
while i > 0:
	pwd = input('请输入陆晓婧的生日:')
	if pwd == password:
		print('回答正确!')
		break
	else:
		i = i - 1
		print('回答错误!')
		if i > 0:
			print('还剩余', i ,'次机会')
		else:
			print('陆晓婧即将到达战场!')
