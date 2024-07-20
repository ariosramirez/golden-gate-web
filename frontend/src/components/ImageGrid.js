import React, { useState, useEffect, useCallback } from 'react';
import ImageCard from './ImageCard';
import Masonry from 'react-masonry-css';
import axios from 'axios';

const ImageGrid = () => {
  const [images, setImages] = useState([]);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [isLoading, setIsLoading] = useState(false);

  const syncImages = async () => {
    try {
      const syncResponse = await axios.get('http://localhost:5000/sync');
      console.log(syncResponse.data.message);
    } catch (error) {
      console.error('There was an error syncing the images!', error);
    }
  };

  const fetchImages = useCallback(async (pageNum) => {
    setIsLoading(true);
    try {
      const response = await axios.get(`http://localhost:5000/images?page=${pageNum}&limit=30`);
      if (response.data.length === 0) {
        await syncImages();
        const retryResponse = await axios.get(`http://localhost:5000/images?page=${pageNum}&limit=30`);
        if (retryResponse.data.length === 0) {
          setHasMore(false);
        } else {
          setImages(prevImages => [...prevImages, ...retryResponse.data]);
        }
      } else {
        setImages(prevImages => [...prevImages, ...response.data]);
      }
    } catch (error) {
      console.error('There was an error fetching the images!', error);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchImages(page); // Fetch the first page of images initially
  }, [fetchImages, page]);

  const loadMoreImages = () => {
    setPage(prevPage => {
      const nextPage = prevPage + 1;
      fetchImages(nextPage);
      return nextPage;
    });
  };

  const breakpoints = {
    default: 3,
    1100: 2,
    700: 1
  };

  return (
    <div>
      <Masonry
        breakpointCols={breakpoints}
        className="my-masonry-grid"
        columnClassName="my-masonry-grid_column">
        {images.map((image, index) => (
          <ImageCard key={index} image={image} />
        ))}
      </Masonry>
      {hasMore && (
        <button onClick={loadMoreImages} className="load-more-button" disabled={isLoading}>
          {isLoading ? 'Loading...' : 'Más 🌉'}
        </button>
      )}
    </div>
  );
}

export default ImageGrid;