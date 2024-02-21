def yolo_to_ssd(yolo_data, image_width, image_height):
    # YOLO format: [class, center_x, center_y, width, height]
    # SSD format: [class, xmin, ymin, xmax, ymax]

    ssd_data = []
    for yolo_item in yolo_data:
        class_id = yolo_item[0]
        center_x, center_y, width, height = yolo_item[1:]

        # Convert center coordinates to absolute coordinates
        xmin = int((center_x - width / 2) * image_width)
        xmax = int((center_x + width / 2) * image_width)
        ymin = int((center_y - height / 2) * image_height)
        ymax = int((center_y + height / 2) * image_height)

        ssd_item = [class_id, xmin, ymin, xmax, ymax]
        ssd_data.append(ssd_item)

    return ssd_data

# Example YOLO data (normalized)
yolo_data = [
    [0, 0.5, 0.5, 0.3, 0.4],  # [class, center_x, center_y, width, height]
    [1, 0.3, 0.7, 0.2, 0.3]
]

# Example image size
image_width = 640
image_height = 480

# Convert YOLO to SSD
ssd_data = yolo_to_ssd(yolo_data, image_width, image_height)

# Print SSD data
for item in ssd_data:
    print(item)
