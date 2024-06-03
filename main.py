import random

from PIL import Image, ImageDraw, ImageFont


def create_gradient_background(width, height, start_color, end_color):
    """Создает изображение с градиентным фоном."""
    background = Image.new("RGB", (width, height), start_color)
    draw = ImageDraw.Draw(background)
    for i in range(height):
        gradient_color = (
            start_color[0] + i * (end_color[0] - start_color[0]) // height,
            start_color[1] + i * (end_color[1] - start_color[1]) // height,
            start_color[2] + i * (end_color[2] - start_color[2]) // height,
        )
        draw.line([(0, i), (width, i)], fill=gradient_color)
    return background


def draw_text_with_shadow(
    draw, text, position, font, text_color, shadow_color, shadow_offset
):
    """Рисует текст с тенью."""
    x, y = position
    draw.text(
        (x + shadow_offset, y + shadow_offset), text, font=font, fill=shadow_color
    )
    draw.text(position, text, font=font, fill=text_color)


def draw_symbol_with_shadow(
    draw, symbol, position, font, symbol_color, shadow_color, shadow_offset
):
    """Рисует символ с тенью."""
    x, y = position
    draw.text(
        (x + shadow_offset, y + shadow_offset), symbol, font=font, fill=shadow_color
    )
    draw.text(position, symbol, font=font, fill=symbol_color)


# def draw_icon_with_shadow(draw, shape, position, size, icon_color, shadow_color, shadow_offset):
#     """Рисует иконку (простую фигуру) с тенью."""
#     x, y = position
#     if shape == "circle":
#         draw.ellipse((x + shadow_offset, y + shadow_offset, x + size + shadow_offset, y + size + shadow_offset),
#                      fill=shadow_color)
#         draw.ellipse((x, y, x + size, y + size), fill=icon_color)
#     elif shape == "square":
#         draw.rectangle((x + shadow_offset, y + shadow_offset, x + size + shadow_offset, y + size + shadow_offset),
#                        fill=shadow_color)
#         draw.rectangle((x, y, x + size, y + size), fill=icon_color)


def is_outside_text_area(
    symbol_x, symbol_y, text_x, text_y, text_width, text_height, padding
):
    """Проверяет, находится ли символ за пределами текстовой области."""
    return not (
        text_x - padding < symbol_x < text_x + text_width + padding
        and text_y - padding < symbol_y < text_y + text_height + padding
    )


def main():
    # Параметры изображения
    width, height = 200, 200
    start_color = (10, 25, 47)
    end_color = (30, 50, 100)

    # Создание фона
    background = create_gradient_background(width, height, start_color, end_color)
    draw = ImageDraw.Draw(background)

    # Параметры текста
    font_path = "Montserrat-SemiBold.ttf"
    font_size = 45
    font = ImageFont.truetype(font_path, font_size)
    text = "TEANUS"
    text_color = (255, 255, 255)
    shadow_color = (0, 0, 0)
    shadow_offset = 5

    # Рисуем текст с тенью
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw_text_with_shadow(
        draw, text, (text_x, text_y), font, text_color, shadow_color, shadow_offset
    )

    # Параметры символов
    symbols = ["{}", "</>", "()", "[]", ";", "//"]
    symbol_font_size = 30
    symbol_font = ImageFont.truetype(font_path, symbol_font_size)
    symbol_color = (173, 216, 230)

    # Рисуем символы вокруг области текста
    padding = 20
    for _ in range(5):
        symbol = random.choice(symbols)
        symbol_bbox = draw.textbbox((0, 0), symbol, font=symbol_font)
        symbol_width = symbol_bbox[2] - symbol_bbox[0]
        symbol_height = symbol_bbox[3] - symbol_bbox[1]

        while True:
            symbol_x = random.randint(0, width - symbol_width)
            symbol_y = random.randint(0, height - symbol_height)
            if is_outside_text_area(
                symbol_x, symbol_y, text_x, text_y, text_width, text_height, padding
            ):
                break

        draw_symbol_with_shadow(
            draw,
            symbol,
            (symbol_x, symbol_y),
            symbol_font,
            symbol_color,
            shadow_color,
            shadow_offset,
        )

    # Параметры иконок
    icon_color = (173, 216, 230)
    icon_size = 40

    # # Рисуем иконки вокруг области текста
    # for _ in range(10):
    #     shape = random.choice(["circle", "square"])
    #     while True:
    #         icon_x = random.randint(0, width - icon_size)
    #         icon_y = random.randint(0, height - icon_size)
    #         if is_outside_text_area(icon_x, icon_y, text_x, text_y, text_width, text_height, padding):
    #             break
    #
    #     draw_icon_with_shadow(draw, shape, (icon_x, icon_y), icon_size, icon_color, shadow_color, shadow_offset)

    # Сохраняем изображение
    image_path = "teanus_post_boosty.png"
    background.save(image_path)
    background.show()


if __name__ == "__main__":
    main()
