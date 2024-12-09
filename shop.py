#商店货物系统，结构为：{物品名称：[价格，等级]}
item = {
    #献祭类道具
    '时间献祭器':
    [
        200,
        3,
        '该道具已不再使用，输入/use 时间献祭器即可获得200刺儿，并且此道具直接消失'
    ],
    '时间提取器':
    [
        1500,
        5,
        '用你的时间换取更好的运气！！！可永久使用~'
    ],
    'kid献祭器':
    [
        300, 
        3,
        '该道具已不再使用，输入/use kid献祭器即可获得300刺儿，并且此道具直接消失'
    ],
    'kid充能器':
    [
        2000,
        5,
        '你在为低等级kid太多无处使用而烦恼吗？使用这个道具可以将你的低等级kid化作能量注入其中。\n当能量达到一定值后你可以消耗能量进行一次祈愿，祈愿获得高等级kid的概率将大幅提升\n输入/use kid充能器/用来充能的kid/数量 来进行充能\n输入/祈愿 来进行祈愿'
    ],
    #额外次数抓捕类道具
    '弹弓': 
    [
        50, 
        1,
        '半小时内忍不住想抓kid的心？没关系，弹弓能让你额外抓取一次！'
    ],
    '一次性小手枪': 
    [
        80, 
        2,
        '和弹弓一样满足你半小时内想抓kid的心，但是因为是枪械，能额外提高概率，应该吧......'
    ],
    '胡萝卜': 
    [
        200, 
        3,
        '胡萝卜，感觉像是能诱惑兔子的道具啊，难道kid里面也有兔子吗？'
    ],
    '烂胡萝卜': 
    [
        1, 
        1,
        '你是怎么觉得这种东西能成为一个道具的？'
    ],
    'kid提取器': 
    [
        300, 
        4,
        '/use kid提取器使用条例\n1. 输入“/use kid提取器/kid名称”来使用\n2. 只能提取当下的确存在的kid\n3. 提取失败会产生巨大爆炸，请做好防护措施\n4. 严禁递归'
    ],
    #BUFF道具
    '指南针': 
    [
        1200, 
        5,
        '给你指路的有力道具！！！'
    ],
    '神秘碎片': 
    [
        2000, 
        5,
        '不知道有什么作用的神秘碎片，看起来能拼成一把钥匙，隐隐泛着淡蓝色的光芒'
    ],
    '时间秒表': 
    [
        500, 
        4,
        '具有一定不稳定性的四次元道具。使用后理论上能清除任意原因导致的冷却时长......'
    ],
    '万能解药': 
    [
        500, 
        4,
        '解除身上除爆炸受伤外的不良状态（前提是你能使用这个道具）'
    ],
    '幸运药水': 
    [
        1, 
        5,
        '神奇的药水，在喝下之后好运程度可以比肩抓kid大神。接下来20次正常的抓kid时，每抓到一次kid都将额外获得15刺儿，并且在第三猎场抓kid时不会获得任何debuff。\n（由环境要素导致的意外危险除外）'
    ],
    '招财猫': 
    [
        180, 
        3,
        '好运伴随君。持有后每天签到可额外获得3刺儿，效果可叠加'
    ],
    #特殊道具
    '赌徒之眼':
    [
        20,
        1,
        '能够让你进du局前查看当前局势，但是...只能用一次'
    ]
}

#今日物品，前期道具较少，采用固定商品固定数量
today_item = {'指南针': 1000, '神秘碎片': 1000, '时间秒表': 50, '胡萝卜': 50, '招财猫': 100, '一次性小手枪': 100, '弹弓': 100, 'kid充能器': 1000, 'kid提取器': 50,'时间提取器':1000,'赌徒之眼':200}