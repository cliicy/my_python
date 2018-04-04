def gen(n):
    i=0;
    while i<n:
        yield i
        i+=1

def getElementByIndex(index,gen):
    r=None
    for i in range(index):
        try:
            r=next(gen)
        except:
            return None
    return r


def _getElementsByIndices(indices,gen):
    rr=[None for i in indices]
    m=max(indices)
    for i in range(m+1):
        try:
            r=next(gen)
            if i in indices:
                i_index_in_indices=indices.index(i)
                rr[i_index_in_indices]=r
        except StopIteration:
            return  rr
    return rr


def getElementsbByIndices(indices, gen):  # 取生成器中的几个元素，序号存在indices中
    rr = [None for i in indices]  # 初始化一个结果数组，默认值全为None，结果存在对应的位置上
    m = max(indices)  # 最大位置
    for i in range(m + 1):
        try:
            r = next(gen)
            if i in indices:
                i_index_in_indices = indices.index(i)
                rr[i_index_in_indices] = r  # 将结果的对应位置变成生成器的内容，当位置出现重复时，此方法不适合
        except StopIteration:
            return rr
    return rr


g1=gen(10)
print(getElementByIndex(3,g1))
g2=gen(20)
print(_getElementsByIndices([1,2,5,12,7],g2))
#print(getElementsbByIndices([1,2,5,12,7],g2))




