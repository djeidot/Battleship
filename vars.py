screen_width = 512
screen_height = 512
screen_middle_h = screen_width / 2
screen_middle_v = screen_height / 2

background_color = (240,240,240)
neutral_color = (180,180,180)
grid_color = (50, 50, 50)
water_color = (50,50,255)
boat_color = (100,100,100)
hit_color = (255,50,50)
border_color = (0, 210, 0)

board_size_h = 10
board_size_v = 10

def get_color(chr):
    return {
        "?": neutral_color,
        ".": water_color,
        "O": boat_color,
        "X": hit_color
    }.get(chr)

pointer_cursor_string = (   #sized 24x24, hotspot(6, 0)
    "     XX                 ",
    "    X..X                ",
    "    X..X                ",
    "    X..X                ",
    "    X..X                ",
    "    X..XXX              ",
    "    X..X..XXX           ",
    "    X..X..X..XXX        ",
    "    X..X..X..X..X       ",
    "XXX X..X..X..X...X      ",
    "X..XX........X...X      ",
    "X...X............X      ",
    " X...............X      ",
    "  X..............X      ",
    "  X..............X      ",
    "   X............ X      ",
    "   X............X       ",
    "    X...........X       ",
    "    X...........X       ",
    "     X.........X        ",
    "     X.........X        ",
    "     XXXXXXXXXXX        ",
    "                        ",
    "                        ",
)
