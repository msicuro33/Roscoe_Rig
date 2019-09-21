#Parent joint to nurbs shape node 

#MEL script
{
string $sel[] = 'ls -sl';
string $shape[0] $sel[1];
parent -add -s $shapes $sel[1];
rename $shapes[0]($sel[1] + "Shape");
delete $sel[0];
}

#Python script
'''Get selected objects in a list'''
sel = cmds.ls(sl=1)
'''Get the shape node of the selected nurbs curve'''
shapes = cmds.listRelatives(sel[0], s = True)
'''Parent the joint to the shape node'''
cmds.parent(add = True, shape = True)
'''Rename the shape node'''
cmds.rename()
'''Delete the original transform that was instanced'''




