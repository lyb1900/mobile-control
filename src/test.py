import random

def main():
    index = random.randint(0,7)
    message = ["我也便宜出",
    "同出，楼主优先",
    "怎么没人看我的闲置手机呢",
    "我也有，便宜出售",
    "急出，我的更便宜些呢",
    "看我的，我的更便宜些呢",
    "这手机我也便宜出，楼主优先",
    "大家可以看我也便宜出，楼主优先"]
    print(index)
    print(message[index])

main()