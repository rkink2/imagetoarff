
# coding: utf-8

# In[ ]:

#The directory where the images directories are
import os, pandas
WorkDir = "C:/temp/Datamining/images/"


# In[ ]:

#Obtain a list of the subdirectories on a directory
def listTextFiles(directory):
    fileList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                 fileList.append(os.path.join(root, file))
    return fileList


# In[ ]:

#Return the number of the bin at which a row belongs: 8 bins
def bin8(row):
    red = row[0]
    green = row[1]
    blue = row[2]
    if (0<=red<2**7) and (0<=green<2**7) and (0<=blue<2**7): return 1
    elif (0<=red<2**7) and (0<=green<2**7) and (2**7<=blue<2**8): return 2
    elif (0<=red<2**7) and (2**7<=green<2**8) and (0<=blue<2**7): return 3
    elif (0<=red<2**7) and (2**7<=green<2**8) and (2**7<=blue<2**8): return 4
    elif (2**7<=red<2**8) and (0<=green<2**7) and (0<=blue<2**7): return 5
    elif (2**7<=red<2**8) and (0<=green<2**7) and (2**7<=blue<2**8): return 6
    elif (2**7<=red<2**8) and (2**7<=green<2**8) and (0<=blue<2**7): return 7
    elif (2**7<=red<2**8) and (2**7<=green<2**8) and (27<=blue<2**8): return 8


# In[ ]:

#Return the number of the bin at which a row belongs: 64 bins
def bin64(row):
    red = row[0]
    green = row[1]
    blue = row[2]
    if (0<=red<2**6) and (0<=green<2**6) and (0<=blue<2**6): return 1
    elif (0<=red<2**6) and (0<=green<2**6) and (2**6<=blue<2*2**6): return 2
    elif (0<=red<2**6) and (0<=green<2**6) and (2*2**6<=blue<3*2**6): return 3
    elif (0<=red<2**6) and (0<=green<2**6) and (3*2**6<=blue<4*2**6): return 4
    elif (0<=red<2**6) and (2**6<= green<2*2**6) and (0<=blue<2**6): return 5
    elif (0<=red<2**6) and (2**6<= green<2*2**6) and (2**6<=blue<2*2**6): return 6
    elif (0<=red<2**6) and (2**6<= green<2*2**6) and (2*2**6<=blue<3*2**6): return 7
    elif (0<=red<2**6) and (2**6<= green<2*2**6) and (3*2**6<=blue<4*2**6): return 8
    elif (0<=red<2**6) and (2*2**6<= green<3*2**6) and (0<=blue<2**6): return 9
    elif (0<=red<2**6) and (2*2**6<= green<3*2**6) and (2**6<=blue<2*2**6): return 10
    elif (0<=red<2**6) and (2*2**6<= green<3*2**6) and (2*2**6<=blue<3*2**6): return 11
    elif (0<=red<2**6) and (2*2**6<= green<3*2**6) and (3*2**6<=blue<4*2**6): return 12
    elif (0<=red<2**6) and (3*2**6<= green<4*2**6) and (0<=blue<2**6): return 13
    elif (0<=red<2**6) and (3*2**6<= green<4*2**6) and (2**6<=blue<2*2**6): return 14
    elif (0<=red<2**6) and (3*2**6<= green<4*2**6) and (2*2**6<=blue<3*2**6): return 15
    elif (0<=red<2**6) and (3*2**6<= green<5*2**6) and (3*2**6<=blue<4*2**6): return 16
    elif (2**6<=red<2*2**6) and (0<=green<2**6) and (0<=blue<2**6): return 17
    elif (2**6<=red<2*2**6) and (0<=green<2**6) and (2**6<=blue<2*2**6): return 18
    elif (2**6<=red<2*2**6) and (0<=green<2**6) and (2*2**6<=blue<3*2**6): return 19
    elif (2**6<=red<2*2**6) and (0<=green<2**6) and (3*2**6<=blue<4*2**6): return 20
    elif (2**6<=red<2*2**6) and (2**6<= green<2*2**6) and (0<=blue<2**6): return 21
    elif (2**6<=red<2*2**6) and (2**6<= green<2*2**6) and (2**6<=blue<2*2**6): return 22
    elif (2**6<=red<2*2**6) and (2**6<= green<2*2**6) and (2*2**6<=blue<3*2**6): return 23
    elif (2**6<=red<2*2**6) and (2**6<= green<2*2**6) and (3*2**6<=blue<4*2**6): return 24
    elif (2**6<=red<2*2**6) and (2*2**6<= green<3*2**6) and (0<=blue<2**6): return 25
    elif (2**6<=red<2*2**6) and (2*2**6<= green<3*2**6) and (2**6<=blue<2*2**6): return 26
    elif (2**6<=red<2*2**6) and (2*2**6<= green<3*2**6) and (2*2**6<=blue<3*2**6): return 27
    elif (2**6<=red<2*2**6) and (2*2**6<= green<3*2**6) and (3*2**6<=blue<4*2**6): return 28
    elif (2**6<=red<2*2**6) and (3*2**6<= green<4*2**6) and (0<=blue<2**6): return 29
    elif (2**6<=red<2*2**6) and (3*2**6<= green<4*2**6) and (2**6<=blue<2*2**6): return 30
    elif (2**6<=red<2*2**6) and (3*2**6<= green<4*2**6) and (2*2**6<=blue<3*2**6): return 31
    elif (2**6<=red<2*2**6) and (3*2**6<= green<5*2**6) and (3*2**6<=blue<4*2**6): return 32
    elif (2*2**6<=red<3*2**6) and (0<=green<2**6) and (0<=blue<2**6): return 33
    elif (2*2**6<=red<3*2**6) and (0<=green<2**6) and (2**6<=blue<2*2**6): return 34
    elif (2*2**6<=red<3*2**6) and (0<=green<2**6) and (2*2**6<=blue<3*2**6): return 35
    elif (2*2**6<=red<3*2**6) and (0<=green<2**6) and (3*2**6<=blue<4*2**6): return 36
    elif (2*2**6<=red<3*2**6) and (2**6<= green<2*2**6) and (0<=blue<2**6): return 37
    elif (2*2**6<=red<3*2**6) and (2**6<= green<2*2**6) and (2**6<=blue<2*2**6): return 38
    elif (2*2**6<=red<3*2**6) and (2**6<= green<2*2**6) and (2*2**6<=blue<3*2**6): return 39
    elif (2*2**6<=red<3*2**6) and (2**6<= green<2*2**6) and (3*2**6<=blue<4*2**6): return 40
    elif (2*2**6<=red<3*2**6) and (2*2**6<= green<3*2**6) and (0<=blue<2**6): return 41
    elif (2*2**6<=red<3*2**6) and (2*2**6<= green<3*2**6) and (2**6<=blue<2*2**6): return 42
    elif (2*2**6<=red<3*2**6) and (2*2**6<= green<3*2**6) and (2*2**6<=blue<3*2**6): return 43
    elif (2*2**6<=red<3*2**6) and (2*2**6<= green<3*2**6) and (3*2**6<=blue<4*2**6): return 44
    elif (2*2**6<=red<3*2**6) and (3*2**6<= green<4*2**6) and (0<=blue<2**6): return 45
    elif (2*2**6<=red<3*2**6) and (3*2**6<= green<4*2**6) and (2**6<=blue<2*2**6): return 46
    elif (2*2**6<=red<3*2**6) and (3*2**6<= green<4*2**6) and (2*2**6<=blue<3*2**6): return 47
    elif (2*2**6<=red<3*2**6) and (3*2**6<= green<5*2**6) and (3*2**6<=blue<4*2**6): return 48
    elif (3*2**6<=red<4*2**6) and (0<=green<2**6) and (0<=blue<2**6): return 49
    elif (3*2**6<=red<4*2**6) and (0<=green<2**6) and (2**6<=blue<2*2**6): return 50
    elif (3*2**6<=red<4*2**6) and (0<=green<2**6) and (2*2**6<=blue<3*2**6): return 51
    elif (3*2**6<=red<4*2**6) and (0<=green<2**6) and (3*2**6<=blue<4*2**6): return 52
    elif (3*2**6<=red<4*2**6) and (2**6<= green<2*2**6) and (0<=blue<2**6): return 53
    elif (3*2**6<=red<4*2**6) and (2**6<= green<2*2**6) and (2**6<=blue<2*2**6): return 54
    elif (3*2**6<=red<4*2**6) and (2**6<= green<2*2**6) and (2*2**6<=blue<3*2**6): return 55
    elif (3*2**6<=red<4*2**6) and (2**6<= green<2*2**6) and (3*2**6<=blue<4*2**6): return 56
    elif (3*2**6<=red<4*2**6) and (2*2**6<= green<3*2**6) and (0<=blue<2**6): return 57
    elif (3*2**6<=red<4*2**6) and (2*2**6<= green<3*2**6) and (2**6<=blue<2*2**6): return 58
    elif (3*2**6<=red<4*2**6) and (2*2**6<= green<3*2**6) and (2*2**6<=blue<3*2**6): return 59 
    elif (3*2**6<=red<4*2**6) and (2*2**6<= green<3*2**6) and (3*2**6<=blue<4*2**6): return 60
    elif (3*2**6<=red<4*2**6) and (3*2**6<= green<4*2**6) and (0<=blue<2**6): return 61
    elif (3*2**6<=red<4*2**6) and (3*2**6<= green<4*2**6) and (2**6<=blue<2*2**6): return 62
    elif (3*2**6<=red<4*2**6) and (3*2**6<= green<4*2**6) and (2*2**6<=blue<3*2**6): return 63
    elif (3*2**6<=red<4*2**6) and (3*2**6<= green<5*2**6) and (3*2**6<=blue<4*2**6): return 64


# In[ ]:

#Return the number of the bin at which a row belongs: 512 bins
def bin512(row):
    red = row[0]
    green = row[1]
    blue = row[2]
    if ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 1 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 2 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 3 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 4 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 5 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 6 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 7 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 8 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 9 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 10 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 11 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 12 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 13 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 14 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 15 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 16 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 17 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 18 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 19 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 20 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 21 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 22 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 23 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 24 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 25 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 26 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 27 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 28 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 29 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 30 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 31 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 32 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 33 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 34 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 35 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 36 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 37 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 38 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 39 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 40 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 41 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 42 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 43 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 44 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 45 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 46 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 47 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 48 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 49 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 50 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 51 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 52 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 53 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 54 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 55 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 56 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 57 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 58 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 59 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 60 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 61 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 62 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 63 
    elif ( 0 * 2**5 <= red <  1 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 64 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 65 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 66 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 67 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 68 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 69 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 70 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 71 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 72 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 73 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 74 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 75 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 76 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 77 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 78 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 79 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 80 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 81 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 82 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 83 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 84 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 85 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 86 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 87 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 88 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 89 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 90 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 91 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 92 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 93 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 94 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 95 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 96 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 97 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 98 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 99 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 100 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 101 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 102 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 103 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 104 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 105 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 106 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 107 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 108 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 109 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 110 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 111 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 112 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 113 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 114 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 115 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 116 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 117 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 118 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 119 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 120 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 121 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 122 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 123 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 124 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 125 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 126 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 127 
    elif ( 1 * 2**5 <= red <  2 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 128 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 129 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 130 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 131 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 132 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 133 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 134 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 135 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 136 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 137 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 138 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 139 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 140 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 141 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 142 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 143 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 144 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 145 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 146 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 147 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 148 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 149 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 150 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 151 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 152 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 153 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 154 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 155 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 156 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 157 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 158 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 159 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 160 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 161 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 162 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 163 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 164 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 165 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 166 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 167 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 168 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 169 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 170 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 171 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 172 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 173 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 174 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 175 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 176 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 177 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 178 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 179 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 180 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 181 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 182 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 183 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 184 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 185 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 186 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 187 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 188 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 189 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 190 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 191 
    elif ( 2 * 2**5 <= red <  3 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 192 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 193 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 194 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 195 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 196 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 197 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 198 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 199 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 200 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 201 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 202 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 203 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 204 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 205 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 206 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 207 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 208 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 209 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 210 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 211 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 212 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 213 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 214 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 215 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 216 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 217 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 218 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 219 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 220 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 221 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 222 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 223 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 224 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 225 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 226 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 227 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 228 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 229 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 230 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 231 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 232 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 233 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 234 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 235 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 236 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 237 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 238 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 239 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 240 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 241 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 242 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 243 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 244 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 245 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 246 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 247 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 248 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 249 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 250 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 251 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 252 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 253 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 254 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 255 
    elif ( 3 * 2**5 <= red <  4 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 256 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 257 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 258 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 259 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 260 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 261 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 262 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 263 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 264 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 265 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 266 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 267 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 268 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 269 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 270 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 271 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 272 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 273 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 274 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 275 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 276 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 277 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 278 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 279 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 280 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 281 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 282 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 283 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 284 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 285 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 286 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 287 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 288 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 289 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 290 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 291 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 292 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 293 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 294 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 295 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 296 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 297 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 298 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 299 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 300 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 301 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 302 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 303 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 304 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 305 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 306 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 307 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 308 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 309 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 310 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 311 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 312 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 313 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 314 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 315 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 316 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 317 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 318 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 319 
    elif ( 4 * 2**5 <= red <  5 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 320 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 321 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 322 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 323 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 324 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 325 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 326 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 327 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 328 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 329 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 330 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 331 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 332 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 333 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 334 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 335 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 336 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 337 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 338 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 339 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 340 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 341 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 342 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 343 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 344 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 345 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 346 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 347 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 348 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 349 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 350 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 351 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 352 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 353 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 354 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 355 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 356 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 357 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 358 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 359 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 360 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 361 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 362 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 363 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 364 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 365 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 366 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 367 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 368 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 369 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 370 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 371 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 372 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 373 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 374 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 375 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 376 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 377 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 378 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 379 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 380 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 381 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 382 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 383 
    elif ( 5 * 2**5 <= red <  6 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 384 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 385 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 386 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 387 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 388 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 389 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 390 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 391 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 392 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 393 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 394 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 395 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 396 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 397 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 398 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 399 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 400 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 401 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 402 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 403 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 404 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 405 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 406 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 407 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 408 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 409 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 410 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 411 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 412 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 413 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 414 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 415 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 416 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 417 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 418 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 419 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 420 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 421 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 422 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 423 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 424 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 425 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 426 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 427 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 428 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 429 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 430 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 431 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 432 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 433 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 434 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 435 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 436 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 437 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 438 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 439 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 440 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 441 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 442 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 443 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 444 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 445 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 446 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 447 
    elif ( 6 * 2**5 <= red <  7 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 448 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 449 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 450 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 451 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 452 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 453 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 454 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 455 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 0 * 2**5 <= green <  1 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 456 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 457 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 458 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 459 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 460 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 461 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 462 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 463 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 1 * 2**5 <= green <  2 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 464 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 465 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 466 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 467 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 468 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 469 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 470 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 471 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 2 * 2**5 <= green <  3 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 472 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 473 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 474 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 475 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 476 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 477 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 478 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 479 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 3 * 2**5 <= green <  4 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 480 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 481 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 482 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 483 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 484 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 485 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 486 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 487 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 4 * 2**5 <= green <  5 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 488 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 489 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 490 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 491 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 492 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 493 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 494 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 495 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 5 * 2**5 <= green <  6 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 496 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 497 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 498 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 499 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 500 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 501 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 502 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 503 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 6 * 2**5 <= green <  7 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 504 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 0 * 2**5 <= blue <  1  * 2**5 ): return 505 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 1 * 2**5 <= blue <  2  * 2**5 ): return 506 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 2 * 2**5 <= blue <  3  * 2**5 ): return 507 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 3 * 2**5 <= blue <  4  * 2**5 ): return 508 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 4 * 2**5 <= blue <  5  * 2**5 ): return 509 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 5 * 2**5 <= blue <  6  * 2**5 ): return 510 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 6 * 2**5 <= blue <  7  * 2**5 ): return 511 
    elif ( 7 * 2**5 <= red <  8 * 2**5 ) and ( 7 * 2**5 <= green <  8 * 2**5 ) and ( 7 * 2**5 <= blue <  8  * 2**5 ): return 512 


# In[ ]:

categories = ["piano", "kangaroo", "strawberry", "sunflower", "airplane", "face", "leopard"]


# In[ ]:

#Process the files on each category
#Train Files 8 bins
B = 8
for category in categories:
    print category
    airplanes = listTextFiles(WorkDir + category + "/training/")
    airplanefile = open(WorkDir + category + "/trainFileB8.txt", 'w')
    for af in airplanes:
        airplane = pandas.read_csv(af, header=None)
        airplane['bin'] = airplane.apply(lambda x: bin8(x), axis=1)
        counts = airplane['bin'].value_counts(normalize=True).sort_index()
        countsd = dict(counts)
        frec = [countsd[i+1] if i+1 in countsd else 0 for i in range(B)]
        li = ["%f" % f for f in frec]
        line = str(li).strip('[]')
        airplanefile.write(line + ", " + category + '\n')
    airplanefile.close()


# In[ ]:

#Process the files on each category
#Train Files 64 bins
categories = ["piano", "kangaroo", "strawberry", "sunflower", "airplane", "face", "leopard"]
B = 64
for category in categories:
    print category
    airplanes = listTextFiles(WorkDir + category + "/training/")
    airplanefile = open(WorkDir + category + "/trainFileB64.txt", 'w')
    for af in airplanes:
        airplane = pandas.read_csv(af, header=None)
        airplane['bin'] = airplane.apply(lambda x: bin64(x), axis=1)
        counts = airplane['bin'].value_counts(normalize=True).sort_index()
        countsd = dict(counts)
        frec = [countsd[i+1] if i+1 in countsd else 0 for i in range(B)]
        li = ["%f" % f for f in frec]
        line = str(li).strip('[]')
        airplanefile.write(line + ", " + category + '\n')
    airplanefile.close()


# In[ ]:

#Process the files on each category
#Testing Files 8 bins
B = 8
for category in categories:
    print category
    airplanes = listTextFiles(WorkDir + category + "/test/")
    airplanefile = open(WorkDir + category + "/testFileB8.txt", 'w')
    for af in airplanes:
        airplane = pandas.read_csv(af, header=None)
        airplane['bin'] = airplane.apply(lambda x: bin8(x), axis=1)
        counts = airplane['bin'].value_counts(normalize=True).sort_index()
        countsd = dict(counts)
        frec = [countsd[i+1] if i+1 in countsd else 0 for i in range(B)]
        li = ["%f" % f for f in frec]
        line = str(li).strip('[]')
        airplanefile.write(line + ", " + category + '\n')
    airplanefile.close()


# In[ ]:

#Process the files on each category
#Testing Files 64 bins
B = 64
for category in categories:
    print category
    airplanes = listTextFiles(WorkDir + category + "/test/")
    airplanefile = open(WorkDir + category + "/testFileB64.txt", 'w')
    for af in airplanes:
        airplane = pandas.read_csv(af, header=None)
        airplane['bin'] = airplane.apply(lambda x: bin64(x), axis=1)
        counts = airplane['bin'].value_counts(normalize=True).sort_index()
        countsd = dict(counts)
        frec = [countsd[i+1] if i+1 in countsd else 0 for i in range(B)]
        li = ["%f" % f for f in frec]
        line = str(li).strip('[]')
        airplanefile.write(line + ", " + category + '\n')
    airplanefile.close()


# In[ ]:

#Process the files on each category
#Training File 512 Bin
B = 512
for category in categories:
    print category
    airplanes = listTextFiles(WorkDir + category + "/training/")
    airplanefile = open(WorkDir + category + "/trainFileB512.txt", 'w')
    for af in airplanes:
        airplane = pandas.read_csv(af, header=None)
        airplane['bin'] = airplane.apply(lambda x: bin512(x), axis=1)
        counts = airplane['bin'].value_counts(normalize=True).sort_index()
        countsd = dict(counts)
        frec = [countsd[i+1] if i+1 in countsd else 0 for i in range(B)]
        li = ["%f" % f for f in frec]
        line = str(li).strip('[]')
        airplanefile.write(line + ", " + category + '\n')
    airplanefile.close()


# In[ ]:

#Process the files on each category
#Testing Files Bin 512
B = 512
for category in categories:
    print category
    airplanes = listTextFiles(WorkDir + category + "/test/")
    airplanefile = open(WorkDir + category + "/testFileB512.txt", 'w')
    for af in airplanes:
        airplane = pandas.read_csv(af, header=None)
        airplane['bin'] = airplane.apply(lambda x: bin512(x), axis=1)
        counts = airplane['bin'].value_counts(normalize=True).sort_index()
        countsd = dict(counts)
        frec = [countsd[i+1] if i+1 in countsd else 0 for i in range(B)]
        li = ["%f" % f for f in frec]
        line = str(li).strip('[]')
        airplanefile.write(line + ", " + category + '\n')
    airplanefile.close()


# In[ ]:



