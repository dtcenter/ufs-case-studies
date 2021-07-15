#!/bin/bash
# Command line arguments
if [ -z "$1" ]; then
   echo "Usage: $0 yyyymmddhh "
   echo "For example: 2018100900, 2019052300, 2019071200, 2019092512, 2019102812, 2020011812, 2020020312, 2020040912, 2020072300" 
   exit
fi
## date (year month day) and time (hour)
yyyymmddhh=$1 #i.e. "2018100900"

if [ "$#" -ge 2 ]; then
  nfcst=$2 #i.e. "12"
else
  nfcst=90
fi

## forecast interval, the default interval are 3 hours
if [ $yyyymmddhh -le 2019052300 ]; then
   nfcst_int=6
else 
   nfcst_int=3
fi

# Get the data (do not need to edit anything after this point!)
mkdir -p $yyyymmddhh
echo "Download files for cycle $yyyymmddhh ..."
cd $yyyymmddhh


#getting online forecast data
ifcst=$nfcst_int
while [ $ifcst -le $nfcst ] 
do
echo $ifcst
  if [ $ifcst -le 99 ]; then 
     if [ $ifcst -le 9 ]; then
        ifcst_str="00"$ifcst
     else
        ifcst_str="0"$ifcst
     fi
  else
        ifcst_str="$ifcst"
 fi
 echo $ifcst_str
#
echo "Downloading file ${yyyymmddhh}_bc.atmf${ifcst_str}.nemsio.tar.gz"
wget -c https://ufs-case-studies.s3.amazonaws.com/${yyyymmddhh}_bc.atmf${ifcst_str}.nemsio.tar.gz
#
ifcst=$[$ifcst+$nfcst_int]
done
