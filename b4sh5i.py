from pwn import *
import random

def get_pie_base(p):
    f = open("/proc/%d/maps" % (p.pid),"r")
    data=""
    for i in f:
        if i.find(p.cwd+"/"+re.findall("[^/][-|_|.|a-zA-Z0-9]+",p.argv[0])[-1]) != -1 :
            data=i.split("-")
            break
    f.close()
    result=int(data[0],16)
    return result

def gdb_pie_attach(p,b_off,cmd=""):
    if len(sys.argv)==2:
        pie_base=get_pie_base(p)
        gdb_cmd=""
        for off_set in b_off:
            gdb_cmd+="b *0x%x + 0x%x\n" %(pie_base,off_set)
        gdb_cmd+=cmd+"c\n"
        attach_p=gdb.attach(p,gdb_cmd)
        return attach_p
    else:
        return 0

def NF(t, size, l=[]):
    ret = ''
    size = random.randrange(1,size+1)
    
    if t == 'd':
        log.success("Call Dump Fuzzer.")
        for i in range(size):
            ret += chr(random.randrange(1,0x100))
        log.info("size : "+str(hex(size)))
    
    elif t == 'c':
        log.success("Call list Choice Fuzzer.")
        if l != []:
            for i in range(size):
                ret += chr(random.choice(l))
            log.info("size : "+str(hex(size)))
        else:
            log.error("SyntaxError: Can't find list value.")
            exit(1)
    
    elif t == '':
        log.error("SyntaxError: Can't find type value.")
        exit(1)
    else:
        log.error("SyntaxError: Can't read argument.")
        exit(1)
    return ret
 
