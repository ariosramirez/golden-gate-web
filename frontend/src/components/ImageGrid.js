import React from 'react';
import Masonry from 'react-masonry-css';
import ImageCard from './ImageCard';
import image1 from '../assets/images/placeholders/image1.jpg';
import image2 from '../assets/images/placeholders/image2.jpg';
import image3 from '../assets/images/placeholders/image3.jpg';
import image4 from '../assets/images/placeholders/image4.jpg';
import image5 from '../assets/images/placeholders/image5.jpg';
import image6 from '../assets/images/placeholders/image6.jpg';
import profile1 from '../assets/images/users/profile-1.avif';
import logo from '../assets/images/placeholders/logo.png';

const images = [
  { src: image1, alt: 'Golden Gate 1', tags: ['Bridge', 'Iconic', 'San Francisco'], author: 'Courtney Hill: test' },
  { src: image2, alt: 'Golden Gate 2', tags: ['Sunset', 'Scenic', 'Tourist Spot'], author: 'Courtney Hill: test' },
  { src: image3, alt: 'Golden Gate 3', tags: ['Fog', 'Mystical'], author: 'Courtney Hill: test' },
  { src: image4, alt: 'Golden Gate 4', tags: ['Architecture', 'Engineering'], author: 'Courtney Hill: test' },
  { src: image5, alt: 'Golden Gate 5', tags: ['Panoramic', 'Landmark'], author: 'Courtney Hill: test' },
  { src: image6, alt: 'Golden Gate 6', tags: ['Dawn', 'Reflection', 'Iconic'], author: 'Courtney Hill: test' }
];

const breakpoints = {
  default: 3,
  1100: 2,
  700: 1
};

function ImageGrid() {
  return (
    <Masonry
      breakpointCols={breakpoints}
      className="my-masonry-grid"
      columnClassName="my-masonry-grid_column">
      {images.map((image, index) => (
        <ImageCard key={index} image={image} logo={logo} profileImg={profile1} />
      ))}
    </Masonry>
  );
}

export default ImageGrid;