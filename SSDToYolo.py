def ssd_to_yolo(ssd_data, image_width, image_height):
    # SSD format: [class, xmin, ymin, xmax, ymax]
    # YOLO format: [class, center_x, center_y, width, height]

    yolo_data = []
    for ssd_item in ssd_data:
        class_id = ssd_item[0]
        xmin, ymin, xmax, ymax = ssd_item[1:]

        # Convert absolute coordinates to center coordinates
        center_x = (xmin + xmax) / 2 / image_width
        center_y = (ymin + ymax) / 2 / image_height
        width = (xmax - xmin) / image_width
        height = (ymax - ymin) / image_height

        yolo_item = [class_id, center_x, center_y, width, height]
        yolo_data.append(yolo_item)

    return yolo_data

# Example SSD data (absolute)
ssd_data = [
    [0, 100, 200, 300, 400],  # [class, xmin, ymin, xmax, ymax]
    [1, 150, 250, 250, 350]
]

# Example image size
image_width = 640
image_height = 480

# Convert SSD to YOLO
yolo_data = ssd_to_yolo(ssd_data, image_width, image_height)

# Print YOLO data
for item in yolo_data:
    print(item)
