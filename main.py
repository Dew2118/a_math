def generate_segments(coord, orientation, n):
    segments = []
    if orientation == "horizontal":
        x = coord[0]
        y = coord[1]
        for i in range(y-n,y+2):
            segments_tuple = []
            if y == i or i < 1 or i + n - 1 > 15:
                continue
            for b in range(n):
                if i + b == y:
                    i += 1
                segments_tuple.append((x,i+b))
            segments.append(segments_tuple)
    else:
        x = coord[0]
        y = coord[1]
        for i in range(x-n,x+2):
            segments_tuple = []
            if x == i or i < 1 or i + n - 1 > 15:
                continue
            for b in range(n):
                if i + b == x:
                    i += 1
                segments_tuple.append((i+b,y))
            segments.append(segments_tuple)
    return segments


def a_math(arr, n):
    if arr == []:
        if n == 1:
            return [[(7, 7)]]
        else:
            result = []
            for i in range(n):
                x_component = []
                for j in range(n):
                    x_component.append((7,7+i-j))
                result.append(x_component)
            for i in range(n):
                y_component = []
                for j in range(n):
                    y_component.append((7+i-j,7))
                result.append(y_component)
            return result
    else:
        for equation in arr:
            #take the first and last tuple and minus them, if x1!=x2 then a = "x", else a = "y"
            if equation[0][0] != equation[-1][0]:
                #horizontal
                y =  equation[0][1]
                x1 = equation[0][0]
                xf = equation[-1][0]
                result = []
                firsts = []
                lasts = []
                for i in range(n):
                    firsts.append((x1-i-1,y))
                    lasts.append((xf+i+1,y))
                result.append(firsts)
                result.append(lasts)
                for coord in equation:
                    result.extend(generate_segments(coord, "horizontal", n))
                return result
            else:
                #vertical
                x =  equation[0][0]
                y1 = equation[0][1]
                yf = equation[-1][1]
                result = []
                firsts = []
                lasts = []
                for i in range(n):
                    firsts.append((x,y1-i-1))
                    lasts.append((x,yf+i+1))
                result.append(firsts)
                result.append(lasts)
                for coord in equation:
                    result.extend(generate_segments(coord, "vertical", n))
                return result