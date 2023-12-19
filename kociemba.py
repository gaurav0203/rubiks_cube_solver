from kociemba.kociemba import solve

def solve_wrap(input_str):
    return solve(input_str)

if __name__=="__main__":
    test = solve('BFURURRFUFDFURLRDRUDLBFBURFLUDLDLFUDLBBRLDLBBRUDFBFBLD')
    print(test)