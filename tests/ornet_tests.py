'''
A test suite for the ornet package.
'''
#Author: Marcus Hill

import os
import shutil
import unittest

import ornet.Pipeline as pipeline

input_path = './data/test_vid.avi'
out_path = os.path.join('.', 'outputs')
vid_name = 'test_vid'
full_video = os.path.join(out_path, vid_name + '.avi')
masks_path = os.path.join(out_path, vid_name + 'MASKS.npy')
downsampled_path = os.path.join(out_path, 'downsampled')
singles_path = os.path.join(out_path, 'singles')
intermediates_path = os.path.join(out_path, 'intermediates')
distances_path = os.path.join(out_path, 'distances')
tmp_path = os.path.join(out_path, 'tmp')

class OrnetTests(unittest.TestCase):

	def test_cell_segmentation(self):
		'''
		Tests the cell segmentation function defined in extract_cells.py.
		'''
		try:
			pipeline.cell_segmentation(vid_name, input_path, 
					os.path.join('data', vid_name + '.vtk'), out_path)
		except:
			self.assertTrue(False)

		self.assertTrue(True)

	def test_downsample_vid(self):
		'''
		Tests the downsampling function defined in Pipeline.py
		'''

		try:
			pipeline.downsample_vid(vid_name, input_path, masks_path, 
						downsampled_path, 100)
		except:
			self.assertTrue(False)

		self.assertTrue(True)

	def test_singles_and_grayscale(self):
		'''
		Tests the cell extraction function defined in extract_helper.py, and
		tests the grayscale conversion function defined in cells_to_gray.py.
		'''

		try:
			pipeline.generate_single_vids(
					os.path.join(downsampled_path, vid_name + '.avi'),
					masks_path, tmp_path)
			pipeline.convert_to_grayscale(os.path.join(tmp_path, 
							'test_vid_1.avi'), tmp_path)
		except:
			self.assertTrue(False)

		self.assertTrue(True)

	def test_compute_gmm_intermediates(self):
		'''
		Tests the GMM process defined in the gmm subpackage.
		'''

		try:
			pipeline.compute_gmm_intermediates(tmp_path, intermediates_path)
		except:
			self.assertTrue(False)

		self.assertTrue(True)

	def test_compute_distances(self):
		'''
		Tests the Jensen-Shannon divergence function defined in affinityfunc.py.
		'''

		try:
			pipeline.compute_distances(intermediates_path, distances_path)
		except:
			self.assertTrue(False)

		self.assertTrue(True)

if __name__ == '__main__':

	os.makedirs(out_path, exist_ok=True)
	os.makedirs(downsampled_path, exist_ok=True)
	os.makedirs(singles_path, exist_ok =True)
	os.makedirs(intermediates_path, exist_ok =True)
	os.makedirs(distances_path, exist_ok=True)
	os.makedirs(tmp_path, exist_ok=True)
	
	unittest.main(exit=False)
	shutil.rmtree('./outputs')
