import math 
    
# Returns the lcm of first n numbers  
def lcm(n):  
    ans = 1
    for i in range(1, n + 1):  
        ans = int((ans * i)/math.gcd(ans, i))
        #print(ans)          
    return ans  
if __name__ == '__main__':
	res=lcm(20)
	print(res)