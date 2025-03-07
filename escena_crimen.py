import bpy
import random

# Limpiar la escena
bpy.ops.wm.read_factory_settings(use_empty=True)

# Crear la habitación 6x6x3
def create_room():
    bpy.ops.mesh.primitive_plane_add(size=6, location=(0, 0, 0))
    floor = bpy.context.active_object
    floor.name = "Floor"

    # Material de piso de madera
    mat_wood = bpy.data.materials.new(name="WoodFloor")
    mat_wood.use_nodes = True
    bsdf = mat_wood.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.8, 0.6, 0.4, 1)
    floor.data.materials.append(mat_wood)

    # Paredes
    wall_material = bpy.data.materials.new(name="WallMaterial")
    wall_material.use_nodes = True
    bsdf_wall = wall_material.node_tree.nodes["Principled BSDF"]
    bsdf_wall.inputs['Base Color'].default_value = (1, 1, 1, 1)
    bsdf_wall.inputs['Roughness'].default_value = 0.9

    for i in range(4):
        bpy.ops.mesh.primitive_plane_add(size=6, location=(0, 0, 1.5))
        wall = bpy.context.active_object
        wall.name = f"Wall_{i+1}"
        wall.rotation_euler[0] = 1.5708
        wall.location[2] = 1.5
        if i < 2:
            wall.rotation_euler[2] = i * 3.1416
            wall.location[1] = 3 if i == 0 else -3
        else:
            wall.rotation_euler[2] = (i - 2) * 3.1416 + 1.5708
            wall.location[0] = 3 if i == 2 else -3

        wall.data.materials.append(wall_material)

# Crear mesa
def create_table():
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0.5), size=1)
    table = bpy.context.active_object
    table.name = "Table"
    table.scale = (1.5, 1, 0.1)

# Crear papeles
def create_paper(location):
    bpy.ops.mesh.primitive_plane_add(size=0.3, location=location)
    paper = bpy.context.active_object
    paper.name = f"Paper_{location}"

# Crear carpeta confidencial
def create_folder():
    bpy.ops.mesh.primitive_plane_add(size=0.6, location=(0, 0, 0.61))
    folder = bpy.context.active_object
    folder.name = "ConfidentialFolder"

    bpy.ops.object.text_add(location=(-0.15, 0, 0.62))
    text = bpy.context.active_object
    text.data.body = "13 letras"
    text.rotation_euler = (1.5708, 0, 0)
    text.scale = (0.1, 0.1, 0.1)

# Crear vaso volcado y charco de agua
def create_glass_and_puddle():
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.1, location=(-0.5, 0, 0.55))
    glass = bpy.context.active_object
    glass.name = "SpilledGlass"
    glass.rotation_euler[1] = 1.5708

    bpy.ops.mesh.primitive_circle_add(radius=0.2, location=(-0.5, 0, 0.01))
    puddle = bpy.context.active_object
    puddle.name = "WaterPuddle"

# Crear ventana
def create_window():
    bpy.ops.mesh.primitive_plane_add(size=1.5, location=(3, 0, 1.5))
    window = bpy.context.active_object
    window.name = "Window"
    window.rotation_euler[2] = 1.5708

# Crear espejo quebrado
def create_broken_mirror():
    bpy.ops.mesh.primitive_plane_add(size=1.5, location=(-3, 0, 1.5))
    mirror = bpy.context.active_object
    mirror.name = "BrokenMirror"
    mirror.rotation_euler[2] = 1.5708

    mat_mirror = bpy.data.materials.new(name="BrokenMirrorMaterial")
    mat_mirror.use_nodes = True
    bsdf = mat_mirror.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.8, 0.8, 0.8, 1)
    bsdf.inputs['Metallic'].default_value = 0.5
    bsdf.inputs['Roughness'].default_value = 0.7
    mirror.data.materials.append(mat_mirror)

# Crear soga colgando
def create_rope():
    bpy.ops.curve.primitive_bezier_circle_add(radius=0.02, location=(0, -2.8, 3))
    rope = bpy.context.active_object
    rope.name = "HangingRope"
    rope.scale[1] = 5

# Crear marca de cuerpo
def create_body_outline():
    bpy.ops.mesh.primitive_circle_add(radius=0.5, location=(0, -2.8, 0.01))
    outline = bpy.context.active_object
    outline.name = "BodyOutline"

# Crear celular roto
def create_broken_phone():
    bpy.ops.mesh.primitive_cube_add(size=0.3, location=(-2.5, 1, 0.05))
    phone = bpy.context.active_object
    phone.name = "BrokenPhone"
    phone.rotation_euler[2] = random.uniform(0, 3.1416)

# Crear marcas de manos en las paredes
def create_handprints():
    for i in range(3):
        bpy.ops.mesh.primitive_plane_add(size=0.4, location=(2.9, random.uniform(-2, 2), random.uniform(1, 2.5)))
        handprint = bpy.context.active_object
        handprint.name = f"Handprint_{i+1}"

# Crear manchas de sangre en el suelo
def create_blood_stains():
    for i in range(3):
        bpy.ops.mesh.primitive_circle_add(radius=0.2, location=(random.uniform(-0.5, 0.5), random.uniform(-2.5, -2.8), 0.01))
        blood = bpy.context.active_object
        blood.name = f"BloodStain_{i+1}"

# Crear luz tenue
def create_light():
    bpy.ops.object.light_add(type='POINT', location=(0, 0, 2.8))
    light = bpy.context.active_object
    light.name = "RoomLight"
    light.data.energy = 50

# Crear escena completa
def create_scene():
    create_room()
    create_table()
    create_paper((0, 0.5, 0.6))
    create_paper((0.2, 0.3, 0.6))
    create_paper((0.5, 0, 0.6))
    create_folder()
    create_glass_and_puddle()
    create_window()
    create_broken_mirror()
    create_rope()
    create_body_outline()
    create_broken_phone()
    create_handprints()
    create_blood_stains()
    create_light()

# Ejecutar creación
create_scene()

print("✅ Escena de crimen generada correctamente.")
