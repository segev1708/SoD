from math import sqrt
def angleMath(movingX,movingY,targetX,targetY,movingSpeed):
        """
        "m" like in y=mx+b
        i wont explain the math because it is complicated but its calculating the angle it 
        needs to move and using pitagoras formula to change the speed it needs to do it 
        so it will be balanced 
        a lot of random characters are there, its because most of them are temporary
        if they are used a lot of times they will have a understandable name
        """
        mX = targetX - movingX
        mY = targetY - movingY
        try:
            m = mY / mX
        except:
            m = 0
        x = 1 
        x = x**2
        if m > 0:
            y = m**2
            z = y + x 
            fm = sqrt(z)
            i = 100 * movingSpeed
            b = i/fm
            newm = m * b * 0.01 * -1 
            newx = x * b * 0.01 * -1

        elif m < 0:
            y = m**2
            z = y + x 
            fm = sqrt(z)
            # print(fm,"on m < 0")
            i = 100 * movingSpeed
            b = i/fm
            newm = m * b * 0.01 * -1
            newx = x * b * 0.01 * -1
            # print(newm,"newm")
            # print(newx,"newx")
        return [newx,newm]

#def