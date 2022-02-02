def cute_number(number,model=0):
        sets = {
                0:"0123456789", #Plain
                1:"₀₁₂₃₄₅₆₇₈₉",
                2:"𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡",
                3:"⁰¹²³⁴⁵⁶⁷⁸⁹",
                4:"0̷1̷2̷3̷4̷5̷6̷7̷8̷9̷",
                5:"0̴1̴2̴3̴4̴5̴6̴7̴8̴9̴",
                6:"⓪①②③④⑤⑥⑦⑧⑨",
                7:"０１２３４５６７８９"
                }
        if model == 4 or model == 5:
                st = sets[model]
                st = [st[i:i+2] for i in range(0, len(st), 2)]
                return(st[number])
        else:
                return(sets[model][number])

def cute_time(time_str="00:00",model=0):
        cute = ""
        for i in time_str:
                if i == time_str[2]:
                        do="Nothing"
                else:
                        cute = cute + cute_number(int(i),model)
        cute = cute[:2] + ":" + cute[2:]
        return cute

def showcase():
        import datetime
        for i in range(0,8):
                print(cute_time(datetime.datetime.now().strftime("%H:%M"),i))
 
