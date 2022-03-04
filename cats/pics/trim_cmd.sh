for x in *.png; do convert $x -fill none -fuzz 1% -draw 'matte 0,0 floodfill' -flop  -draw 'matte 0,0 floodfill' -flop -trim $x; done
