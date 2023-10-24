import qrcode
import qrcode.image.pil


def creation_qr_code(url, filename):
    """
    Create a QR code image from a given URL
    and save it to a specified filename.

    Args:
        url (str): The URL to be encoded in the QR code.
        filename (str): The name of the file (without extension)
        to save the QR code image.

    Example:
        To create a QR code for the URL "https://www.example.com"
        and save it as "example_qr":
        >>> creation_qr_code("https://www.example.com", "example_qr")

    This function uses the qrcode library to generate a QR code image
    with the given URL.
    The resulting image is saved in the "qr_codes" directory
    with the specified filename and ".png" extension.

    Note:
        Ensure that the qrcode library is installed in your environment
        before using this function.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    image = qr.make_image(image_factory=qrcode.image.pil.PilImage)
    image.save(f"qr_codes/{filename}.png")
