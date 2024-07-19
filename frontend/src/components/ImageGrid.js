import React, { useState, useEffect } from 'react';
import ImageCard from './ImageCard';
import Masonry from 'react-masonry-css';
import axios from 'axios';

const ImageGrid = () => {
  const [images, setImages] = useState([]);

  useEffect(() => {
    // Fetch images from the backend
    axios.get('http://localhost:5000/images')
      .then(response => {
        setImages(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the images!', error);
      });
  }, []);

  const breakpoints = {
    default: 3,
    1100: 2,
    700: 1
  };

  return (
    <Masonry
      breakpointCols={breakpoints}
      className="my-masonry-grid"
      columnClassName="my-masonry-grid_column">
      {images.map((image, index) => (
        <ImageCard key={index} image={image} />
      ))}
    </Masonry>
  );
}

export default ImageGrid;