# UE4 SKELETON BUILDER
# Written by Giuseppe Mastrangelo
# (C) Apache License, Version 2.0

import c4d
import json
from c4d import gui

skeleton_string = '[{"roty": 0.0, "rotx": -0.0, "rotz": -0.0, "posz": 0.0, "name": "root", "posx": 0.0, "posy": 0.0, "children": [{"roty": -89.1388, "rotx": 123.5323, "rotz": 146.8763, "posz": -91.1644, "name": "pelvis", "posx": -0.4259, "posy": 10.1787, "children": [{"roty": 0.018, "rotx": 0.6441, "rotz": 17.3537, "posz": 0.0, "name": "spine_01", "posx": 10.8089, "posy": -0.8514, "children": [{"roty": 2.505, "rotx": 1.2245, "rotz": -5.8406, "posz": 0.0, "name": "spine_02", "posx": 18.8754, "posy": 3.8012, "children": [{"roty": 1.9659, "rotx": 1.7226, "rotz": -3.2048, "posz": 0.0, "name": "spine_03", "posx": 13.4073, "posy": 0.4205, "children": [{"roty": 54.5509, "rotx": 88.8559, "rotz": -80.5184, "posz": 3.782, "name": "clavicle_l", "posx": 11.8837, "posy": -2.7321, "children": [{"roty": 63.296, "rotx": 4.332, "rotz": 34.1221, "posz": 0.0, "name": "upperarm_l", "posx": 15.7849, "posy": -0.0, "children": [{"roty": -0.0017, "rotx": 0.002, "rotz": 48.6737, "posz": -0.0, "name": "lowerarm_l", "posx": 30.3399, "posy": 0.0, "children": [{"roty": 10.5753, "rotx": -72.5156, "rotz": -3.6035, "posz": -0.0, "name": "hand_l", "posx": 26.9751, "posy": -0.0, "children": [{"roty": -7.5602, "rotx": 15.3205, "rotz": -44.0068, "posz": 2.1094, "name": "index_01_l", "posx": 12.0681, "posy": 1.7635, "children": [{"roty": 6.93, "rotx": 2.7318, "rotz": -20.5636, "posz": 0.0, "name": "index_02_l", "posx": 4.2875, "posy": -0.0, "children": [{"roty": 3.6417, "rotx": 5.4379, "rotz": -15.6468, "posz": -0.0, "name": "index_03_l", "posx": 3.3938, "posy": 0.0, "children": []}]}]}, {"roty": -9.533, "rotx": -13.6247, "rotz": -42.3001, "posz": -0.5712, "name": "middle_01_l", "posx": 12.2443, "posy": 1.2936, "children": [{"roty": 1.502, "rotx": 1.6262, "rotz": -55.3048, "posz": -0.0, "name": "middle_02_l", "posx": 4.6404, "posy": -0.0, "children": [{"roty": -11.8249, "rotx": 4.9626, "rotz": -26.0842, "posz": 0.0, "name": "middle_03_l", "posx": 3.6488, "posy": -0.0, "children": []}]}]}, {"roty": -19.6358, "rotx": -6.6973, "rotz": -31.5678, "posz": -4.6431, "name": "pinky_01_l", "posx": 10.1407, "posy": 2.2632, "children": [{"roty": -14.3695, "rotx": 26.9453, "rotz": -67.5275, "posz": 0.0, "name": "pinky_02_l", "posx": 3.571, "posy": 0.0, "children": [{"roty": 0.6103, "rotx": 15.4391, "rotz": -30.7386, "posz": -0.0, "name": "pinky_03_l", "posx": 2.9856, "posy": -0.0, "children": []}]}]}, {"roty": -20.0562, "rotx": 0.9266, "rotz": -45.7833, "posz": -2.8469, "name": "ring_01_l", "posx": 11.4979, "posy": 1.7535, "children": [{"roty": -1.1315, "rotx": 24.6919, "rotz": -60.4065, "posz": -0.0, "name": "ring_02_l", "posx": 4.4302, "posy": -0.0, "children": [{"roty": 9.1218, "rotx": 23.033, "rotz": -34.6419, "posz": -0.0, "name": "ring_03_l", "posx": 3.4767, "posy": -0.0, "children": []}]}]}, {"roty": 35.5783, "rotx": 91.5715, "rotz": -30.6833, "posz": 2.5378, "name": "thumb_01_l", "posx": 4.762, "posy": 2.375, "children": [{"roty": 7.0272, "rotx": -1.5936, "rotz": -31.2761, "posz": -0.0, "name": "thumb_02_l", "posx": 3.8697, "posy": 0.0, "children": [{"roty": -7.931, "rotx": -2.767, "rotz": -7.1125, "posz": 0.0, "name": "thumb_03_l", "posx": 4.0622, "posy": -0.0, "children": []}]}]}]}, {"roty": 0.0, "rotx": 8.4708, "rotz": 0.0, "posz": -0.2768, "name": "lowerarm_twist_01_l", "posx": 13.975, "posy": 0.1503, "children": []}]}, {"roty": 0.0, "rotx": -0.3781, "rotz": 0.0, "posz": 0.0716, "name": "upperarm_twist_01_l", "posx": 15.6418, "posy": -0.0483, "children": []}]}]}, {"roty": 57.0414, "rotx": 82.34, "rotz": 103.5885, "posz": -3.782, "name": "clavicle_r", "posx": 11.8838, "posy": -2.7321, "children": [{"roty": 67.3316, "rotx": 19.3789, "rotz": 51.5801, "posz": -0.0001, "name": "upperarm_r", "posx": -15.7847, "posy": -0.0001, "children": [{"roty": -0.0002, "rotx": 0.0001, "rotz": 38.4875, "posz": 0.0, "name": "lowerarm_r", "posx": -30.3401, "posy": 0.0, "children": [{"roty": 6.5522, "rotx": -72.4964, "rotz": 1.2569, "posz": 0.0, "name": "hand_r", "posx": -26.9752, "posy": -0.0, "children": [{"roty": -4.1477, "rotx": 15.0965, "rotz": -28.1621, "posz": -2.1094, "name": "index_01_r", "posx": -12.0679, "posy": -1.7637, "children": [{"roty": 5.6417, "rotx": 2.1268, "rotz": -16.4363, "posz": 0.0001, "name": "index_02_r", "posx": -4.2877, "posy": 0.0001, "children": [{"roty": 1.5033, "rotx": 1.6939, "rotz": 5.7872, "posz": 0.0, "name": "index_03_r", "posx": -3.3938, "posy": 0.0001, "children": []}]}]}, {"roty": -7.2654, "rotx": 2.0676, "rotz": -24.2064, "posz": 0.5711, "name": "middle_01_r", "posx": -12.2441, "posy": -1.2937, "children": [{"roty": 1.4578, "rotx": -0.4478, "rotz": -25.0652, "posz": -0.0, "name": "middle_02_r", "posx": -4.6406, "posy": -0.0001, "children": [{"roty": -6.13, "rotx": 2.4744, "rotz": 3.84, "posz": 0.0, "name": "middle_03_r", "posx": -3.6489, "posy": 0.0, "children": []}]}]}, {"roty": -21.7667, "rotx": -15.019, "rotz": -28.177, "posz": 4.6431, "name": "pinky_01_r", "posx": -10.1406, "posy": -2.2634, "children": [{"roty": -6.0736, "rotx": 18.1354, "rotz": -45.4389, "posz": 0.0, "name": "pinky_02_r", "posx": -3.5711, "posy": -0.0001, "children": [{"roty": 3.533, "rotx": 6.4836, "rotz": -12.7273, "posz": 0.0, "name": "pinky_03_r", "posx": -2.9854, "posy": 0.0003, "children": []}]}]}, {"roty": -14.9577, "rotx": -14.3996, "rotz": -37.3781, "posz": 2.8469, "name": "ring_01_r", "posx": -11.498, "posy": -1.7538, "children": [{"roty": 1.1497, "rotx": 12.4012, "rotz": -36.7597, "posz": 0.0, "name": "ring_02_r", "posx": -4.4299, "posy": 0.0001, "children": [{"roty": 5.543, "rotx": 3.423, "rotz": 4.4131, "posz": 0.0, "name": "ring_03_r", "posx": -3.4767, "posy": 0.0001, "children": []}]}]}, {"roty": 32.1593, "rotx": 86.027, "rotz": -28.1429, "posz": -2.5378, "name": "thumb_01_r", "posx": -4.7621, "posy": -2.3751, "children": [{"roty": 7.3074, "rotx": 3.2653, "rotz": -21.6671, "posz": -0.0001, "name": "thumb_02_r", "posx": -3.8696, "posy": 0.0001, "children": [{"roty": 4.3406, "rotx": 4.899, "rotz": 15.8647, "posz": -0.0, "name": "thumb_03_r", "posx": -4.0622, "posy": -0.0, "children": []}]}]}]}, {"roty": -0.0002, "rotx": -4.6274, "rotz": 0.0, "posz": 0.0, "name": "lowerarm_twist_01_r", "posx": -27.7492, "posy": 0.0, "children": []}]}, {"roty": -0.0001, "rotx": -38.353, "rotz": -0.0, "posz": -0.0, "name": "upperarm_twist_01_r", "posx": -0.4669, "posy": -0.0, "children": []}]}]}, {"roty": 1.3311, "rotx": 9.3999, "rotz": 16.7296, "posz": 0.0, "name": "neck_01", "posx": 16.5588, "posy": -0.3553, "children": [{"roty": -1.6889, "rotx": 7.7235, "rotz": -26.5415, "posz": -0.0, "name": "head", "posx": 9.2836, "posy": 0.3642, "children": []}]}]}]}]}, {"roty": -14.5821, "rotx": 23.7719, "rotz": -16.3303, "posz": 9.0058, "name": "thigh_l", "posx": -1.4488, "posy": -0.5314, "children": [{"roty": -1.5952, "rotx": -6.2218, "rotz": 21.3734, "posz": 0.0, "name": "calf_l", "posx": -42.572, "posy": -0.0, "children": [{"roty": -0.0396, "rotx": 3.1303, "rotz": 1.1909, "posz": 0.0783, "name": "calf_twist_01_l", "posx": -20.4768, "posy": 0.312, "children": []}, {"roty": 8.379, "rotx": 1.2533, "rotz": -1.826, "posz": 0.0, "name": "foot_l", "posx": -40.1967, "posy": -0.0, "children": [{"roty": 0.009, "rotx": 0.0039, "rotz": 91.8836, "posz": -0.0354, "name": "ball_l", "posx": -12.5861, "posy": -14.9083, "children": []}]}]}, {"roty": 0.0338, "rotx": -8.9488, "rotz": -0.5433, "posz": 0.0001, "name": "thigh_twist_01_l", "posx": -22.0942, "posy": 0.0217, "children": []}]}, {"roty": -9.7994, "rotx": 12.9955, "rotz": 175.0384, "posz": -9.0058, "name": "thigh_r", "posx": -1.4486, "posy": -0.5314, "children": [{"roty": -2.8415, "rotx": -8.1701, "rotz": 25.7336, "posz": 0.0, "name": "calf_r", "posx": 42.5723, "posy": -0.0, "children": [{"roty": 0.1959, "rotx": 6.1195, "rotz": 1.5425, "posz": -0.0783, "name": "calf_twist_01_r", "posx": 20.4769, "posy": -0.312, "children": []}, {"roty": 7.9369, "rotx": 7.5134, "rotz": -20.8695, "posz": 0.0, "name": "foot_r", "posx": 40.1968, "posy": 0.0, "children": [{"roty": 0.009, "rotx": 0.0039, "rotz": 91.8836, "posz": 0.0354, "name": "ball_r", "posx": 12.5861, "posy": 14.9083, "children": []}]}]}, {"roty": 0.0367, "rotx": 0.4404, "rotz": 1.059, "posz": -0.0001, "name": "thigh_twist_01_r", "posx": 22.0942, "posy": -0.0217, "children": []}]}]}, {"roty": 0.0, "rotx": -0.0, "rotz": -0.0, "posz": 0.0, "name": "ik_foot_root", "posx": 0.0, "posy": 0.0, "children": [{"roty": -88.8778, "rotx": 141.8208, "rotz": 139.2071, "posz": -13.4657, "name": "ik_foot_l", "posx": 17.0763, "posy": 8.0721, "children": []}, {"roty": 88.8778, "rotx": -38.1788, "rotz": -139.2071, "posz": -13.4656, "name": "ik_foot_r", "posx": -17.0763, "posy": 8.0721, "children": []}]}, {"roty": 0.0, "rotx": -0.0, "rotz": -0.0, "posz": 0.0, "name": "ik_hand_root", "posx": 0.0, "posy": 0.0, "children": [{"roty": -35.1726, "rotx": 74.068, "rotz": -32.7511, "posz": -111.6797, "name": "ik_hand_gun", "posx": -56.6461, "posy": 0.3354, "children": [{"roty": -32.1687, "rotx": -145.8003, "rotz": 93.709, "posz": -43.8695, "name": "ik_hand_l", "posx": 77.8854, "posy": -69.6019, "children": []}, {"roty": 0.0, "rotx": 0.0, "rotz": 0.0, "posz": 0.0, "name": "ik_hand_r", "posx": 0.0, "posy": 0.0, "children": []}]}]}]}]'

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
