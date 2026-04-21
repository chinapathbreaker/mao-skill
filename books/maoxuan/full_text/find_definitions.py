# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

base = r"C:\Users\6dog\.qclaw\workspace\mao-skill\books\maoxuan\full_text"
files = ['vol1.txt','vol2.txt','vol3.txt','vol4.txt','vol5.txt','vol678.txt']

texts = {}
for f in files:
    path = os.path.join(base, f)
    try:
        texts[f] = open(path, 'r', encoding='utf-8', errors='ignore').read()
    except:
        texts[f] = open(path, 'r', encoding='gbk', errors='ignore').read()

# Search for explicit definition patterns
patterns = [
    r'所谓(.+?)，[是为](.+?)。',
    r'(.+?)就是(.+?)。',
    r'(.+?)是(.+?)，(.+?)。',
    r'矛盾.{0,5}就是.{0,20}对立统一',
    r'实践.{0,5}就是.{0,30}认识',
    r'实事求是.{0,5}就是.{0,30}',
    r'群众路线.{0,5}就是.{0,30}',
    r'主观主义.{0,5}包括.{0,20}',
    r'教条主义.{0,5}是.{0,20}',
    r'经验主义.{0,5}是.{0,20}',
    r'修正主义.{0,5}是.{0,20}',
    r'关门主义.{0,5}是.{0,20}',
    r'尾巴主义.{0,5}是.{0,20}',
    r'官僚主义.{0,5}是.{0,20}',
    r'机会主义.{0,5}是.{0,20}',
    r'左倾.{0,5}是.{0,20}',
    r'右倾.{0,5}是.{0,20}',
    r'新民主主义.{0,5}是.{0,30}',
    r'人民内部矛盾.{0,5}是.{0,30}',
    r'敌我矛盾.{0,5}是.{0,30}',
    r'整风.{0,5}是.{0,30}',
    r'统一战线.{0,5}是.{0,30}',
    r'游击战争.{0,5}是.{0,30}',
    r'持久战.{0,5}是.{0,30}',
    r'人民战争.{0,5}是.{0,30}',
    r'调查研究.{0,5}就是.{0,30}',
    r'没有调查.{0,10}没有发言权',
    r'枪杆子里面出政权',
    r'星星之火.{0,5}可以燎原',
]

# Key terms and their likely volumes
term_locs = {
    '矛盾': 'vol2.txt',  # On Contradiction
    '实践': 'vol2.txt',  # On Practice
    '实事求是': 'vol2.txt',
    '群众路线': 'vol2.txt',
    '主观主义': 'vol2.txt',
    '教条主义': 'vol2.txt',
    '经验主义': 'vol2.txt',
    '新民主主义': 'vol2.txt',  # On New Democracy
    '统一战线': 'vol3.txt',  # On Coalition Govt
    '整风': 'vol4.txt',  # Reform of Learning/Party
    '人民内部矛盾': 'vol4.txt',  # On Correct Handling
    '持久战': 'vol2.txt',  # On Protracted War
    '游击战': 'vol2.txt',
    '调查研究': 'vol1.txt',  # Report on Peasant Move
}

# Search for key terms and show context
search_terms = [
    '所谓矛盾', '矛盾着的对立面', '对立统一', '矛盾的普遍性', '矛盾的特殊性',
    '所谓实践', '从实践到认识', '从认识到实践',
    '实事求是', '没有调查没有发言权',
    '群众路线', '从群众中来',
    '主观主义', '教条主义', '经验主义',
    '修正主义', '关门主义', '尾巴主义', '官僚主义',
    '新民主主义', '新民主主义的革命', '无产阶级领导权',
    '统一战线', '又团结又斗争',
    '整风运动', '反对主观主义',
    '人民内部矛盾', '敌我矛盾',
    '枪杆子里面出政权', '武装夺取政权',
    '星星之火可以燎原',
    '持久战', '游击战',
    '上层建筑', '经济基础',
    '辩证法', '唯物论', '唯心论',
]

for term in search_terms:
    for f in files:
        text = texts[f]
        idx = 0
        while True:
            idx = text.find(term, idx)
            if idx == -1:
                break
            start = max(0, idx - 80)
            end = min(len(text), idx + 120)
            snippet = text[start:end].replace('\n', ' ')
            print(f"\n=== [{f}] found '{term}' ===")
            print(snippet)
            print("---")
            idx += len(term)
            break  # only first occurrence per file
