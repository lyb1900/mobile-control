

from chatterbot import ChatBot


from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
# Create a new chat bot named Charlie



my_bot = ChatBot("mybot", storage_adapter="chatterbot.storage.SQLStorageAdapter",database_uri='sqlite:///d:\\m30robot.db')


# trainer = ChatterBotCorpusTrainer(my_bot)

# trainer.train(
#     "chatterbot.corpus.chinese"
# )

trainerlist = ListTrainer(my_bot)

# 手机参数问题
trainerlist.train([
    "运存多大",
    "这台是1g运存＋8g内存的，屏幕大，成色好，也有2＋32 2＋16的，看我主页"
])
trainerlist.train([
    "内存多大",
    "这台是8g内存的，屏幕大，成色好，也有32 16的，看我主页"
])
trainerlist.train([
    "内存多大的",
    "这台是8g内存的，屏幕大，成色好，也有32 16的，看我主页"
])
trainerlist.train([
    "运行内存多少",
    "这台是8g内存的，屏幕大，成色好，也有32 16的，看我主页"
])
trainerlist.train([
    "屏幕多大",
    "5.5"
])
trainerlist.train([
    "什么配置",
    "这台是8g内存的，屏幕大，成色好，也有32 16的，看我主页"
])

trainerlist.train([
    "安卓多少版本",
    "安卓6.0"
])

# 手机网络制式

# 手机使用问题
trainerlist.train([
    "手机卡吗",
    "日常接打电话，微信视频刷头条没问题"
])
trainerlist.train([
    "能上微信吗",
    "可以的"
])
trainerlist.train([
    "有电信4g吗",
    "全网通",
    "王者卡不卡，可以打电话吗",
    "可以功能正常"
])
trainerlist.train([
    "电信4g可以用吗",
    "可以，全网通",
])
# 如何交易问题
trainerlist.train([
    "怎么出",
    "直接拍，今天寄",
])
trainerlist.train([
    "可以自提吗",
    "可以的，自提便宜5元，提前说下时间"
])
trainerlist.train([
    "当面交易可以吗",
    "可以的，自提便宜5元，提前说下时间"
])
trainerlist.train([
    "好的谢谢",
    "欢迎购买",
])
trainerlist.train([
    "什么手机",
    "海信的一个机子，上市公司质量有保障，不是小作坊的",
    "联调移动4吗",
    "是的，全网通",
    "2+16吗",
    "这台是1g运存＋8g内存的，屏幕大，成色好，也有2＋32 2＋16的，看我主页"
])
trainerlist.train([
    "这是什么手机",
    "海信的一个机子，上市公司质量有保障，不是小作坊的",
    "能玩微信吗",
    "可以",
])


trainerlist.train([
    "有几台",
    "数量不多，喜欢可以直接拍下"
])
trainerlist.train([
    "有多少台啊",
    "你要几台",
    "5台",
    "有的",
    "联通4g可以用吗",
    "可以",
    "多少钱一台",
    "聊天窗口顶部有显示价格，亏本出，价格已经很低了",
    "你这是3g网络还是4g",
    "全网通4g",
    "价格能不能便宜点",
    "送线膜壳，已经很便宜了",
    "哪儿发货",
    "南京",
    "便宜点",
    "已经很便宜了"
])

# 价格

trainerlist.train([
    "价格",
    "聊天窗口顶部有显示价格，亏本出，价格已经很低了。"
])

trainerlist.train([
    "多少钱",
    "聊天窗口顶部有显示价格，亏本出，价格已经很低了",
])
trainerlist.train([
    "最低多少",
    "聊天窗口顶部有显示价格，亏本出，价格已经很低了",
])
trainerlist.train([
    "什么价位",
    "聊天窗口顶部有显示价格，亏本出，价格已经很低了",
    "电信4g支持吗",
    "全网通4g",
    "手机是什么型号的呢",
    "海信的一个机子，上市公司质量有保障，不是小作坊的"
])

trainerlist.train([
    "运费20",
    "聊天窗口顶部有总价格亏本出，价格已经很低了",
    "今天发还是明天发",
    "晚上打包发货"
])
trainerlist.train([
    "这种手机有多少",
    "你要几台，有的",
    "能上支付宝淘宝微信",
    "可以",
    "付款了",
    "好的，晚上打包发货",
])
trainerlist.train([
    "可以用电信卡吗",
    "可以",
    "怎么装电话卡",
    "打开后盖",
])
trainerlist.train([
    "可以用电信卡吗",
    "可以",
    "什么牌子的手机",
    "海信的一个机子，上市公司质量有保障，不是小作坊的",
    "内存多大",
    "这台是8g内存的，屏幕大，成色好，也有32 16的，看我主页",
])
trainerlist.train([
    "你好",
    "你好",
    "手机还在吗",
    "在",
])
trainerlist.train([
    "手机还在吗",
    "在",
])
trainerlist.train([
    "在",
    "在",
    "在卖吗",
    "有的，可以拍",
    "可以正常使用qq微信支付宝吗",
    "可以"
    "威海发货吗",
    "发的"
])
trainerlist.train([
    "在不",
    "在",
])
trainerlist.train([
    "卡不卡",
    "日常接打电话看下新闻，用聊天软件可以的",
])
trainerlist.train([
    "在吗",
    "在，可以拍",
])
trainerlist.train([
    "还没发出去",
    "快递员已取件，快递员白天在外面跑，晚上才会更新",
])
trainerlist.train([
    "[笑脸]",
    "在的，可以直接下单",
    "当面交易",
    "欢迎上门自取验机，但因为上门自取有个时间成本，需要花我的时间，所以邮费不减免。为避免被放鸽子，需要您在平台上拍下并付款后才能上门自取验机，当面验机后没问题请当面确认收货，有问题可关闭交易，平台会将资金返还。"
])

trainerlist.train([
    "几成新",
    "9成新",
    "到深圳大概多久",
    "3-4天",
    "能便宜不",
    "已经很便宜了，机子好的",
    "全网通吗",
    "是的"
])
# ret = my_bot.get_response("在")
# print(ret)

# 价格 