from datetime import datetime

margin = 30
paths = ["Maurizio-HairlineItalic.otf", "Maurizio-ThinItalic.otf", "Maurizio-UltraLightItalic.otf", "Maurizio-LightItalic.otf", "Maurizio-RegularItalic.otf", "Maurizio-MediumItalic.otf", "Maurizio-BoldItalic.otf", "Maurizio-ExtraBoldItalic.otf", "Maurizio-BlackItalic.otf"]
fontNames = []
pageNumber = 1
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
timestampFile = datetime.now().strftime('%Y-%m-%d_%H-%M')

for path in paths:
    fontNames.append(installFont(path))
    
print(fontNames)

font("Maurizio-HairlineItalic")
allGlyphs = listFontGlyphNames()

txt = FormattedString()
txt.fontSize(100)
txt.lineHeight(115)

#goes through all glyphs in the font
for glyph in allGlyphs:
    #goes throug all weights imported
    for font in fontNames:
        txt.font(font)
        txt.appendGlyph(glyph)
        


# make new page when text flows over
while txt:
    newPage("A4Landscape")
    textBox(txt, (margin, margin, width()-margin*2, height()-margin*2))
    txt = textOverflow(txt, (margin, margin, width()-margin*2, height()-margin*2))
    fontSize(12)
    text(str(pageNumber), (width()-margin, 20), align="right")
    pageNumber+=1
    text(timestamp, (margin, 20))
    
    
saveImage("instance_proof"+timestampFile+".pdf")
# uninstall font
uninstallFont(path)