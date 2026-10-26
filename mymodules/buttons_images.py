from mymodules.builder import Builder

class Img(object):
    # get the categories images, will be used once you click on some the categories to change those images with active or inactive
    image1 = Builder.builder.get_object("image1")
    image2 = Builder.builder.get_object("image2")
    image3 = Builder.builder.get_object("image3")
    image4 = Builder.builder.get_object("image4")
    image5 = Builder.builder.get_object("image5")
    image6 = Builder.builder.get_object("image6")