'''
Created on 2015/10/22

@author: Takanari Seito
'''

if __name__ == '__main__':
    #線形計画法のパッケージPuLPのサンプルコード
    #参考:http://qiita.com/mzmttks/items/82ea3a51e4dbea8fbc17

    #pulpのインポート
    import pulp

    #問題の定義
    #pulp.LpProblem(A,B)
    #A:'問題名'、B:pulp.LpMinimize/pulp.LpMaximize
    problem = pulp.LpProblem('sample', pulp.LpMinimize)

    #変数の定義
    #pulp.LpVariable(A,B,C,D)
    #A:'変数名',B:最小値,C:最大値,D:種類(Continuous/Integer/Binary)
    a = pulp.LpVariable('a', 0, 1)
    b = pulp.LpVariable('b', 0, 1)

    #目的関数の定義
    #F(a,b) = a + b
    problem += a + b

    #制約条件の定義
    #a >= 0, b >= 0.1, a + b == 0.5
    problem += a >= 0
    problem += b >= 0.1
    problem += a + b == 0.5

    #問題を解く
    status = problem.solve()

    #結果の表示
    print (problem)
    print ("Result:")
    print ("Status:", pulp.LpStatus[status])
    print ("a", a.value())
    print ("b", b.value())