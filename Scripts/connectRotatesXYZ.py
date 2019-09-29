import maya.cmds as cmds
import maya.mel as mel
import sys
#Connect XYZ Translates Rotates script from Wolf rig

#Only for testing, normally separate connecting Rotates and Translates in separate scripts

sel = cmds.ls(sl=1)

cmds.connectAttr(sel[0]+'.rotateX', sel[1]+'.rotateX', f=1)
cmds.connectAttr(sel[0]+'.rotateY', sel[1]+'.rotateY', f=1)
cmds.connectAttr(sel[0]+'.rotateZ', sel[1]+'.rotateZ', f=1)