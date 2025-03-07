import bpy
import random

# Limpiar la escena
bpy.ops.wm.read_factory_settings(use_empty=True)

# Crear la habitación 6x6x3
def create_room():
    bpy.ops.mesh.primitive_plane_add(size=6, location=(0, 0, 0))
    floor = bpy.context.active_object
    floor.name = "Floor"

    # Paredes
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

# Agua cerca de la marca
def create_near_water():
    bpy.ops.mesh.primitive_circle_add(radius=0.1, location=(0.2, -2.8, 0.01))
    near_water = bpy.context.active_object
    near_water.name = "WaterNearBody"

# Crear silla tirada
def create_chair():
    bpy.ops.mesh.primitive_cube_add(location=(-1, 0.5, 0.25), size=1)
    chair = bpy.context.active_object
    chair.name = "Chair"
    chair.scale = (0.4, 0.4, 0.4)
    chair.rotation_euler = (1.5708, 0, 0.7854)

# Crear librero y libros esparcidos
def create_bookshelf_and_books():
    bpy.ops.mesh.primitive_cube_add(location=(2, 2, 0.5), size=1)
    bookshelf = bpy.context.active_object
    bookshelf.name = "Bookshelf"
    bookshelf.scale = (0.3, 0.6, 1)

    for i in range(3):
        create_paper((2 + i * 0.15, 2, 0.1))
        create_paper((2 - i * 0.15, 2.2, 0.1))

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
    create_rope()
    create_body_outline()
    create_near_water()
    create_chair()
    create_bookshelf_and_books()
    create_light()

# Ejecutar creación
create_scene()

print("✅ Escena de crimen generada correctamente.")
