import maya.cmds as cmds

#zeroNode script from Wolf rig
def zeroNode():
	sel = cmds.ls(sl=1)

	for cur in sel:
		trans = cmds.xform(cur,q=1, ws=1, t=1)
		rot = cmds.xform(cur,q=1, ws=1, ro=1)
		
		zeroNode = cmds.group(em=1, n=(cur+'_zeroNode'))

		cmds.xform(zeroNode, ws=1, t=(trans[0], trans[1], trans[2]))
		cmds.xform(zeroNode, ws=1, ro=(rot[0], rot[1], rot[2]))

		cmds.parent(cur,zeroNode)
