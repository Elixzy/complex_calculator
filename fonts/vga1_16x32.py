WIDTH = 16
HEIGHT = 32
FIRST = 0x20
LAST = 0x7f
_FONT = \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x7f\xfe\x7f\xfe\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x7f\xfe\x7f\xfe\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x01\x80\x01\x80\x0f\xf0\x0f\xf0\x39\x9c\x39\x9c\x71\x8e\x71\x8e\x71\x80\x71\x80\x39\x80\x39\x80\x0f\xf0\x0f\xf0\x01\x9c\x01\x9c\x01\x8e\x01\x8e\x71\x8e\x71\x8e\x39\x9c\x39\x9c\x0f\xf0\x0f\xf0\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x1c\x1e\x1c\x1e\x38\x1e\x38\x00\x70\x00\x70\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x0e\x3c\x0e\x3c\x1c\x3c\x1c\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xc0\x07\xc0\x1c\x70\x1c\x70\x38\x38\x38\x38\x1c\x70\x1c\x70\x07\xc0\x07\xc0\x0f\xce\x0f\xce\x38\xfc\x38\xfc\x70\x78\x70\x78\x70\x78\x70\x78\x38\xfc\x38\xfc\x0f\xce\x0f\xce\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x03\x80\x03\x80\x01\xc0\x01\xc0\x00\xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x07\x00\x03\x80\x03\x80\x01\xc0\x01\xc0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x38\x0e\x38\x03\xe0\x03\xe0\x3f\xfe\x3f\xfe\x03\xe0\x03\xe0\x0e\x38\x0e\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x3f\xfe\x3f\xfe\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfe\x3f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00\x38\x00\x38\x00\x70\x00\x70\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x0e\x00\x0e\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xe0\x07\xe0\x1c\x38\x1c\x38\x38\x3c\x38\x3c\x38\x7c\x38\x7c\x38\xdc\x38\xdc\x39\x9c\x39\x9c\x3b\x1c\x3b\x1c\x3e\x1c\x3e\x1c\x3c\x1c\x3c\x1c\x1c\x38\x1c\x38\x07\xe0\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x01\xc0\x03\xc0\x03\xc0\x0f\xc0\x0f\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0\x0f\xf0\x38\x1c\x38\x1c\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x1c\x00\x1c\x00\x70\x00\x70\x01\xc0\x01\xc0\x07\x00\x07\x00\x1c\x00\x1c\x00\x38\x00\x38\x00\x3f\xfe\x3f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0\x0f\xf0\x38\x1c\x38\x1c\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x1c\x00\x1c\x01\xf0\x01\xf0\x00\x1c\x00\x1c\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x38\x1c\x38\x1c\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xf0\x01\xf0\x03\xf0\x03\xf0\x07\x70\x07\x70\x0e\x70\x0e\x70\x1c\x70\x1c\x70\x38\x70\x38\x70\x3f\xfc\x3f\xfc\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfe\x3f\xfe\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xf0\x3f\xf0\x00\x1c\x00\x1c\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x38\x1c\x38\x1c\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1c\x00\x1c\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xf0\x3f\xf0\x38\x1c\x38\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x1c\x1c\x1c\x1c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xf8\x3f\xf8\x00\x38\x00\x38\x00\x38\x00\x38\x00\x70\x00\x70\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1c\x1c\x1c\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x1c\x1c\x1c\x1c\x07\xf0\x07\xf0\x1c\x1c\x1c\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x1c\x1c\x1c\x1c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1c\x1c\x1c\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x1c\x0e\x1c\x0e\x07\xfe\x07\xfe\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x1c\x00\x1c\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x80\x03\x80\x03\x80\x03\x80\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x0e\x00\x0e\x00\x1c\x00\x1c\x00\x0e\x00\x0e\x00\x07\x00\x07\x00\x03\x80\x03\x80\x01\xc0\x01\xc0\x00\xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x07\x00\x03\x80\x03\x80\x01\xc0\x01\xc0\x00\xe0\x00\xe0\x00\x70\x00\x70\x00\x38\x00\x38\x00\x70\x00\x70\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xe0\x07\xe0\x1c\x38\x1c\x38\x38\x1c\x38\x1c\x00\x38\x00\x38\x00\x70\x00\x70\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0\x0f\xf0\x38\x1c\x38\x1c\x70\x0e\x70\x0e\x71\xfe\x71\xfe\x73\x8e\x73\x8e\x73\x8e\x73\x8e\x73\x8e\x73\x8e\x71\xfc\x71\xfc\x70\x00\x70\x00\x38\x00\x38\x00\x0f\xfc\x0f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x03\xc0\x07\xe0\x07\xe0\x0e\x70\x0e\x70\x1c\x38\x1c\x38\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x3f\xfc\x3f\xfc\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xf0\x3f\xf0\x38\x1c\x38\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x1c\x38\x1c\x3f\xf0\x3f\xf0\x38\x1c\x38\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x1c\x38\x1c\x3f\xf0\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1c\x1c\x1c\x1c\x38\x0e\x38\x0e\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x0e\x38\x0e\x1c\x1c\x1c\x1c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xf0\x3f\xf0\x38\x1c\x38\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x1c\x38\x1c\x3f\xf0\x3f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xe0\x3f\xe0\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfc\x3f\xfc\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xe0\x3f\xe0\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1c\x1c\x1c\x1c\x38\x0e\x38\x0e\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x3e\x38\x3e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x1c\x1c\x1c\x1c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x3f\xfe\x3f\xfe\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x00\x1c\x1c\x1c\x1c\x1c\x0e\x38\x0e\x38\x03\xe0\x03\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x38\x1c\x38\x1c\x70\x1c\x70\x1c\xe0\x1c\xe0\x1d\xc0\x1d\xc0\x1f\x80\x1f\x80\x1f\x80\x1f\x80\x1d\xc0\x1d\xc0\x1c\xe0\x1c\xe0\x1c\x70\x1c\x70\x1c\x38\x1c\x38\x1c\x1c\x1c\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xfc\x3f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x78\x1e\x78\x1e\x7c\x3e\x7c\x3e\x7e\x7e\x7e\x7e\x77\xee\x77\xee\x73\xce\x73\xce\x71\x8e\x71\x8e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x0e\x38\x0e\x3c\x0e\x3c\x0e\x3e\x0e\x3e\x0e\x3f\x0e\x3f\x0e\x3b\x8e\x3b\x8e\x39\xce\x39\xce\x38\xee\x38\xee\x38\x7e\x38\x7e\x38\x3e\x38\x3e\x38\x1e\x38\x1e\x38\x0e\x38\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1c\x1c\x1c\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x1c\x1c\x1c\x1c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xf0\x3f\xf0\x38\x1c\x38\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x1c\x38\x1c\x3f\xf0\x3f\xf0\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1c\x1c\x1c\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\xee\x38\xee\x1c\x7c\x1c\x7c\x07\xf8\x07\xf8\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xf0\x3f\xf0\x38\x1c\x38\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x1c\x38\x1c\x3f\xf0\x3f\xf0\x38\xe0\x38\xe0\x38\x70\x38\x70\x38\x38\x38\x38\x38\x1c\x38\x1c\x38\x0e\x38\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf0\x0f\xf0\x38\x1c\x38\x1c\x70\x0e\x70\x0e\x70\x00\x70\x00\x38\x00\x38\x00\x0f\xf0\x0f\xf0\x00\x1c\x00\x1c\x00\x0e\x00\x0e\x70\x0e\x70\x0e\x38\x1c\x38\x1c\x0f\xf0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfe\x3f\xfe\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x1c\x1c\x1c\x1c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x1c\x38\x1c\x38\x0e\x70\x0e\x70\x07\xe0\x07\xe0\x03\xc0\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x70\x0e\x71\x8e\x71\x8e\x73\xce\x73\xce\x77\xee\x77\xee\x3e\x7c\x3e\x7c\x1c\x38\x1c\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x1c\x38\x1c\x38\x0e\x70\x0e\x70\x07\xe0\x07\xe0\x03\xc0\x03\xc0\x07\xe0\x07\xe0\x0e\x70\x0e\x70\x1c\x38\x1c\x38\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x0e\x38\x0e\x1c\x1c\x1c\x1c\x0e\x38\x0e\x38\x07\x70\x07\x70\x03\xe0\x03\xe0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfe\x3f\xfe\x00\x1c\x00\x1c\x00\x38\x00\x38\x00\x70\x00\x70\x00\xe0\x00\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x0e\x00\x0e\x00\x1c\x00\x1c\x00\x3f\xfe\x3f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x1c\x00\x0e\x00\x0e\x00\x07\x00\x07\x00\x03\x80\x03\x80\x01\xc0\x01\xc0\x00\xe0\x00\xe0\x00\x70\x00\x70\x00\x38\x00\x38\x00\x1c\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\xc0\x03\xc0\x07\xe0\x07\xe0\x0e\x70\x0e\x70\x1c\x38\x1c\x38\x38\x1c\x38\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x07\x00\x07\x00\x03\x80\x03\x80\x01\xc0\x01\xc0\x00\xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf8\x0f\xf8\x00\x0e\x00\x0e\x0f\xfe\x0f\xfe\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x0f\xfe\x0f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3f\xf0\x3f\xf0\x38\x1c\x38\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x3f\xf8\x3f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf8\x0f\xf8\x38\x0e\x38\x0e\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x0e\x38\x0e\x0f\xf8\x0f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x07\xfe\x07\xfe\x1c\x0e\x1c\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x0f\xfe\x0f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf8\x0f\xf8\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x3f\xfe\x3f\xfe\x38\x00\x38\x00\x38\x00\x38\x00\x0f\xfc\x0f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x0f\xf0\x0f\xf0\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xf8\x0f\xf8\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x0f\xfe\x0f\xfe\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x1f\xf8\x1f\xf8\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x3b\xf8\x3b\xf8\x3c\x0e\x3c\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x00\x70\x00\x70\x00\x70\x00\x00\x00\x00\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\x70\x00\xe0\x00\xe0\x0f\x80\x0f\x80\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x38\x0e\x38\x0e\x70\x0e\x70\x0e\xe0\x0e\xe0\x0f\xc0\x0f\xc0\x0e\xe0\x0e\xe0\x0e\x70\x0e\x70\x0e\x38\x0e\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3e\x78\x3e\x78\x39\xce\x39\xce\x39\xce\x39\xce\x39\xce\x39\xce\x39\xce\x39\xce\x39\xce\x39\xce\x39\xce\x39\xce\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xe0\x3f\xe0\x38\x38\x38\x38\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xf0\x07\xf0\x1c\x1c\x1c\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x1c\x1c\x1c\x1c\x07\xf0\x07\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xf0\x3f\xf0\x38\x1c\x38\x1c\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x1c\x38\x1c\x3f\xf0\x3f\xf0\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xfe\x07\xfe\x1c\x0e\x1c\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x1c\x0e\x1c\x0e\x07\xfe\x07\xfe\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xf0\x3f\xf0\x38\x1c\x38\x1c\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xfc\x0f\xfc\x38\x00\x38\x00\x38\x00\x38\x00\x0f\xf8\x0f\xf8\x00\x0e\x00\x0e\x00\x0e\x00\x0e\x1f\xf8\x1f\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x1f\xfc\x1f\xfc\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x38\x1c\x0f\xfc\x0f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x70\x0e\x70\x0e\x38\x1c\x38\x1c\x1c\x38\x1c\x38\x0e\x70\x0e\x70\x07\xe0\x07\xe0\x03\xc0\x03\xc0\x01\x80\x01\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x38\x0e\x39\xce\x39\xce\x3b\xee\x3b\xee\x1f\x7c\x1f\x7c\x0e\x38\x0e\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x38\x1c\x38\x0e\x70\x0e\x70\x07\xe0\x07\xe0\x03\xc0\x03\xc0\x07\xe0\x07\xe0\x0e\x70\x0e\x70\x1c\x38\x1c\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x0e\x38\x0e\x1c\x1c\x1c\x1c\x0e\x38\x0e\x38\x07\x70\x07\x70\x03\xe0\x03\xe0\x01\xc0\x01\xc0\x03\x80\x03\x80\x07\x00\x07\x00\x0e\x00\x0e\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xfe\x3f\xfe\x00\x1c\x00\x1c\x00\x70\x00\x70\x01\xc0\x01\xc0\x07\x00\x07\x00\x1c\x00\x1c\x00\x3f\xfe\x3f\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x01\xc0\x01\xc0\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x1e\x00\x1e\x00\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x03\x80\x01\xc0\x01\xc0\x00\xf8\x00\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x00\x1f\x00\x03\x80\x03\x80\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x00\x78\x00\x78\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x01\xc0\x03\x80\x03\x80\x1f\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x9e\x07\x9e\x3c\xf0\x3c\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc0\x01\xc0\x07\x70\x07\x70\x1c\x1c\x1c\x1c\x70\x07\x70\x07\x70\x07\x70\x07\x7f\xff\x7f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

FONT = memoryview(_FONT)
