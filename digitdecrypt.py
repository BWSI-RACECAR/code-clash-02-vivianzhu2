class Solution:    
    def digitdecrypt(self, num):
            #type num: int
            #return type: int
            # temp=0
            digitlist=[]
            i=0
            # #TODO: Write code below   to returnn an int with the solution to the prompt.
            while(num//10!=0):
                digitlist.append(num%10)
                num=num//10
                i+=1
            sum=0
           # digitlist=digitlist[::-1]
            #print(digitlist)
            for i in range(0,len(digitlist)):
                 sum+= digitlist[i]
            #print(sum)
            if(sum>10):
                 return self.digitdecrypt(sum)
            else:
                 return sum
            # if num<0:
            #     raise ValueError("Invalid argument. Please enter a positive integer.")
            # while(num>9):
            #     dig_list= [int[i]for i in str(num)]
            #     num=0
            #     for i in dig_list:
            #       num=num+1
            # return num
def main():
    input1= input()
    input2 = int(input1)

    
    tc1 = Solution()
    ans = tc1.digitdecrypt(input2)
    print(ans)
    
if __name__ == "__main__":
    main()