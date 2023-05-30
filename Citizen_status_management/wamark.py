from PIL import Image, ImageDraw, ImageFont


def add_watermark():
    font = ImageFont.load_default()
    filename = '/Users/mbungai/PycharmProjects/Citizen_status_management/Images_output/archie-ar.JPG'
    opened_image = Image.open(filename)
    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)
    font_size = int(image_width / 80)
    font = ImageFont.truetype("arial.ttf", font_size)
    x, y = int(image_width - 200), int(image_height - 10)
    draw.text((x, y), text='CameroonDepartment.gov', font=font, fill='#FFF', stroke_width=2, stroke_fill='#222',
              anchor='ms')
    opened_image.show()
    opened_image.save('/Users/mbungai/PycharmProjects/Citizen_status_management/Images_output/new.jpg')


# add_watermark()
