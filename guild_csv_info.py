# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫
import tkinter as tk  # 使用Tkinter前需要先导入
class TaptitianGuildRapid:

    def __init__(self, csv_from_game, part_attack, whole_dict=None, max_rapid_times=0, k=None, namelist=None,
                 ):
        self.csv_from_game = csv_from_game
        self.csv_from_game = self.csv_from_game.strip().split('\n')  # 把csv文件变成list
        #print(self.csv_from_game)

        self.part_attack = part_attack
        if whole_dict is None:
            whole_dict = {}
        self.whole_dict = whole_dict
        self.max_rapid_times = max_rapid_times
        if namelist is None:
            namelist = []
        self.namelist = namelist
        if k is None:
            k = []
        self.k = k

    def main(self):
        self.namelist=[]
        for i in self.csv_from_game:
            if i == self.csv_from_game[0]:
                continue
            self.k = i.split(',')  # 每个分开后开始导入字典
            weather_name_in_dict = self.k[0] in self.whole_dict

            if not weather_name_in_dict:
                self.namelist.append(self.k[0])
                self.add_name_to_dict(self.k)
            else:
                self.add_dmg_to_dict(self.k)
        print(self.effective_maximum_dmg())
        #print(self.whole_dict)
        #print(self.namelist)
        return ['\t'+str(i[0])+'   \t'+str(i[1])+'\t\t\t'+str(i[2])+"\n" for i in self.effective_maximum_dmg()]
        #return [str(i)+'\n' for i in self.effective_maximum_dmg()]

    def add_name_to_dict(self, k):  # 把名字放到字典里，并且创造字典 完成名称，编号，和突袭次数
        self.whole_dict[k[0]] = {'ID': self.k[1], 'Times': self.k[2], 'Total_dmg': 0, 'Wrong_dmg': 0,
                                 'effective_maximum_dmg': 0,'bone_dmg':0,
                                 'Lojak': {'k[6]': 0, 'k[7]': 0, 'k[8]': 0, 'k[9]': 0, 'k[10]': 0, 'k[11]': 0,
                                           'k[12]': 0, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                                           'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 0, 'k[23]': 0,
                                           'k[24]': 0, 'k[25]': 0, 'k[26]': 0, 'k[27]': 0, 'k[28]': 0, 'k[29]': 0},
                                 'Mohaca': {'k[6]': 0, 'k[7]': 0, 'k[8]': 0, 'k[9]': 0, 'k[10]': 0, 'k[11]': 0,
                                            'k[12]': 0, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                                            'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 0, 'k[23]': 0,
                                            'k[24]': 0, 'k[25]': 0, 'k[26]': 0, 'k[27]': 0, 'k[28]': 0, 'k[29]': 0},
                                 'Terro': {'k[6]': 0, 'k[7]': 0, 'k[8]': 0, 'k[9]': 0, 'k[10]': 0, 'k[11]': 0,
                                           'k[12]': 0, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                                           'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 0, 'k[23]': 0,
                                           'k[24]': 0, 'k[25]': 0, 'k[26]': 0, 'k[27]': 0, 'k[28]': 0, 'k[29]': 0},
                                 'Jukk': {'k[6]': 0, 'k[7]': 0, 'k[8]': 0, 'k[9]': 0, 'k[10]': 0, 'k[11]': 0,
                                          'k[12]': 0, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                                          'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 0, 'k[23]': 0,
                                          'k[24]': 0, 'k[25]': 0, 'k[26]': 0, 'k[27]': 0, 'k[28]': 0, 'k[29]': 0},
                                 'Sterl': {'k[6]': 0, 'k[7]': 0, 'k[8]': 0, 'k[9]': 0, 'k[10]': 0, 'k[11]': 0,
                                           'k[12]': 0, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                                           'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 0, 'k[23]': 0,
                                           'k[24]': 0, 'k[25]': 0, 'k[26]': 0, 'k[27]': 0, 'k[28]': 0, 'k[29]': 0},
                                 'Takedar': {'k[6]': 0, 'k[7]': 0, 'k[8]': 0, 'k[9]': 0, 'k[10]': 0, 'k[11]': 0,
                                             'k[12]': 0, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                                             'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 0, 'k[23]': 0,
                                             'k[24]': 0, 'k[25]': 0, 'k[26]': 0, 'k[27]': 0, 'k[28]': 0, 'k[29]': 0}}

        self.add_dmg_to_dict(k)

        return

    def add_dmg_to_dict(self, k):  # 全局变量已经有了添加过的名字和里面初始化了
        for i in range(6, 30):
            self.whole_dict[k[0]][k[4]]['k[' + str(i) + ']'] += int(k[i])  # 各部分伤害
            self.whole_dict[k[0]]['Wrong_dmg'] += self.part_attack[k[4]]['k[' + str(i) + ']'] * int(k[i])
            if i>=22:
                self.whole_dict[k[0]]['bone_dmg'] += self.part_attack[k[4]]['k[' + str(i) + ']'] * int(k[i])
        self.whole_dict[k[0]]['Total_dmg'] += int(k[5])  # 全伤害
        if int(k[2]) > int(self.max_rapid_times):
            self.max_rapid_times = k[2]
        return

    def effective_maximum_dmg(self):
        effectivelist = []
        top5_tt_effective = []
        botton5_tt_effective = []
        top_wrong_dmg=[]
        top5_tt_wrong_dmg=[]
        top_wrong_bone_dmg=[]
        top5_wrong_bone_dmg = []
        top_times=[]
        top5_times=[]
        bottom5_times=[]
        totallist=[]
        for i in self.whole_dict:
            self.whole_dict[i]['effective_maximum_dmg'] = self.whole_dict[i]['Total_dmg'] - self.whole_dict[i][
                'Wrong_dmg']
            effectivelist.append(self.whole_dict[i]['effective_maximum_dmg'])
            top_wrong_dmg.append(self.whole_dict[i]['Wrong_dmg'])
            top_wrong_bone_dmg.append(self.whole_dict[i]['bone_dmg'])
            top_times.append(self.whole_dict[i]['Times'])
        dict_effective_maximum_dmg = dict(zip(self.namelist, effectivelist))
        dict_Wrong_dmg = dict(zip(self.namelist, top_wrong_dmg))
        dict_Bone_dmg= dict(zip(self.namelist, top_wrong_bone_dmg))
        dict_top_times = dict(zip(self.namelist, top_times))
        j = 1
        for i in sorted(dict_effective_maximum_dmg.items(), key=lambda x: x[1], reverse=True):
            totallist.append(['有效伤害第：'+str(j),i[0],i[1]])
            j += 1
            if j > 6:  # 前5名
                break
        j = 1
        for i in sorted(dict_effective_maximum_dmg.items(), key=lambda x: x[1], reverse=True)[::-1]:
            totallist.append(['伤害倒数第：'+str(j),i[0],i[1]])
            j += 1
            if j > 6:  # 倒数5个
                break
        j = 1
        for i in sorted(dict_Wrong_dmg.items(), key=lambda x: x[1], reverse=True):
            totallist.append(['无效伤害第：'+str(j),i[0],i[1]])
            j += 1
            if j > 6:
                break
        j = 1
        for i in sorted(dict_Bone_dmg.items(), key=lambda x: x[1], reverse=True):
            totallist.append(['骨架伤害第：'+str(j),i[0],i[1]])
            j += 1
            if j > 6:
                break
        j=1
        for i in sorted(dict_top_times.items(), key=lambda x: x[1], reverse=True):
            totallist.append(['突袭次数第：'+str(j),i[0],i[1]])
            j += 1
            if j > 6:  # 前5名
                break
        j = 1
        for i in sorted(dict_top_times.items(), key=lambda x: x[1], reverse=True)[::-1]:
            totallist.append(['倒数突袭次数：'+str(j),i[0],i[1]])
            j += 1
            if j > 6:  # 倒数5个
                break
        return totallist  # 返回两个list字典

def printt():
    csv_from_Tkinter = csv_from.get('0.0', "end")
    #print(csv_from_Tkinter)
    part_attack = {'Lojak': {'k[6]': 0, 'k[7]': 0, 'k[8]': 0, 'k[9]': 0, 'k[10]': 0, 'k[11]': 1,
                             'k[12]': 0, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                             'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 1, 'k[23]': 1,
                             'k[24]': 1, 'k[25]': 1, 'k[26]': 1, 'k[27]': 1, 'k[28]': 1, 'k[29]': 1},
                   'Mohaca': {'k[6]': 0, 'k[7]': 1, 'k[8]': 0, 'k[9]': 0, 'k[10]': 0, 'k[11]': 0,
                              'k[12]': 0, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                              'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 1, 'k[23]': 1,
                              'k[24]': 1, 'k[25]': 1, 'k[26]': 1, 'k[27]': 1, 'k[28]': 1, 'k[29]': 1},
                   'Terro': {'k[6]': 0, 'k[7]': 0, 'k[8]': 1, 'k[9]': 1, 'k[10]': 1, 'k[11]': 1,
                             'k[12]': 1, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                             'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 1, 'k[23]': 1,
                             'k[24]': 1, 'k[25]': 1, 'k[26]': 1, 'k[27]': 1, 'k[28]': 1, 'k[29]': 1},
                   'Jukk': {'k[6]': 0, 'k[7]': 0, 'k[8]': 0, 'k[9]': 0, 'k[10]': 0, 'k[11]': 0,
                            'k[12]': 0, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                            'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 1, 'k[23]': 1,
                            'k[24]': 1, 'k[25]': 1, 'k[26]': 1, 'k[27]': 1, 'k[28]': 1, 'k[29]': 1},
                   'Sterl': {'k[6]': 0, 'k[7]': 0, 'k[8]': 1, 'k[9]': 1, 'k[10]': 1, 'k[11]': 1,
                             'k[12]': 0, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                             'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 1, 'k[23]': 1,
                             'k[24]': 1, 'k[25]': 1, 'k[26]': 1, 'k[27]': 1, 'k[28]': 1, 'k[29]': 1},
                   'Takedar': {'k[6]': 0, 'k[7]': 0, 'k[8]': 0, 'k[9]': 0, 'k[10]': 0, 'k[11]': 0,
                               'k[12]': 0, 'k[13]': 0, 'k[14]': 0, 'k[15]': 0, 'k[16]': 0, 'k[17]': 0,
                               'k[18]': 0, 'k[19]': 0, 'k[20]': 0, 'k[21]': 0, 'k[22]': 1, 'k[23]': 1,
                               'k[24]': 1, 'k[25]': 1, 'k[26]': 1, 'k[27]': 1, 'k[28]': 1, 'k[29]': 1}}  ##不打是1，打是0

    run = TaptitianGuildRapid(csv_from_Tkinter, part_attack)
    datesets=run.main()
    mainWin=tk.Tk() #创建新的主体窗口
    mainWin.title('本次工会突袭数据')#title 要在geometry上面
    mainWin.geometry('800x600')
    datashow = tk.Text(mainWin,width=300,
                   height=60)
    datashow.pack()
    datashow.insert(tk.END, datesets)



if __name__ == '__main__':
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()
    # 第2步，给窗口的可视化起名字
    window.title('Taptitian2 工会突袭数据分析表，下面窗口粘贴CSV文本-----书生Academy-制作')
    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('800x600')  # 这里的乘是小x
    b1 = tk.Button(window, text='输出值', width=10,
                   height=2, command=printt)
    b1.pack()
    csv_from = tk.Text(window,width=300,
                   height=60)
    csv_from.pack()
    csv_from.insert(tk.END, '把复制出来的本文粘贴到这里')
    # 第8步，主窗口循环显示
    window.mainloop()



