# -*- coding: cp936 -*-
import xlrd
import sys
import cx_Oracle
def calchh(j):
   if j==0:
      return '00'
   elif j==1:
      return '01'
   elif j==2:
      return '02'
   elif j==3:
      return '03'
   elif j==4:
      return '04'
   elif j==5:
      return '05'
   elif j==6:
      return '06'
   elif j==7:
      return '07'
   elif j==8:
      return '08'
   elif j==9:
      return '09'
   elif j==10:
      return '10'
   elif j==11:
      return '11'
   elif j==12:
      return '12'
   elif j==13:
      return '13'
   elif j==14:
      return '14'
   elif j==15:
      return '15'
   elif j==16:
      return '16'
   elif j==17:
      return '17'
   elif j==18:
      return '18'
   elif j==19:
      return '19'
   elif j==20:
      return '20'
   elif j==21:
      return '21'
   elif j==22:
      return '22'
   else :
      return '23'
def main():
   con = cx_Oracle.connect('test/test@sampledb') 
   cur = con.cursor()

   book=xlrd.open_workbook(r'E:\cj\load.xlsx')
   sheet0=book.sheet_by_index(0)
   nrows = sheet0.nrows    # 获取行总数
   ncols = sheet0.ncols    #获取列总数
   i=0
   while(i<nrows):
      YMD=sheet0.cell_value(i, 0)
      YMD1=str(YMD)
      Y=YMD1[0:4]
      M=YMD1[4:6]
      D=YMD1[6:8]
      j=1
      while(j<ncols):
         loadvalue=sheet0.cell_value(i, j)
         if j % 4 == 1:
             mm='00'
         elif j % 4 == 2:
             mm='15'
         elif j%4==3:
             mm='30'
         else :
             mm='45'
         jx=(j-1)/4
         hh=calchh(jx)
         YMDHMS=Y+'-'+M+'-'+D+' '+hh+':'+mm+':00'
         print YMDHMS
         cur.execute("INSERT INTO H33_179(DATETIME, loadvalue)VALUES(YMDHMS, loadvalue)" 
         con.commit() 
         j=j+1
      i=i+1

   cur.close() 
   con.close()
if __name__ == '__main__':
  main()
