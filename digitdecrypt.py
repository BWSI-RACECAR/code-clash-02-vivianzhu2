class Solution:    
    def digitdecrypt(self, num):
            #type num: int
            #return type: int
            # temp=0
            # digitlist=[]
            # i=0
            # #TODO: Write code below   to returnn an int with the solution to the prompt.
            # while(num%10!=0):
            #     digitlist[i]= num%10
            #     num/=10
            #     i+=1
            # sum=0
            # digitlist=digitlist[::-1]
            # print(digitlist)
            # for i in range(0,digitlist-1):
            #      sum+= digitlist[i]
            # if(sum>10):
            #      digitdecrypt(sum)
            # else:
            #      return sum
            while(num>0):
                dig_list= [int[i]for i in str(num)]
                num=0
                for i in avg_list:
                  num=num+1
            return num
def main():
    input1= input()
    input2 = int(input1)

    
    tc1 = Solution()
    ans = tc1.digitdecrypt(input2)
    print(ans)
    
if __name__ == "__main__":
    main()