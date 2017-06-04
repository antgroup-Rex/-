def Draw_Base_Plate(scene=bpy.context.scene):
    #Add cube for cutting sides of base plate

    bpy.ops.mesh.primitive_cube_add(radius=0.05, location=(0.175,0,0.09))
    cube1 = scene.objects.active
    # copy cube1 and link to scene (not required as example howto)
    '''
    cube2 = cube1.copy()
    cube2.location.x = -0.175
    scene.objects.link(cube2)
    '''

    #Adding base plate
    bpy.ops.mesh.primitive_cylinder_add(radius=0.15,depth=0.005, location=(0,0,0.09))
    cyl = scene.objects.active

    #Adding booleab difference modifiers
    for ob in [cube1, cube1]:
        mod = cyl.modifiers.new("FacePlateBool", type='BOOLEAN')
        mod.operation = 'DIFFERENCE'
        mod.object =  ob        
        bpy.ops.object.modifier_apply(modifier=mod.name)
        ob.location.x = -ob.location.x

    #Deselect cylinder and delete cube        
    cyl.select = False
    scene.objects.unlink(cube1)
    bpy.data.objects.remove(cube1)   