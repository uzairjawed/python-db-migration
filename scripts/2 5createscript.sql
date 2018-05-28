CREATE TABLE `asset_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;


INSERT INTO `asset_type` (`id`, `name`, `description`)
VALUES
	(1, 'Brochure', ''),
	(2, 'Document', ''),
	(3, 'Price List', ''),
	(4, 'Main Image', ''),
	(5, 'Main Image HD', 'Main image used for high definition cases'),
	(6, 'Thumbnail Image', ''),
	(7, 'Thumbnail Image HD', ''),
	(8, 'Video', ''),
	(9, 'Press Release', ''),
	(12, 'Feature Text', 'File type for the features sections, must be a .rtf file to work in the sales library.'),
	(13, 'Avatar', 'People\'s photos'),
	(14, 'Commercial Contact Image', ''),
	(15, 'Service Care Thumbnail', 'Service Care Thumbnail...'),
	(16, 'Service Care Main Image', 'Service Care Main Image..'),
	(17, 'Driving Experience', 'Driving Experience'),
	(18, 'Form Vehicle Thumbnail', ''),
	(19, 'Finance Comparison', '');
