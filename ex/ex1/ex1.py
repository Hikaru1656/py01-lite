import math;
import sys;

#円周率を取得
pi = math.pi

#まず、第一引数に値が入力されているか確認
if len(sys.argv) <= 1:
    #されていなければ、強制終了
    print('入力値がありません')
    sys.exit()
else:
    #されている場合、intかstrかを判断
    num = sys.argv[1];
    try:
        int(num)
    except:
        try:
            float(num)
        except:
            print('数値を入力してください')
        else:
            print(float(num)*float(num)*pi)
    else:
        print(int(num)*int(num)*pi)
