from colorama import init,Fore
init(autoreset=True)
tasks={}
while True:
    print(Fore.CYAN+"\n1记录时长 2查看汇总 0退出")
    op = input("选择：")
    if op == "1":
        name = input("任务名：")
        t = float(input("用时(秒)："))
        tasks[name] = tasks.get(name,0)+t
        print(Fore.GREEN+"记录成功")
        print(Fore.GREEN+"✅记录成功")
    elif op == "2":
        for k,v in tasks.items():
            print(f"{k}:{v:.1f}秒")
    elif op == "0":
        print("结束")
        break
    else:
        print(Fore.RED+"输入错啦")