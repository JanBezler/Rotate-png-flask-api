from PIL import Image
import numpy as np
from flask import Flask, send_file, request, Response


class RotateImage():

    def __init__(self, im):
        self.white = np.array([255, 255, 255])
        self.red = np.array([255, 0, 0])

        self.im = im
        self.npim = np.asarray(im)
        self.line_orientation = 0

        self.line_orientation = self.search_wr_line(self.npim)

        self.im = self.im.rotate(90 * self.line_orientation, expand=True)

    def search_wr_line(self, image):
        for i, row in enumerate(image):
            for j, _ in enumerate(row):
                try:
                    if (row[j] == self.white).all():
                        if (row[j+1] == self.white).all() & (row[j+2] == self.white).all():
                            if (row[j-1] == self.red).all() & (row[j-2] == self.red).all() & (row[j-3] == self.red).all():
                                return 1
                            elif (row[j+3] == self.red).all() & (row[j+4] == self.red).all() & (row[j+5] == self.red).all():
                                return 3

                        if (image[i+1][j] == self.white).all() & (image[i+2][j] == self.white).all():
                            if (image[i-1][j] == self.red).all() & (image[i-2][j] == self.red).all() & (image[i-3][j] == self.red).all():
                                return 2
                            elif (image[i+3][j] == self.red).all() & (image[i+4][j] == self.red).all() & (image[i+5][j] == self.red).all():
                                return 4

                except IndexError:
                    pass
        return 0


app = Flask(__name__)


@app.route('/rotate', methods=['POST'])
def rotate():
    f = request.files["image"]
    image = RotateImage(Image.open(f))

    if bool(image.line_orientation):
        image.im.save("output_image.png")
        return send_file("output_image.png", mimetype="image/png")
    else:
        return Response(status=204)


if __name__ == "__main__":
    app.run(debug=False)
