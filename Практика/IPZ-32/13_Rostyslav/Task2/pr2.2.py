def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]  
        for j in range(1, i):
            
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        if i > 0:
            row.append(1)  
        triangle.append(row)
    return triangle

n = 10
triangle = pascal_triangle(n)
for row in triangle:
    print(row)