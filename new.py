#!/usr/bin/env python3.4

import rocket
# TODO: extra package with transforms, matrices, etc

cargo = rocket.CargoHold()
#cargo.gl = rocket.load_shaders('vertex.glsl', 'fragment.glsl')

def main():
    canvas = rocket.make_canvas()
    rocket.launch(canvas)

@rocket.call
def draw():
    pass
    #cargo.gl['a_position'] = rocket.make_buffer(cargo.verts)
    #cargo.gl.draw('points', rocket.make_buffer(cargo.index, type='index'))
    # drawing tasks:
    # setting variables, including vertices, colors, indexs, and uniforms
    # and drawing, different methods and index buffers


@rocket.call
def update():
    print('hello!')


@rocket.call
def left_click(pos):
    #cargo.gl = rocket.load_shaders('other.glsl', 'fragment.glsl')
    pass


if __name__ == '__main__':
    main()
