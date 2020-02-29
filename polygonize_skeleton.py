# POLYGONIZE SKELETON
# Written by Giuseppe Mastrangelo
# (C) Apache License, Version 2.0

import c4d
import json
from c4d import gui

def select_all_objects():
    doc = c4d.documents.GetActiveDocument()
    FirstObject = doc.GetFirstObject()
    FirstObject.SetBit(c4d.BIT_ACTIVE)
    c4d.EventAdd()
    c4d.CallCommand(16388) # select all children
    
def convert_joints_to_polygon_objects():
    c4d.CallCommand(1022912)

def bind_polygon_with_joints():
    c4d.CallCommand(1019881)

def main():
    select_all_objects()
    convert_joints_to_polygon_objects()
    select_all_objects()
    bind_polygon_with_joints()
    
    print("Done")


if __name__=='__main__':
    main()
