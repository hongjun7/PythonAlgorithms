# �ѱ� -> �ʼ�, �߼�, ����
def destroy(c):
    head = "��������������������������������������"
    vowel = "�������¤äĤŤƤǤȤɤʤˤ̤ͤΤϤФѤҤ�"
    tail = "�Ǥ�����������������������������������������������������"
    o = ord(c) - 44032
    h = head[o // 588]
    o%= 588
    v = vowel[o // 28]
    t = tail[o % 28]
    if t == "��": t = ""
    return h, v, t

# �ʼ�, �߼�, ���� -> �ѱ�
def combine(h, v, t):
    head = "��������������������������������������"
    vowel = "�������¤äĤŤƤǤȤɤʤˤ̤ͤΤϤФѤҤ�"
    tail = "�Ǥ�����������������������������������������������������"
    
    h = head.find(h)
    v = vowel.find(v)
    last = t
    t = tail.find(last) if last else 0
    return chr(44032 + 588*h + 28*v + t)

# �ѱ� -> ���� ��ȯ (udlr)
def change_dir(c, d):
    h, v, t = destroy(c)
    if d == 'u': v = '��'
    elif d == 'd': v = '��'
    elif d == 'l': v = '��'
    else: v = '��'
    return combine(h, v, t)

tailgen = "..����������������"

def make_9(n, base=9):
    T = []
    while n:
        T.append(n%base)
        n//= base
    return T[::-1]

def make_n(n, base):
    # bonus cases
    if n == 32: return '��P����'
    
    s = ''
    T = make_9(n, base)
    mul = combine('��', '��', tailgen[base])
    
    if T[0] == 1: s+= mul
    else: s+= combine('��', '��', tailgen[T[0]]) + mul + '��'
    for i in range(1, len(T)):
        c = T[i]
        if c == 0: s+= ''
        elif c == 1: s+= '�޹�Ÿ��'
        else: s+= combine('��', '��', tailgen[c]) + '��'
        if i != len(T)-1: s+= mul + '��'
    return s + '��'

def make_n_opt(n):
    return min([make_n(n, base) for base in range(2, 10)], key=len)

def ordize(s):
    return [ord(c) for c in s]

def aheuize(s):
    return ''.join(make_n_opt(ord(c)) for c in s)

print(aheuize(input()) + '��')