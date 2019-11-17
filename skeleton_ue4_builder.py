# UE4 SKELETON BUILDER
# Written by Giuseppe Mastrangelo
# (C) Apache License, Version 2.0

import c4d
import json
from c4d import gui

skeleton_string = '[{"roty": 0.0, "rotx": -90.0, "rotz": 0.0, "posz": 0.0, "name": "root", "posx": 0.0, "posy": 0.0, "children": [{"roty": -89.7906, "rotx": 89.9981, "rotz": 89.9981, "posz": -96.7506, "name": "pelvis", "posx": 0.0, "posy": 1.0562, "children": [{"roty": -0.0, "rotx": -0.0, "rotz": 7.1539, "posz": 0.0, "name": "spine_01", "posx": 10.8089, "posy": -0.8514, "children": [{"roty": -0.0, "rotx": -0.0, "rotz": -14.0636, "posz": -0.0, "name": "spine_02", "posx": 18.8753, "posy": 3.8012, "children": [{"roty": 0.0, "rotx": 0.0, "rotz": -2.7794, "posz": 0.0, "name": "spine_03", "posx": 13.4073, "posy": 0.4205, "children": [{"roty": 61.8536, "rotx": 108.7192, "rotz": -101.5409, "posz": 3.782, "name": "clavicle_l", "posx": 11.8837, "posy": -2.7321, "children": [{"roty": 40.3005, "rotx": 7.6739, "rotz": 17.021, "posz": -0.0, "name": "upperarm_l", "posx": 15.7849, "posy": 0.0, "children": [{"roty": -10.3973, "rotx": -3.6133, "rotz": 30.3609, "posz": -0.0, "name": "lowerarm_l", "posx": 30.3399, "posy": 0.0, "children": [{"roty": 2.4998, "rotx": -76.3562, "rotz": 0.4126, "posz": 0.0, "name": "hand_l", "posx": 26.9751, "posy": 0.0, "children": [{"roty": -3.7638, "rotx": 14.867, "rotz": -25.5369, "posz": 2.1094, "name": "index_01_l", "posx": 12.0681, "posy": 1.7635, "children": [{"roty": -0.4753, "rotx": 1.3378, "rotz": -11.9861, "posz": -0.0, "name": "index_02_l", "posx": 4.2875, "posy": -0.0, "children": [{"roty": 0.9973, "rotx": 1.1374, "rotz": 9.4963, "posz": 0.0, "name": "index_03_l", "posx": 3.3938, "posy": 0.0, "children": []}]}]}, {"roty": -7.0406, "rotx": 1.9179, "rotz": -22.8259, "posz": -0.5712, "name": "middle_01_l", "posx": 12.2443, "posy": 1.2936, "children": [{"roty": 1.1368, "rotx": -2.025, "rotz": -12.2807, "posz": -0.0, "name": "middle_02_l", "posx": 4.6404, "posy": -0.0, "children": [{"roty": -4.39, "rotx": 0.7814, "rotz": 15.3998, "posz": -0.0, "name": "middle_03_l", "posx": 3.6488, "posy": -0.0, "children": []}]}]}, {"roty": -18.934, "rotx": -18.7246, "rotz": -20.1859, "posz": -4.6431, "name": "pinky_01_l", "posx": 10.1407, "posy": 2.2632, "children": [{"roty": -1.3157, "rotx": 1.0638, "rotz": -11.2081, "posz": -0.0, "name": "pinky_02_l", "posx": 3.571, "posy": 0.0, "children": [{"roty": 3.8697, "rotx": 0.4457, "rotz": -1.039, "posz": 0.0, "name": "pinky_03_l", "posx": 2.9856, "posy": -0.0, "children": []}]}]}, {"roty": -10.9893, "rotx": -13.5103, "rotz": -23.2921, "posz": -2.8469, "name": "ring_01_l", "posx": 11.4979, "posy": 1.7535, "children": [{"roty": -1.6697, "rotx": 0.3014, "rotz": -13.3155, "posz": 0.0, "name": "ring_02_l", "posx": 4.4302, "posy": 0.0, "children": [{"roty": 2.9877, "rotx": -0.3608, "rotz": 12.8997, "posz": -0.0, "name": "ring_03_l", "posx": 3.4767, "posy": -0.0, "children": []}]}]}, {"roty": 36.919, "rotx": 95.0691, "rotz": -27.0562, "posz": 2.5378, "name": "thumb_01_l", "posx": 4.762, "posy": 2.375, "children": [{"roty": 9.8332, "rotx": 1.6131, "rotz": -15.1513, "posz": -0.0, "name": "thumb_02_l", "posx": 3.8697, "posy": 0.0, "children": [{"roty": 0.4792, "rotx": 2.4148, "rotz": 12.3857, "posz": 0.0, "name": "thumb_03_l", "posx": 4.0622, "posy": 0.0, "children": []}]}]}]}, {"roty": 0.0, "rotx": 0.0, "rotz": 0.0, "posz": -0.0, "name": "lowerarm_twist_01_l", "posx": 14.0, "posy": 0.0, "children": []}]}, {"roty": 0.0, "rotx": -0.0, "rotz": -0.0, "posz": 0.0, "name": "upperarm_twist_01_l", "posx": 0.5, "posy": -0.0, "children": []}]}]}, {"roty": 61.8536, "rotx": 108.7192, "rotz": 78.459, "posz": -3.782, "name": "clavicle_r", "posx": 11.8838, "posy": -2.7321, "children": [{"roty": 40.3005, "rotx": 7.6739, "rotz": 17.021, "posz": 0.0, "name": "upperarm_r", "posx": -15.7848, "posy": -0.0, "children": [{"roty": -10.3973, "rotx": -3.6133, "rotz": 30.3609, "posz": -0.0, "name": "lowerarm_r", "posx": -30.34, "posy": -0.0, "children": [{"roty": 2.4998, "rotx": -76.3562, "rotz": 0.4126, "posz": 0.0, "name": "hand_r", "posx": -26.9752, "posy": 0.0, "children": [{"roty": -3.7638, "rotx": 14.867, "rotz": -25.5369, "posz": -2.1094, "name": "index_01_r", "posx": -12.0679, "posy": -1.7637, "children": [{"roty": -0.4753, "rotx": 1.3378, "rotz": -11.9861, "posz": 0.0001, "name": "index_02_r", "posx": -4.2877, "posy": 0.0001, "children": [{"roty": 0.9973, "rotx": 1.1374, "rotz": 9.4963, "posz": 0.0, "name": "index_03_r", "posx": -3.3938, "posy": 0.0001, "children": []}]}]}, {"roty": -7.0406, "rotx": 1.9179, "rotz": -22.8259, "posz": 0.5711, "name": "middle_01_r", "posx": -12.2441, "posy": -1.2937, "children": [{"roty": 1.1368, "rotx": -2.025, "rotz": -12.2807, "posz": -0.0, "name": "middle_02_r", "posx": -4.6406, "posy": -0.0001, "children": [{"roty": -4.39, "rotx": 0.7814, "rotz": 15.3998, "posz": 0.0, "name": "middle_03_r", "posx": -3.6489, "posy": 0.0, "children": []}]}]}, {"roty": -18.934, "rotx": -18.7246, "rotz": -20.1859, "posz": 4.6431, "name": "pinky_01_r", "posx": -10.1406, "posy": -2.2634, "children": [{"roty": -1.3157, "rotx": 1.0638, "rotz": -11.2081, "posz": 0.0, "name": "pinky_02_r", "posx": -3.5711, "posy": -0.0001, "children": [{"roty": 3.8697, "rotx": 0.4457, "rotz": -1.039, "posz": 0.0, "name": "pinky_03_r", "posx": -2.9854, "posy": 0.0003, "children": []}]}]}, {"roty": -10.9893, "rotx": -13.5103, "rotz": -23.2921, "posz": 2.8469, "name": "ring_01_r", "posx": -11.498, "posy": -1.7538, "children": [{"roty": -1.6697, "rotx": 0.3014, "rotz": -13.3155, "posz": 0.0, "name": "ring_02_r", "posx": -4.4299, "posy": 0.0001, "children": [{"roty": 2.9877, "rotx": -0.3608, "rotz": 12.8997, "posz": 0.0, "name": "ring_03_r", "posx": -3.4767, "posy": 0.0001, "children": []}]}]}, {"roty": 36.919, "rotx": 95.0691, "rotz": -27.0562, "posz": -2.5378, "name": "thumb_01_r", "posx": -4.7621, "posy": -2.3751, "children": [{"roty": 9.8332, "rotx": 1.6131, "rotz": -15.1513, "posz": -0.0001, "name": "thumb_02_r", "posx": -3.8696, "posy": 0.0001, "children": [{"roty": 0.4792, "rotx": 2.4148, "rotz": 12.3857, "posz": -0.0, "name": "thumb_03_r", "posx": -4.0622, "posy": 0.0, "children": []}]}]}]}, {"roty": 0.0, "rotx": -13.5104, "rotz": 0.0, "posz": 0.0, "name": "lowerarm_twist_01_r", "posx": -14.0, "posy": 0.0, "children": []}]}, {"roty": 0.0, "rotx": -19.9519, "rotz": 0.0, "posz": 0.0, "name": "upperarm_twist_01_r", "posx": -0.5, "posy": -0.0, "children": []}]}]}, {"roty": 0.0, "rotx": 0.0, "rotz": 23.508, "posz": 0.0, "name": "neck_01", "posx": 16.5588, "posy": -0.3553, "children": [{"roty": 0.0, "rotx": 0.0, "rotz": -15.3486, "posz": 0.0, "name": "head", "posx": 9.2836, "posy": 0.3642, "children": []}]}]}]}]}, {"roty": -7.0323, "rotx": 8.5635, "rotz": 1.5155, "posz": 9.0058, "name": "thigh_l", "posx": -1.4488, "posy": -0.5314, "children": [{"roty": 1.7873, "rotx": -5.736, "rotz": 7.6136, "posz": 0.0, "name": "calf_l", "posx": -42.572, "posy": 0.0, "children": [{"roty": -0.2191, "rotx": 0.3236, "rotz": 0.873, "posz": 0.0, "name": "calf_twist_01_l", "posx": -20.4768, "posy": -0.0, "children": []}, {"roty": 3.7049, "rotx": -0.4154, "rotz": -8.0596, "posz": -0.0, "name": "foot_l", "posx": -40.1967, "posy": -0.0, "children": [{"roty": 0.009, "rotx": 0.0039, "rotz": 91.8836, "posz": -0.0802, "name": "ball_l", "posx": -10.4538, "posy": -16.5779, "children": []}]}]}, {"roty": -0.0002, "rotx": -5.4387, "rotz": 0.0563, "posz": 0.0, "name": "thigh_twist_01_l", "posx": -22.0942, "posy": -0.0, "children": []}]}, {"roty": -7.0323, "rotx": 8.5635, "rotz": -178.4845, "posz": -9.0058, "name": "thigh_r", "posx": -1.4486, "posy": -0.5314, "children": [{"roty": 1.7873, "rotx": -5.736, "rotz": 7.6136, "posz": 0.0, "name": "calf_r", "posx": 42.5723, "posy": -0.0, "children": [{"roty": -0.2191, "rotx": 0.3234, "rotz": 0.873, "posz": 0.0, "name": "calf_twist_01_r", "posx": 20.4769, "posy": 0.0, "children": []}, {"roty": 3.7049, "rotx": -0.4154, "rotz": -8.0596, "posz": 0.0, "name": "foot_r", "posx": 40.1968, "posy": 0.0, "children": [{"roty": 0.009, "rotx": 0.0039, "rotz": 91.8836, "posz": 0.0802, "name": "ball_r", "posx": 10.4538, "posy": 16.5778, "children": []}]}]}, {"roty": -0.0002, "rotx": -5.4389, "rotz": 0.0563, "posz": 0.0, "name": "thigh_twist_01_r", "posx": 22.0942, "posy": -0.0, "children": []}]}]}, {"roty": 0.0, "rotx": -0.0, "rotz": -0.0, "posz": 0.0, "name": "ik_foot_root", "posx": 0.0, "posy": 0.0, "children": [{"roty": -88.8778, "rotx": 141.821, "rotz": 139.2072, "posz": -13.4657, "name": "ik_foot_l", "posx": 17.0763, "posy": 8.0721, "children": []}, {"roty": 88.8778, "rotx": -38.1789, "rotz": -139.2072, "posz": -13.4656, "name": "ik_foot_r", "posx": -17.0763, "posy": 8.0721, "children": []}]}, {"roty": 0.0, "rotx": -0.0, "rotz": -0.0, "posz": 0.0, "name": "ik_hand_root", "posx": 0.0, "posy": 0.0, "children": [{"roty": -35.1726, "rotx": 74.068, "rotz": -32.7511, "posz": -111.6797, "name": "ik_hand_gun", "posx": -56.6461, "posy": 0.3354, "children": [{"roty": -32.1687, "rotx": -145.8003, "rotz": 93.709, "posz": -43.8695, "name": "ik_hand_l", "posx": 77.8854, "posy": -69.6019, "children": []}, {"roty": 0.0, "rotx": 0.0, "rotz": 0.0, "posz": -0.0, "name": "ik_hand_r", "posx": -0.0, "posy": -0.0, "children": []}]}]}]}]'

def rebuild_skeleton(skeleton, parent):
    for bone in skeleton:
        name = bone["name"]
        posx = bone["posx"]
        posy = bone["posy"]
        posz = bone["posz"]
        rotx = c4d.utils.DegToRad(bone["rotx"])
        roty = c4d.utils.DegToRad(bone["roty"])
        rotz = c4d.utils.DegToRad(bone["rotz"])

        print("build " + name)
        
        joint = c4d.BaseObject(c4d.Ojoint)
        joint.SetRotationOrder(c4d.ROTATIONORDER_XYZGLOBAL)
        joint.SetName(name)
        joint.SetAbsPos(c4d.Vector(posx, posy, posz))
        joint.SetAbsRot(c4d.Vector(rotx, roty, rotz))
        if parent is None: 
            doc.InsertObject(joint)
        else:
            joint.InsertUnder(parent)
        
        if len(bone["children"]) > 0: 
            rebuild_skeleton(bone["children"], joint)

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
    skeleton = json.loads(skeleton_string)
    rebuild_skeleton(skeleton, None)
    select_all_objects()
    convert_joints_to_polygon_objects()
    select_all_objects()
    bind_polygon_with_joints()
    
    print("Done")


if __name__=='__main__':
    main()
