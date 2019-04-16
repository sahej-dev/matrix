"""
Created on Thu Apr 4 13:15:39 2019
@author: Sahej A Singh
"""
import random

def createMatrix(order, a_ij):
        m_n = str(order)
        if " " in m_n:
            mnList = "".join(m_n.split('*')).split()
        else:
            mnList = m_n.split('*')
            
        m = int(mnList[0])
        n = int(mnList[1])
        
        a_ij = str(a_ij)
        
        matrice = []
        matriceRow = []
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                matriceRow.append(eval(a_ij))
            matrice.append(matriceRow)
            matriceRow = [] 
        return mat(matrice)


class mat:
    def __init__(self, matrix = []):
        self.matrix = matrix
        
        
    def printMat(self):
        for row in self.matrix:
            print(row)
        print()
            
    
    def multiplyMat(self, mat2):
        mat2 = mat2.toList()
        matProduct = []
        sum = 0
        
        if len(self.matrix[0]) == len(mat2):
            for i in range(0,len(self.matrix)):
                matProduct += [[]]
                for j in range(0,len(mat2[0])):
                    for k in range(0,len(mat2)):
                        sum += self.matrix[i][k]*mat2[k][j]
                    matProduct[i].append(sum)
                    sum = 0
                print(matProduct[i])
        else:
            print("Error!\nMatrice multiplication not possible.")
            
            
    def addMat(self,mat2):
        mat2 = mat2.toList()
        if(len(list(self.matrix)) == len(mat2) and len(list(self.matrix[0])) == len(mat2[0])):
            sumMat = []
            sumRow = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    sumRow.append(self.matrix[i][j] + mat2[i][j])
                sumMat.append(sumRow)
                sumRow = []
            return mat(sumMat)
        else:
            print("Order must be same to add the matrices.")
            
            
    def subMat(self,mat2):
        mat2 = mat2.toList()
        if(len(self.matrix) == len(mat2) and len(self.matrix[0]) == len(mat2[0])):
            subMat = []
            subRow = []
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    subRow.append(self.matrix[i][j] - mat2[i][j])
                subMat.append(subRow)
                subRow = []
            return mat(subMat)
        else:
            print("Order must be same to add the matrices.")
            
            
    def transpose(self):
        transposeMat = self.toList()
        for i in range(len(transposeMat)):
            for j in range(i,len(transposeMat[0])):
                transposeMat[i][j],transposeMat[j][i] = transposeMat[j][i],transposeMat[i][j]
        return mat(transposeMat)
    
    
    def toList(self):
        listMat = list()
        listRow = list()
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                listRow.append(self.matrix[row][column])
                
            listMat.append(listRow)
            listRow = []
        return listMat
    
    
    def equals(self, mat2):
        mat2 = mat2.toList()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != mat2[i][j]:
                    return False     
        return True
                
    
    def negateMat(self):
        matList = self.toList()
        for i in range(len(matList)):
            for j in range(len(matList[0])):
                matList[i][j] = -1*matList[i][j]
        return mat(matList)
    
    
    def multiplyScalar(self, scalar):
        matList = self.toList()        
        for i in range(len(matList)):
            for j in range(len(matList[0])):
                matList[i][j] = scalar*matList[i][j]
        return mat(matList)
    
    
    def isSym(self):
        if self.matrix == self.transpose().toList():
            return True
        return False
    
        
    def isSkewSym(self):
        if self.matrix == self.transpose().negateMat().toList():
            return True
        return False
    
    
    def componentSym(self):
        matList = self.toList()
        matt = mat(matList)
        return matt.addMat(matt.transpose()).multiplyScalar(0.5)
    
    
    def componentSkewSym(self):
        matList = self.toList()
        matt = mat(matList)
        return matt.subMat(matt.transpose()).multiplyScalar(0.5)
    
    
    def randMat(self,low,high,order = str()):
        matList = createMatrix(order,'0').toList()
        for i in range(len(matList)):
            for j in range(len(matList[i])):
                matList[i][j] = random.randrange(low,high)
        return mat(matList)
        
    
    def multiplyDiagonals(self):
        if len(self.matrix) == len(self.matrix[0]):
            product = 1
            for i in range(len(self.matrix)):
                product *= self.matrix[i][i]
            return product
        else:
            print("Matrix must be a square matrix.")
    
    
    def getSubMat(self,idxX,idxY):
        matt = self.toList()
        subRow = list()
        subMat = list()
        for i in range(len(matt)):
            for j in range(len(matt[0])):
                if i != idxX and j != idxY:
                    subRow.append(matt[i][j])
            if len(subRow) != 0:
                subMat.append(subRow)
                subRow = []
        return mat(subMat)
                    
    def getDet(self):
        matt = self.toList()
        if len(matt) == len(matt[0]):
            det = 0.0
            if len(matt) != 2:
                for idx in range(0,len(matt[0])):
                    det += ((-1)**(idx))*(matt[0][idx]* mat(matt).getSubMat(0,idx).getDet())
                return det
            else:
                return (matt[0][0]*matt[1][1] - matt[0][1]*matt[1][0])
        else:
            print("Matrix must be a square matrix")
        