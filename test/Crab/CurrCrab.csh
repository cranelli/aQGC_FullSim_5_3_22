#!/bin/csh

#crabLocation="/scratch/crab/CRAB_2_8_8/crab.csh"

#source $crabLocation;

#source /scratch/crab/CRAB_2_8_8/crab.csh

#source /scratch/crab/CRAB_2_10_1/crab.csh

#Maryland
source /scratch/crab/current/crab.csh

#CERN
source /afs/cern.ch/cms/ccs/wm/scripts/Crab/crab.sh

voms-proxy-init -voms cms -valid 192:00;
