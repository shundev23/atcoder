# my code v1
def calcArea(val: int) -> int:
    result = pow(val,2)
    return result

# input validation
while True:
    try:
        N =  int(input("正方形の辺の長さを入力してください。（1<N<100）: "))
        if( 1 < N  < 100):
            break
        else:
            print("入力値は1以上100以下で入力してください。")
    except ValueError:
        print("入力値は数値で入力してください。")
        
print("正方形の面積は：",calcArea(N))
