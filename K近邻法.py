##定义数据存储结构，即链表形式
class Node(object):
    def __init__(self,value=None,lchild=None,rchild=None):
        self.data=value;
        self.lchild=lchild;
        self.rchild=rchild;
    def __str__(self):
        return ("Node:value={},lchild={},rchild={}".format(self.data,self.lchild,self.rchild));

class Linklist(object):
    def __init__(self):
        self.root=Node();
        self.tailnode=None;
  
def disttwo(a,b):
    return (((np.array(a)-np.array(b))**2).sum()**0.5);
      
###将数据从Excel导入python中，并对数据进行预处理
import numpy as np;
import pandas as pd;

nearestPoint=None;
nearestValue=0;
df=pd.read_excel("D:\kdtree.xls");
df=pd.DataFrame(df);
a=df.values[:,:];
b=np.copy(a);
depth=0;
###构造平衡kd树
#定义生成左右子树的函数
def appendtree(node=None,a=0,depth=0):
    n=a.shape[0];#用来标记a的行数
    m=a.shape[1];#用来标记a的列数
    col=depth%m;#用来判断该节点的深度
    #用选择排序法对a特征向量进行升序排序
    if n>0:
        tttt=1;
        kx=1;
        for i in range(n-1):
            t=i;#用来标记a中该样本的行数
            for j in range(i+1,n):
                if (a[t][col]>a[j][col]):
                    t=j;
            if (t!=i):
                print("第{}次互换坐标位置".format(tttt));
                print("互换前的位置是：a[{}]={},a[{}]={}".format(i,a[i],t,a[t]));
                a[i][0],a[i][1],a[t][0],a[t][1]=a[t][0],a[t][1],a[i][0],a[i][1];
                print("互换后的位置是：a[{}]={},a[{}]={}".format(i,a[i],t,a[t]));
                tttt=tttt+1;
        print("第{}次递归完成".format(kx));
        mid=n//2;
        node.data=a[mid];
        if (mid>=1):
            node1=Node();#用来标记左子节点
            node2=Node();#用来标记右子节点
            node.lchild=node1;
            node.rchild=node2;
            al=a[:mid,:];#对a进行切分，a1为上半较小的部分
            print("al为：{}".format(al));
            ah=a[mid:,:];#对a进行切分，a2为下半较大的部分
            print("ah为：{}".format(ah));
            appendtree(node1,al,depth+1);
            appendtree(node2,ah,depth+1);
        else:
            node.lchild=None;
            node.rchild=None;
                
    else:
        node=None;
#构造平衡kd树
root=Linklist();#创建根节点
node=Node();#创建节点以存储各个节点数据
root.lchild=node;
depth=0;#当前原始树的深度为0
appendtree(node,b,depth);



x=[3,3];
###用kd树的最近邻搜索
#定义求两点之间距离的函数

#定义搜索最近邻搜索函数
def travel(node,x,depth=0):
    global nearestPoint;
    global nearestValue;
    if node!=None:
        n=len(x);#特征数
        axis=depth%n;#计算轴是第几列
        if (x[axis]<node.data[axis]):
            travel(node.lchild,x,depth+1);
        else:
            travel(node.rchild,x,depth+1);
        #以下是递归完毕后，向父节点方向回溯
        distNodeAndX=disttwo(x,node.data);
        if (nearestPoint==None):#确定当前点，更新最近的点和值
            nearestPoint=node;
            nearestValue=distNodeAndX;
        elif (nearestValue>distNodeAndX):
            nearestPoint=node;
            nearestValue=distNodeAndX;
        #确定是否需要去子节点的区域搜索
        if (abs(x[axis]-node.data[axis])<=nearestValue):
            if (x[axis]<node.data[axis]):
                travel(node.rchild,x,depth+1);
            else:
                travel(node.lchild,x,depth+1);
#进行kd数的最近邻搜索求解
node=root.lchild;
travel(node,x,depth);
print("x点{}的最近邻点是{}".format(x,nearestPoint.data));











