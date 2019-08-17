grid=[]
for _ in range(20):
	row=list(map(str,input().split( )))
	grid.append(row)
for i in range(20):
	for j in range(20):
		grid[i][j]=int(grid[i][j])
pro=1
for i in range(20):
	for j in range(20):
		if j<17:
			p=int(grid[i][j])*int(grid[i][j+1])*int(grid[i][j+2])*int(grid[i][j+3])
			if p>pro:
				pro=p
				a=(i,j)
				b=(i,j+1)
				c=(i,j+2)
				d=(i,j+3)

		if i<17:
			p=int(grid[i][j])*int(grid[i+1][j])*int(grid[i+2][j])*int(grid[i+3][j])
			if p>pro:
				pro=p
				a=(i,j)
				b=(i+1,j)
				c=(i+2,j)
				d=(i+3,j)
		if i<17 and j>=3:
			p=int(grid[i][j])*int(grid[i+1][j-1])*int(grid[i+2][j-2])*int(grid[i+3][j-3])
			if p>pro:
				pro=p
				a=(i,j)
				b=(i+1,j-1)
				c=(i+2,j-2)
				d=(i+3,j-3)

		if i<17 and j<17:
			p=int(grid[i][j])*int(grid[i+1][j+1])*int(grid[i+2][j+2])*int(grid[i+3][j+3])
			if p>pro:
				pro=p
				a=(i,j)
				b=(i+1,j+1)
				c=(i+2,j+2)
				d=(i+3,j+3)

print(pro)
print(a)
print(b)
print(c)
print(d)
