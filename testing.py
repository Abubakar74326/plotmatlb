def translation(x,y,Tx,Ty):
    xnew = x + Tx
    ynew = y + Ty
    return xnew, ynew



def trans():
    x=input("enter the x number")
    y=input("enter the y number")
    Tx=input("enter the tx number")
    Ty=input("enter the ty number")
    xnew_value, ynew_value = translation(x, y, Tx, Ty)
    return {'x':xnew_value,'y':ynew_value}