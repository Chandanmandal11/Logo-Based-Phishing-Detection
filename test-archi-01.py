from PIL import Image, ImageDraw, ImageFont

# Create a blank image with white background
width, height = 1500, 1000
background_color = (255, 255, 255)
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# Define fonts
font_path = "DejaVuSans-Bold.ttf"
title_font = ImageFont.truetype(font_path, 40)
subtitle_font = ImageFont.truetype(font_path, 30)
text_font = ImageFont.truetype(font_path, 24)

# Define colors
title_color = (0, 0, 0)
box_color = (135, 206, 235)
line_color = (0, 0, 0)
text_color = (0, 0, 0)

# Add title
title = "AI-Powered Issue Resolution Platform Architecture"
draw.text((width // 2 - draw.textsize(title, font=title_font)[0] // 2, 20), title, fill=title_color, font=title_font)

# Draw boxes for each component
components = {
    "User Interface (UI)\n- Post Issues\n- Browse/Search Issues": (50, 100, 450, 250),
    "Data Collection\n- Store Issues\n- Store User Profiles": (50, 300, 450, 450),
    "AI Engine\n- Keyword-Based Search\n- Commonality & Mutualism Matching\n- Proximity-Based Discovery": (550, 100, 950, 450),
    "Backend\n- Data Management\n- User Sessions": (1050, 100, 1450, 250),
    "Notification System\n- Alerts for Matches\n- Responses": (1050, 300, 1450, 450),
    "Privacy & Security\n- Data Protection\n- Secure Communication": (50, 500, 1450, 600)
}

# Draw the boxes and add labels
for label, (x1, y1, x2, y2) in components.items():
    draw.rectangle([x1, y1, x2, y2], outline=line_color, width=2)
    draw.text((x1 + 10, y1 + 10), label, fill=text_color, font=text_font)

# Draw arrows between components
arrows = [
    ((450, 175), (550, 175)),  # UI to AI Engine
    ((450, 375), (550, 375)),  # Data Collection to AI Engine
    ((950, 275), (1050, 175)),  # AI Engine to Backend
    ((950, 375), (1050, 375)),  # AI Engine to Notification System
    ((450, 525), (1450, 525)),  # Data Collection to Privacy & Security
    ((1050, 525), (1050, 450))  # Notification System to Privacy & Security
]

for (x1, y1), (x2, y2) in arrows:
    draw.line([x1, y1, x2, y2], fill=line_color, width=2)
    arrow_head = [(x2, y2 - 5), (x2, y2 + 5), (x2 + 10, y2)]
    draw.polygon(arrow_head, fill=line_color)

# Save the image
image_path = "updated_architecture_diagram.png"
image.save(image_path)
print(f"Diagram saved to {image_path}")
