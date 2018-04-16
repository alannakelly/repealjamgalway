import svgwrite

dwg = svgwrite.Drawing('cards.svg', size=('210mm','297mm'),profile='full',debug=True)
        

dwg.viewbox(0,0,210,297)
dwg.add(dwg.rect((0,0), (210,297),fill='white'))
dwg.add(dwg.rect((5,5), (55,80),fill='white', stroke='black',stroke_width=1,rx=2.5,ry=2.5))
dwg.save()

