#!/bin/bash

wd=$PWD

git clone https://github.com/Chinwendu20/Hackbio-team-Mcclintock.git

cd Scripts

RScript iamjamesucheStage_0.R > iaju.txt

cat *.txt > TEAMMCCLINTOCK.csv

rm *.txt

mv TEAMMCCLINTOCK.csv $wd

