
import argparse
import sys
import numpy as np
import argparse  
import random
import numpy as np
'''用于简单level-k 博弈理论分析'''
'''问每个人：从给定 0 到 100 的整数范围内，猜测一个最接近所有猜测数字平均数 2/3 的整数。即倘若所有猜测数的平均是 60，那么正确的猜测将会是 40。你认为哪个数字会是平均数 2/3 的正确猜测呢？
   称为“ k 级推理”。其中 k 代表一个推理周期的重复次数。一个 k 级为 0 的人会非常天真地参与我们的博弈，他不会考虑别人的选择而只是任意地猜一个数字。一个 k 级为 1 的人会假设别人都在 0 级博弈，进而平均数为 50，因此猜测数为 33。一个 k 级为 2 的人会假设其他人都在 1 级博弈，导致他们最终猜测数为 22。'''
#https://baijiahao.baidu.com/s?id=1663101694696905100

def runGameOnce_A(numPlayer,levelRatio,numRounds):
    #轮数序号,每个人的出牌，每个人的收益
    playerRecord1= [0]*numRounds
    
    
    for i in range(numRounds):
        print("round:",i)
        # 定义数字列表和对应的概率分布
        levelType = [0, 1, 2, 3, 4]
        probabilities =levelRatio

        # 使用random.choice函数生成指定数字
        generated_type = np.random.choice(levelType, p=probabilities,size=10).tolist()
       
        print('type:',generated_type)
        
        cards = [0]*numPlayer#每个人的出牌
        income = [0]*numPlayer#每个人的收益
        
        for j in range(numPlayer):
            typeT = generated_type[j]
            if typeT  == 0:
                showCard = random.randint(0, 100)
            if typeT  == 1:
                showCard = 33
            if typeT  == 2:
                showCard = 22
            cards[j] = showCard 
            
        avg = np.mean(cards)*2/3
        index = np.argmin(abs(cards-avg))
        income[index] = 100
        playerRecord1[i] = [generated_type,cards,income]
        print('income:',income)
        print('card:',cards)
    
    return playerRecord1

def main():
    
    parser = argparse.ArgumentParser(description="simple Level-K sample1")
    
    parser.add_argument('-np','--numPlayer', default=10, type=int,help='多少人玩游戏，默认：10')
    
    parser.add_argument('-lo','--levelRatio', default=[1.0,0,0,0,0], nargs='+',type=float,help='level的人数比例,默认：[1.0,0,0,0]')
    
    parser.add_argument('-nr','--numRounds', default=1, type=int,help='每次游戏进行运行轮数,默认：1')
    
    args = parser.parse_args()                   
    numPlayer = args.numPlayer
    levelRatio= args.levelRatio 
    numRounds=args.numRounds
                    
    playerRecord1 =  runGameOnce_A(numPlayer,levelRatio,numRounds)
    print(playerRecord1)
   
if __name__=="__main__":
    main()