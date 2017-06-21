import imgaug as ia
from imgaug import augmenters as iaa

def rotate_batch(images, degrees):
	seq = iaa.Affine(
			rotate=degrees, # rotate by degrees
			order=ia.ALL, # use any of scikit-image's interpolation methods
			cval=0, # if mode is constant
			mode='constant' # use any of scikit-image's warping modes (see 2nd image from the top for examples)
		)

	return seq.augment_images(images)

def fliplr(images):
	"""Horizontal flip half of all images"""
	seq = iaa.Fliplr(0.5)
	return seq.augment_images(images)
