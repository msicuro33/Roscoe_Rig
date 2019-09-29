import maya.cmds as cmds
import maya.mel as mel
import sys
'''
Stores the Translates and Rotates of a joint to snap controls into position

'''

def orientControls():
	current = cmds.ls(sl=True)

#Query the Rotate and Translate values of the first of two current selections and store in variables
	rotates = cmds.xform('current[0]',q=True, t = True, ws = True)
	translates = cmds.xform('current[0]',q=True, ro = True, ws = True)
#Move the second selection with the Translate and Rotate values of the first
	cmds.xform('current[1]', t = translates, ws = True)
	cmds.xform('current[1]', ro = rotates, ws = True)
