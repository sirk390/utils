

def set_minlength(lst, minlen, makefiller=lambda: None):
    current_len = len(lst)
    if minlen > current_len:
        for _ in range(minlen - current_len):
            lst.append(makefiller())

def set_maxlength(lst, maxlen):
    current_len = len(lst)
    if maxlen < current_len:
        del lst[maxlen:]
        
def set_length(lst, length, makefiller=None):
    set_minlength(lst, length, makefiller=makefiller)
    set_maxlength(lst, length)
  
if __name__ == "__main__":
    a = []
    set_minlength(a, 5)
    print a
    b = [1, 9,2]
    set_length(b, 2)
    print b